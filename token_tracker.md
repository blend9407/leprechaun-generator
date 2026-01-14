# Token Management & Budget Control System
## Leprechaun Name Generator Project

**Critical Mission**: Monitor and control AI token usage to ensure we DO NOT exceed the $5 total budget.

### Project Context
- **5-day challenge**: 3 days setup + 2 days revenue generation
- **6 specialized agents**: developer, UI designer, security, market research, code quality, image analysis
- **Current location**: /a0/usr/projects/yemadesignstudio/leprechaun-generator
- **Budget**: $5.00 total

### Budget Allocation Strategy
| Category | Allocation | Percentage | Max Tokens (approx)* |
|----------|------------|------------|----------------------|
| Development | $2.50 | 50% | ~125,000 tokens |
| Design/UI | $1.00 | 20% | ~50,000 tokens |
| Testing/Security | $0.75 | 15% | ~37,500 tokens |
| Marketing/Deployment | $0.75 | 15% | ~37,500 tokens |
| **TOTAL** | **$5.00** | **100%** | **~250,000 tokens** |

*Based on approximate rate of $0.02 per 1,000 tokens (DeepSeek pricing)

### Alert Thresholds
- **50% threshold**: $2.50 spent → WARNING
- **80% threshold**: $4.00 spent → CRITICAL WARNING
- **90% threshold**: $4.50 spent → EMERGENCY - STOP NON-ESSENTIAL WORK
- **95% threshold**: $4.75 spent → COMPLETE LOCKDOWN

### Token Optimization Guidelines
1. **Code Reuse**: Always check for existing code before regenerating
2. **File Inclusion**: Use `§§include(/path/to/file)` instead of rewriting content
3. **Concise Instructions**: Keep agent messages focused and specific
4. **Batch Operations**: Group related tasks to minimize context switching
5. **Local Processing**: Use local tools (terminal, python) when possible instead of LLM calls

### Current Usage (Baseline - Day 0)
| Agent Type | Estimated Daily Tokens | Estimated Cost/Day | Notes |
|------------|------------------------|-------------------|-------|
| Developer | 25,000 | $0.50 | High token usage expected during setup |
| UI Designer | 10,000 | $0.20 | Moderate usage for design iterations |
| Security | 7,500 | $0.15 | Lower but consistent monitoring |
| Market Research | 15,000 | $0.30 | Initial research intensive |
| Code Quality | 5,000 | $0.10 | Automated checks lower token usage |
| Image Analysis | 7,500 | $0.15 | Vision models may be more expensive |
| **Daily Total** | **70,000** | **$1.40** | |
| **Projected 5-Day** | **350,000** | **$7.00** | **EXCEEDS BUDGET!** |

### Immediate Actions Required
1. **Reduce baseline by 30%** to stay within budget
2. Implement strict token counting for all agent interactions
3. Create automated tracking system
4. Establish daily review meetings (simulated)

### Tracking Methodology
1. **Manual Log**: Each agent reports token usage after major tasks
2. **Estimation Guide**:
   - Simple query: ~500 tokens
   - Code review: ~1,000-2,000 tokens
   - File analysis: ~2,000-5,000 tokens
   - Complex problem solving: ~5,000-10,000 tokens
3. **Daily Caps**:
   - Developer: 17,500 tokens ($0.35)
   - UI Designer: 7,000 tokens ($0.14)
   - Others: 5,250 tokens each ($0.105)

### Next Steps
1. Create token logging script
2. Review current agent communications for optimization
3. Establish alert system
4. Coordinate budget awareness with all agents

**Last Updated**: 2026-01-13
**Current Status**: INITIAL SETUP - NEEDS OPTIMIZATION

## Agent Token Protocol Implementation

### Quick Start for Agents
1. **Always work in project directory**:
   ```bash
   cd /a0/usr/projects/yemadesignstudio/leprechaun-generator
   ```

2. **Before starting work, estimate**:
   ```bash
   python3 -c "from token_tracker import quick_estimate; t, c = quick_estimate('Your task description', 'your_agent_type'); print(f'Estimated: {t} tokens, ${c}')"
   ```

3. **After completing work, report**:
   ```bash
   python3 -c "from token_tracker import agent_report; result = agent_report('your_agent_type', 'Task Name', 'Task description', 'complexity'); print(f'Reported: ${result[\"estimated_cost\"]}')"
   ```

### Agent Types Reference
- `developer` - Core development work
- `ui_designer` - Design and UI work
- `security` - Security testing
- `market_research` - Market analysis
- `code_quality` - Code review
- `image_analysis` - Image processing

### Complexity Levels
- `simple` - Basic queries, file operations
- `medium` - Analysis, review, design
- `complex` - Problem solving, development
- `very_complex` - Major architecture

### Current Project Status
Based on initial setup, we have:
- **Total Budget**: $5.00
- **Days Remaining**: 5 (3 setup + 2 revenue)
- **Agents Active**: 6 specialized agents
- **Current Phase**: Day 1 complete (design system, mockups, templates)

### Daily Allocation Targets
| Day | Development | Design/UI | Testing/Security | Marketing/Deployment | Total |
|-----|-------------|-----------|------------------|---------------------|-------|
| 1   | $0.50       | $0.20     | $0.15            | $0.15               | $1.00 |
| 2   | $0.75       | $0.30     | $0.20            | $0.25               | $1.50 |
| 3   | $0.75       | $0.30     | $0.20            | $0.25               | $1.50 |
| 4   | $0.25       | $0.10     | $0.10            | $0.05               | $0.50 |
| 5   | $0.25       | $0.10     | $0.10            | $0.05               | $0.50 |
| **Total** | **$2.50** | **$1.00** | **$0.75** | **$0.75** | **$5.00** |

### Optimization Success Metrics
- **Target**: 30% reduction from baseline projections
- **Current Baseline**: 70,000 tokens/day ($1.40)
- **Target**: 49,000 tokens/day ($0.98)
- **Savings Needed**: 21,000 tokens/day ($0.42)

### File Inclusion Best Practices
```python
# Instead of rewriting:
"Here's the code: def function(): ..."

# Use include:
"Here's the updated file: §§include(/a0/usr/projects/yemadesignstudio/leprechaun-generator/file.py)"
```

### Code Reuse Examples
1. **Check existing components first**:
   ```bash
   ls components/
   ls design-system/
   ```

2. **Reuse design system elements**:
   ```python
   # Instead of designing new button
   # Use: design-system/design-system.md button styles
   ```

3. **Reuse PDF templates**:
   ```python
   # Instead of creating new template
   # Modify: pdf-templates/classic-emerald-template.html
   ```

### Emergency Contact
- **Token Management Agent**: Monitoring budget 24/7
- **Location**: This directory
- **Files to check**: token_logs/daily_usage.json, token_logs/alerts.json
- **Immediate action required if**: alerts.json contains new warnings

### Success Checklist
- [ ] All agents have read agent_token_protocol.md
- [ ] All agents are reporting usage
- [ ] Daily budget targets are being met
- [ ] Optimization suggestions are being implemented
- [ ] No alerts in alerts.json

**Last Updated**: 2026-01-13
**Status**: ACTIVE - TRACKING IN PROGRESS
