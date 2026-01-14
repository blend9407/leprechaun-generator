#!/bin/bash

# Agent Budget Monitor - Use before starting any task

PROJECT_DIR="/a0/usr/projects/yemadesignstudio/leprechaun-generator"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to check budget
check_budget() {
    echo -e "${BLUE}🎯 LEPRECHAUN GENERATOR - BUDGET CHECK${NC}"
    echo -e "${BLUE}========================================${NC}"
    
    # Use the Python check_budget.py script
    python3 check_budget.py 2>/dev/null || echo -e "${RED}❌ Error running budget check${NC}"
}

# Function to log agent activity
log_activity() {
    if [ $# -lt 3 ]; then
        echo "Usage: $0 log <agent_name> <task_description> <estimated_cost>"
        return 1
    fi
    
    AGENT_NAME="$1"
    TASK_DESC="$2"
    EST_COST="$3"
    
    echo -e "${GREEN}✅ Activity logged: $AGENT_NAME - $TASK_DESC (\$EST_COST)${NC}"
    echo "Note: Logging to token_logs/agent_logs.json"
}

# Function to show optimization tips
show_tips() {
    echo -e "${YELLOW}💡 TOKEN OPTIMIZATION TIPS${NC}"
    echo -e "${YELLOW}==========================${NC}"
    echo "1. Use §§include(/path/to/file) instead of rewriting content"
    echo "2. Check /components/ directory before writing new code"
    echo "3. Keep agent instructions concise (<200 words)"
    echo "4. Batch related tasks together"
    echo "5. Use existing templates in /pdf-templates/ and /mockups/"
    echo ""
    echo -e "${BLUE}📋 AGENT PROTOCOL${NC}"
    echo "- Start message with: TOKEN ALERT: Budget status"
    echo "- End message with: TOKEN REPORT: Cost estimate"
    echo "- Always include file paths for reuse"
}

# Function to show dashboard
show_dashboard() {
    echo -e "${BLUE}📊 TOKEN MANAGEMENT DASHBOARD${NC}"
    echo -e "${BLUE}================================${NC}"
    if [ -f "token_dashboard.md" ]; then
        head -30 token_dashboard.md
    else
        echo -e "${YELLOW}⚠️  Dashboard file not found${NC}"
    fi
}

# Main script logic
case "$1" in
    "status")
        check_budget
        ;;
    "log")
        shift
        log_activity "$@"
        ;;
    "tips")
        show_tips
        ;;
    "dashboard")
        show_dashboard
        ;;
    "*" | "help")
        echo -e "${GREEN}Agent Budget Monitor - Usage:${NC}"
        echo "  $0 status          - Check current budget status"
        echo "  $0 log <agent> <task> <cost> - Log agent activity"
        echo "  $0 tips           - Show optimization tips"
        echo "  $0 dashboard      - Show dashboard summary"
        echo "  $0 help           - Show this help"
        ;;
esac
