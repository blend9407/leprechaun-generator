#!/bin/bash

# Token Management Utilities for Leprechaun Generator Project
# Usage: ./token_utils.sh [command] [args]

PROJECT_DIR="/a0/usr/projects/yemadesignstudio/leprechaun-generator"
cd "$PROJECT_DIR" || exit 1

case "$1" in
    "estimate")
        # Estimate token usage for a task
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: ./token_utils.sh estimate [agent_type] [task_description]"
            echo "Agent types: developer, ui_designer, security, market_research, code_quality, image_analysis"
            exit 1
        fi
        python3 -c "
from token_tracker import quick_estimate
text = '''$3'''
tokens, cost = quick_estimate(text, '$2')
print(f'📊 ESTIMATE FOR $2:')
print(f'  Tokens: {tokens:,}')
print(f'  Cost: ${cost:.4f}')
print(f'  Budget Impact: {(cost/5.0)*100:.2f}% of total budget')
"
        ;;
    
    "report")
        # Report completed task
        if [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ]; then
            echo "Usage: ./token_utils.sh report [agent_type] [task_name] [task_description]"
            echo "Optional: Add [complexity] (simple/medium/complex/very_complex, default: medium)"
            exit 1
        fi
        COMPLEXITY="${5:-medium}"
        python3 -c "
from token_tracker import agent_report
result = agent_report(
    agent_type='$2',
    task='$3',
    message='''$4''',
    complexity='$COMPLEXITY'
)
print(f'✅ REPORTED TASK: $3')
print(f'  Agent: $2')
print(f'  Complexity: $COMPLEXITY')
print(f'  Estimated Cost: ${result["estimated_cost"]:.4f}')
print(f'  Total Spent: ${result["total_spent"]:.2f}/$5.00')
"
        ;;
    
    "status")
        # Check budget status
        python3 -c "
from token_tracker import TokenTracker
tracker = TokenTracker()
summary = tracker.get_summary()
print('💰 BUDGET STATUS')
print('=' * 40)
print(f'Total Budget: $5.00')
print(f'Spent: ${summary["total_spent"]:.2f}')
print(f'Remaining: ${summary["remaining_budget"]:.2f}')
print(f'Percentage Used: {summary["percentage_used"]}%')
print(f'On Track: {"✅ YES" if summary["on_track"] else "❌ NO"}')
print()
print('📈 CATEGORY BREAKDOWN:')
for category, spent in summary["category_breakdown"].items():
    allocation = {'development': 2.5, 'design_ui': 1.0, 'testing_security': 0.75, 'marketing_deployment': 0.75}[category]
    percent = (spent/allocation)*100 if allocation > 0 else 0
    bar = '█' * int(percent/5) + '░' * (20 - int(percent/5))
    print(f'  {category.replace("_", " ").title():20} ${spent:.2f}/${allocation:.2f} {bar} {percent:.1f}%')
"
        ;;
    
    "alerts")
        # Check for alerts
        if [ -f "token_logs/alerts.json" ]; then
            python3 -c "
import json
with open('token_logs/alerts.json', 'r') as f:
    data = json.load(f)
if data['alerts']:
    print('🚨 ACTIVE ALERTS:')
    for alert in data['alerts'][-5:]:  # Show last 5 alerts
        print(f'  {alert["timestamp"]}: {alert["message"]}')
else:
    print('✅ No active alerts')
"
        else
            echo "No alerts file found"
        fi
        ;;
    
    "tips")
        # Get optimization tips
        python3 -c "
from token_tracker import TokenTracker
tracker = TokenTracker()
tips = tracker.get_optimization_suggestions()
print('💡 OPTIMIZATION TIPS:')
for i, tip in enumerate(tips[:5], 1):
    print(f'{i}. {tip}')
"
        ;;
    
    "log")
        # Show recent agent logs
        if [ -f "token_logs/agent_logs.json" ]; then
            python3 -c "
import json
from datetime import datetime
with open('token_logs/agent_logs.json', 'r') as f:
    data = json.load(f)
print('📝 RECENT AGENT ACTIVITY (last 10):')
for entry in data['agent_interactions'][-10:]:
    ts = datetime.fromisoformat(entry['timestamp']).strftime('%H:%M')
    print(f'{ts} {entry["agent"]:15} {entry["task"][:30]}... ${entry["estimated_cost"]:.4f}')
"
        else
            echo "No agent logs found"
        fi
        ;;
    
    "help"|*)
        echo "Token Management Utilities"
        echo "========================="
        echo "Commands:"
        echo "  estimate [agent] [task]    - Estimate token cost before task"
        echo "  report [agent] [name] [desc] [complexity] - Report completed task"
        echo "  status                     - Check budget status"
        echo "  alerts                     - Check for alerts"
        echo "  tips                       - Get optimization tips"
        echo "  log                        - Show recent agent activity"
        echo "  help                       - Show this help"
        echo ""
        echo "Agent types: developer, ui_designer, security, market_research, code_quality, image_analysis"
        echo "Complexity: simple, medium, complex, very_complex"
        ;;
esac
