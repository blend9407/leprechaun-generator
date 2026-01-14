# Agent Token Usage Protocol
## For Leprechaun Name Generator Project

## Overview
All 6 specialized agents MUST follow this protocol to ensure we stay within the $5 token budget.

## The 6 Specialized Agents
1. **Developer** - Core application development
2. **UI Designer** - Design system and interfaces
3. **Security** - Security testing and compliance
4. **Market Research** - Market analysis and validation
5. **Code Quality** - Code review and testing
6. **Image Analysis** - Image processing and optimization
7. **Token Management** (Me) - Budget control and monitoring

## Mandatory Reporting Requirements

### 1. After Each Major Task
Every agent MUST report token usage after completing a major task:

```python
# Example reporting code (can be run in terminal)
cd /a0/usr/projects/yemadesignstudio/leprechaun-generator
python3 -c "
from token_tracker import agent_report
result = agent_report(
    agent_type='developer',  # Change to your agent type
    task='Created Flask backend',
    message='Full implementation of Flask server with...',
    complexity='complex'  # simple/medium/complex/very_complex
)
print(f'Reported: {result["estimated_cost"]}')
"
```

### 2. Quick Estimation Before Large Tasks
Before starting large tasks, estimate token usage:

```python
python3 -c "
from token_tracker import quick_estimate
text = 'Your planned task description here...'
tokens, cost = quick_estimate(text, 'developer')
print(f'Estimated: {tokens} tokens, ${cost}')
"
```

### 3. Daily Summary
At the end of each day, run:
```bash
cd /a0/usr/projects/yemadesignstudio/leprechaun-generator
python3 -c "
from token_tracker import TokenTracker
tracker = TokenTracker()
summary = tracker.get_summary()
print(f'Daily Summary:')
print(f'  Total: ${summary["total_spent"]:.2f} / $5.00')
print(f'  Remaining: ${summary["remaining_budget"]:.2f}')
print(f'  On Track: {"YES" if summary["on_track"] else "NO"}')
"
```

## Token Optimization Rules (MUST FOLLOW)

### Rule 1: Code Reuse Over Regeneration
```python
# BAD: Regenerating existing code
# "Create a new Flask app from scratch"

# GOOD: Reusing existing code
# "Check /components/ for existing Flask setup and modify"
# "Use §§include(/path/to/existing_code.py) as base"
```

### Rule 2: File Inclusion Over Rewriting
```python
# BAD: Copy-pasting long file content
# (Rewrites entire file in message)

# GOOD: Using include replacement
# "Here's the updated file: §§include(/path/to/file.py)"
```

### Rule 3: Concise Instructions
```python
# BAD: Long, verbose instructions
# "I need you to create a Flask application that has routes for..."

# GOOD: Specific, concise instructions
# "Add /generate-name route to existing Flask app"
```

### Rule 4: Batch Related Tasks
```python
# BAD: Multiple separate requests
# 1. "Create route A"
# 2. "Create route B"
# 3. "Create route C"

# GOOD: Single batched request
# "Create routes A, B, C with these specifications..."
```

## Complexity Guidelines

### Simple (1.0x multiplier)
- Simple queries
- File reading
- Basic commands

### Medium (1.5x multiplier)
- Code review
- Design analysis
- Market research queries

### Complex (2.5x multiplier)
- Problem solving
- New feature development
- Security testing

### Very Complex (4.0x multiplier)
- Major system architecture
- Complex algorithm design
- Integration of multiple systems

## Alert System

### Thresholds and Actions:
1. **50% ($2.50)**: Warning - Review optimization opportunities
2. **80% ($4.00)**: Critical - Limit non-essential work
3. **90% ($4.50)**: Emergency - Stop non-essential work
4. **95% ($4.75)**: Lockdown - Essential work only

### Check Current Status:
```bash
cd /a0/usr/projects/yemadesignstudio/leprechaun-generator
cat token_logs/daily_usage.json
cat token_logs/alerts.json
```

## Agent-Specific Guidelines

### Developer Agent
- Daily cap: $0.35 (17,500 tokens)
- Focus: Code reuse, existing components
- Use: `agent_type='developer'`

### UI Designer Agent
- Daily cap: $0.14 (7,000 tokens)
- Focus: Reuse design system components
- Use: `agent_type='ui_designer'`

### Security Agent
- Daily cap: $0.105 (5,250 tokens)
- Focus: Automated checks where possible
- Use: `agent_type='security'`

### Market Research Agent
- Daily cap: $0.105 (5,250 tokens)
- Focus: Batch research queries
- Use: `agent_type='market_research'`

### Code Quality Agent
- Daily cap: $0.105 (5,250 tokens)
- Focus: Automated linting tools
- Use: `agent_type='code_quality'`

### Image Analysis Agent
- Daily cap: $0.105 (5,250 tokens)
- Focus: Local image processing when possible
- Use: `agent_type='image_analysis'`

## Emergency Procedures

### If Approaching Budget Limit:
1. **Immediately** stop all non-essential work
2. **Switch** to local tools (terminal, python scripts)
3. **Use** existing code/components
4. **Report** to Token Management agent

### If Budget Exceeded:
1. **Complete lockdown** - only critical bug fixes
2. **Use only** local processing
3. **No new** AI agent calls

## Quick Reference Commands

```bash
# 1. Report a task
python3 -c "from token_tracker import agent_report; \
agent_report('developer', 'Task name', 'Description', 'medium')"

# 2. Quick estimate
python3 -c "from token_tracker import quick_estimate; \
t, c = quick_estimate('Your text', 'developer'); \
print(f'{t} tokens, ${c}')"

# 3. Check budget
python3 -c "from token_tracker import TokenTracker; \
t=TokenTracker(); s=t.get_summary(); \
print(f'${s[\"total_spent\"]:.2f}/$5.00 ({s[\"percentage_used\"]}%)')"

# 4. Get optimization tips
python3 -c "from token_tracker import TokenTracker; \
t=TokenTracker(); \
for tip in t.get_optimization_suggestions()[:3]: print(f'- {tip}')"
```

## Contact
- **Token Management Agent**: Responsible for budget control
- **Location**: /a0/usr/projects/yemadesignstudio/leprechaun-generator
- **Files**: token_tracker.py, token_tracker.md, agent_token_protocol.md

**Last Updated**: 2026-01-13
**Status**: ACTIVE - ALL AGENTS MUST COMPLY
