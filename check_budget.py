#!/usr/bin/env python3

import json
import os
from datetime import datetime
from token_tracker import TokenTracker

def main():
    print("📊 LEPRECHAUN GENERATOR BUDGET ANALYSIS")
    print("=" * 50)
    
    # Initialize tracker
    tracker = TokenTracker()
    summary = tracker.get_summary()
    
    # Budget status
    print("\n💰 BUDGET STATUS")
    print(f"Total Budget: $5.00")
    print(f"Spent: ${summary['total_spent']:.2f}")
    print(f"Remaining: ${summary['remaining_budget']:.2f}")
    print(f"Percentage Used: {summary['percentage_used']}%")
    print(f"On Track: {'✅ YES' if summary['on_track'] else '❌ NO'}")
    
    # Category breakdown
    print("\n📈 CATEGORY BREAKDOWN")
    allocations = {
        'development': 2.5,
        'design_ui': 1.0,
        'testing_security': 0.75,
        'marketing_deployment': 0.75
    }
    
    for category, spent in summary['category_breakdown'].items():
        allocation = allocations.get(category, 0)
        percent = (spent / allocation * 100) if allocation > 0 else 0
        bar_length = 20
        filled = int(percent / 5)
        bar = '█' * filled + '░' * (bar_length - filled)
        category_name = category.replace('_', ' ').title()
        print(f"  {category_name:20} ${spent:.2f}/${allocation:.2f} {bar} {percent:.1f}%")
    
    # Check logs
    print("\n📝 AGENT ACTIVITY LOGS")
    logs_path = "token_logs/agent_logs.json"
    if os.path.exists(logs_path):
        with open(logs_path, 'r') as f:
            logs = json.load(f)
        
        interactions = logs.get('agent_interactions', [])
        print(f"Total interactions recorded: {len(interactions)}")
        
        if interactions:
            print("\nRecent activity (last 5):")
            for entry in interactions[-5:]:
                ts = datetime.fromisoformat(entry['timestamp']).strftime('%H:%M')
                agent = entry['agent']
                task = entry['task'][:40] + '...' if len(entry['task']) > 40 else entry['task']
                cost = entry['estimated_cost']
                print(f"  {ts} {agent:15} {task:45} ${cost:.4f}")
    else:
        print("No agent logs found")
    
    # Check alerts
    print("\n🚨 ALERT STATUS")
    alerts_path = "token_logs/alerts.json"
    if os.path.exists(alerts_path):
        with open(alerts_path, 'r') as f:
            alerts_data = json.load(f)
        
        active_alerts = alerts_data.get('alerts', [])
        if active_alerts:
            print(f"Active alerts: {len(active_alerts)}")
            for alert in active_alerts[-3:]:
                ts = datetime.fromisoformat(alert['timestamp']).strftime('%H:%M')
                print(f"  {ts}: {alert['message']}")
        else:
            print("✅ No active alerts")
    else:
        print("No alerts file found")
    
    # Optimization tips
    print("\n💡 OPTIMIZATION SUGGESTIONS")
    tips = tracker.get_optimization_suggestions()
    for i, tip in enumerate(tips[:3], 1):
        print(f"{i}. {tip}")
    
    # Daily targets
    print("\n🎯 DAILY TARGETS (5-day challenge)")
    daily_targets = [
        ("Day 1 (Setup)", 1.00),
        ("Day 2 (Dev)", 1.50),
        ("Day 3 (Dev)", 1.50),
        ("Day 4 (Revenue)", 0.50),
        ("Day 5 (Revenue)", 0.50)
    ]
    
    total_spent = summary['total_spent']
    for day, target in daily_targets:
        status = "✅" if total_spent <= target else "❌"
        print(f"  {status} {day}: ${total_spent:.2f}/${target:.2f}")
    
    print("\n" + "=" * 50)
    print("Token Management Agent - Monitoring Active")

if __name__ == "__main__":
    main()
