#!/usr/bin/env python3
"""
Token Management & Budget Control System
for Leprechaun Name Generator Project
"""

import json
import os
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Constants
BUDGET_TOTAL = 5.00  # $5 total budget
TOKEN_RATE = 0.02  # $0.02 per 1000 tokens (DeepSeek approximate)
ALERT_THRESHOLDS = [0.5, 0.8, 0.9, 0.95]  # 50%, 80%, 90%, 95%

# Budget allocation by category
BUDGET_ALLOCATION = {
    "development": 2.50,  # 50%
    "design_ui": 1.00,   # 20%
    "testing_security": 0.75,  # 15%
    "marketing_deployment": 0.75  # 15%
}

# Agent types and their categories
AGENT_CATEGORIES = {
    "developer": "development",
    "ui_designer": "design_ui",
    "security": "testing_security",
    "market_research": "marketing_deployment",
    "code_quality": "testing_security",
    "image_analysis": "design_ui",
    "token_management": "development"  # My own category
}

class TokenTracker:
    def __init__(self, log_dir: str = "token_logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
        # Initialize tracking files
        self.daily_log = self.log_dir / "daily_usage.json"
        self.agent_log = self.log_dir / "agent_logs.json"
        self.alerts_log = self.log_dir / "alerts.json"
        
        self._initialize_files()
    
    def _initialize_files(self):
        """Initialize tracking files if they don't exist"""
        if not self.daily_log.exists():
            with open(self.daily_log, 'w') as f:
                json.dump({
                    "total_spent": 0.0,
                    "total_tokens": 0,
                    "daily_breakdown": {},
                    "category_breakdown": {cat: 0.0 for cat in BUDGET_ALLOCATION}
                }, f, indent=2)
        
        if not self.agent_log.exists():
            with open(self.agent_log, 'w') as f:
                json.dump({"agent_interactions": []}, f, indent=2)
        
        if not self.alerts_log.exists():
            with open(self.alerts_log, 'w') as f:
                json.dump({"alerts": []}, f, indent=2)
    
    def estimate_tokens(self, text: str, agent_type: str, task_complexity: str = "medium") -> int:
        """Estimate token count based on text length and task complexity"""
        # Rough estimation: ~4 characters per token for English
        base_tokens = max(1, len(text) // 4)
        
        # Complexity multipliers
        multipliers = {
            "simple": 1.0,      # Simple queries
            "medium": 1.5,      # Code review, analysis
            "complex": 2.5,     # Problem solving, design
            "very_complex": 4.0 # Major development tasks
        }
        
        multiplier = multipliers.get(task_complexity, 1.5)
        estimated = int(base_tokens * multiplier)
        
        # Agent-specific adjustments
        agent_adjustments = {
            "developer": 1.2,      # Developers use more tokens
            "ui_designer": 1.1,    # Designers moderate
            "security": 1.0,       # Security checks
            "market_research": 1.3, # Research intensive
            "code_quality": 0.8,   # Automated checks
            "image_analysis": 1.5, # Vision models expensive
            "token_management": 0.5 # My own tracking
        }
        
        adjustment = agent_adjustments.get(agent_type, 1.0)
        return int(estimated * adjustment)
    
    def log_interaction(self, agent_type: str, task: str, text: str, 
                       task_complexity: str = "medium") -> Dict:
        """Log an agent interaction and return cost estimate"""
        # Estimate tokens
        tokens = self.estimate_tokens(text, agent_type, task_complexity)
        cost = tokens * TOKEN_RATE / 1000  # Convert to dollars
        
        # Get current date
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Load current data
        with open(self.daily_log, 'r') as f:
            daily_data = json.load(f)
        
        with open(self.agent_log, 'r') as f:
            agent_data = json.load(f)
        
        # Update daily totals
        daily_data["total_spent"] += cost
        daily_data["total_tokens"] += tokens
        
        # Update daily breakdown
        if today not in daily_data["daily_breakdown"]:
            daily_data["daily_breakdown"][today] = {"cost": 0.0, "tokens": 0}
        daily_data["daily_breakdown"][today]["cost"] += cost
        daily_data["daily_breakdown"][today]["tokens"] += tokens
        
        # Update category breakdown
        category = AGENT_CATEGORIES.get(agent_type, "development")
        daily_data["category_breakdown"][category] += cost
        
        # Save updated daily data
        with open(self.daily_log, 'w') as f:
            json.dump(daily_data, f, indent=2)
        
        # Log agent interaction
        interaction = {
            "timestamp": datetime.datetime.now().isoformat(),
            "agent": agent_type,
            "category": category,
            "task": task,
            "estimated_tokens": tokens,
            "estimated_cost": round(cost, 4),
            "complexity": task_complexity
        }
        
        agent_data["agent_interactions"].append(interaction)
        with open(self.agent_log, 'w') as f:
            json.dump(agent_data, f, indent=2)
        
        # Check for alerts
        self._check_alerts(daily_data["total_spent"])
        
        return interaction
    
    def _check_alerts(self, total_spent: float):
        """Check if we've crossed any alert thresholds"""
        percentage = total_spent / BUDGET_TOTAL
        
        with open(self.alerts_log, 'r') as f:
            alerts_data = json.load(f)
        
        for threshold in ALERT_THRESHOLDS:
            if percentage >= threshold:
                alert_name = f"{int(threshold*100)}%_threshold"
                
                # Check if this alert already exists today
                today = datetime.datetime.now().strftime("%Y-%m-%d")
                existing_alerts = [a for a in alerts_data["alerts"] 
                                  if a["name"] == alert_name and a["date"] == today]
                
                if not existing_alerts:
                    alert = {
                        "name": alert_name,
                        "threshold": threshold,
                        "actual_percentage": round(percentage, 3),
                        "total_spent": round(total_spent, 2),
                        "date": today,
                        "timestamp": datetime.datetime.now().isoformat(),
                        "message": self._get_alert_message(threshold, total_spent)
                    }
                    alerts_data["alerts"].append(alert)
                    
                    with open(self.alerts_log, 'w') as f:
                        json.dump(alerts_data, f, indent=2)
    
    def _get_alert_message(self, threshold: float, total_spent: float) -> str:
        """Generate appropriate alert message"""
        percentage = total_spent / BUDGET_TOTAL
        remaining = BUDGET_TOTAL - total_spent
        
        if threshold == 0.5:
            return f"WARNING: 50% budget reached! ${total_spent:.2f} spent, ${remaining:.2f} remaining."
        elif threshold == 0.8:
            return f"CRITICAL WARNING: 80% budget reached! ${total_spent:.2f} spent, ${remaining:.2f} remaining. Limit non-essential work."
        elif threshold == 0.9:
            return f"EMERGENCY: 90% budget reached! ${total_spent:.2f} spent, ${remaining:.2f} remaining. STOP NON-ESSENTIAL WORK."
        elif threshold == 0.95:
            return f"LOCKDOWN: 95% budget reached! ${total_spent:.2f} spent, ${remaining:.2f} remaining. COMPLETE LOCKDOWN - ESSENTIAL WORK ONLY."
        return ""
    
    def get_summary(self) -> Dict:
        """Get current budget summary"""
        with open(self.daily_log, 'r') as f:
            daily_data = json.load(f)
        
        total_spent = daily_data["total_spent"]
        total_tokens = daily_data["total_tokens"]
        percentage = total_spent / BUDGET_TOTAL
        remaining = BUDGET_TOTAL - total_spent
        
        # Calculate daily averages if we have data
        days = len(daily_data["daily_breakdown"])
        daily_avg = total_spent / max(1, days)
        
        # Project remaining days (5-day challenge)
        projected_total = daily_avg * 5
        
        return {
            "total_budget": BUDGET_TOTAL,
            "total_spent": round(total_spent, 2),
            "total_tokens": total_tokens,
            "percentage_used": round(percentage * 100, 1),
            "remaining_budget": round(remaining, 2),
            "daily_average": round(daily_avg, 2),
            "projected_5_day_total": round(projected_total, 2),
            "on_track": projected_total <= BUDGET_TOTAL,
            "category_breakdown": daily_data["category_breakdown"],
            "daily_breakdown": daily_data["daily_breakdown"]
        }
    
    def get_optimization_suggestions(self) -> List[str]:
        """Generate optimization suggestions based on current usage"""
        suggestions = []
        
        with open(self.daily_log, 'r') as f:
            daily_data = json.load(f)
        
        with open(self.agent_log, 'r') as f:
            agent_data = json.load(f)
        
        # Check category usage
        for category, spent in daily_data["category_breakdown"].items():
            allocation = BUDGET_ALLOCATION.get(category, 0)
            if allocation > 0 and spent > allocation * 0.8:  # Over 80% of allocation
                suggestions.append(f"{category.replace('_', ' ').title()} category at {spent/allocation*100:.1f}% of allocation. Consider reducing {category} work.")
        
        # Check for code reuse opportunities
        developer_tasks = [i for i in agent_data["agent_interactions"] 
                          if i["agent"] == "developer" and "code" in i["task"].lower()]
        if len(developer_tasks) > 5:
            suggestions.append(f"{len(developer_tasks)} developer code tasks detected. Implement code reuse library to reduce token usage.")
        
        # Check for file inclusion usage
        all_tasks = agent_data["agent_interactions"]
        text_lengths = [len(i["task"]) for i in all_tasks]
        avg_length = sum(text_lengths) / max(1, len(text_lengths))
        if avg_length > 1000:  # Long task descriptions
            suggestions.append(f"Average task description length: {avg_length:.0f} characters. Use §§include() for long content instead of rewriting.")
        
        # General suggestions
        suggestions.extend([
            "Use code reuse instead of regeneration - check existing components first",
            "Use §§include(/path/to/file) for file content instead of rewriting",
            "Keep agent instructions concise and specific",
            "Batch related tasks to minimize context switching",
            "Use local tools (terminal, python) when possible instead of LLM calls"
        ])
        
        return suggestions

# Utility functions for agents to use
def quick_estimate(text: str, agent_type: str = "developer") -> Tuple[int, float]:
    """Quick token and cost estimate for agents"""
    tracker = TokenTracker()
    tokens = tracker.estimate_tokens(text, agent_type)
    cost = tokens * TOKEN_RATE / 1000
    return tokens, round(cost, 4)

def agent_report(agent_type: str, task: str, message: str, complexity: str = "medium"):
    """Simple function for agents to report their usage"""
    tracker = TokenTracker()
    return tracker.log_interaction(agent_type, task, message, complexity)

if __name__ == "__main__":
    # Test the tracker
    tracker = TokenTracker()
    
    # Log some test interactions
    test_interactions = [
        ("developer", "Create Flask backend setup", "Setting up Flask server with...", "complex"),
        ("ui_designer", "Design mockup review", "Reviewing the generator mockup...", "medium"),
        ("market_research", "Competitor analysis", "Analyzing competitor features...", "medium"),
    ]
    
    for agent, task, text, complexity in test_interactions:
        result = tracker.log_interaction(agent, task, text, complexity)
        print(f"Logged: {agent} - {task[:30]}... - Cost: ${result['estimated_cost']}")
    
    # Get summary
    summary = tracker.get_summary()
    print(f"\nBudget Summary:")
    print(f"  Total Spent: ${summary['total_spent']} / ${summary['total_budget']}")
    print(f"  Percentage: {summary['percentage_used']}%")
    print(f"  Remaining: ${summary['remaining_budget']}")
    print(f"  On Track: {'YES' if summary['on_track'] else 'NO'}")
    
    # Get suggestions
    suggestions = tracker.get_optimization_suggestions()
    print(f"\nOptimization Suggestions:")
    for i, suggestion in enumerate(suggestions[:3], 1):
        print(f"  {i}. {suggestion}")
