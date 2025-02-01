from praisonaiagents import Agent, Tools
from praisonaiagents.tools import execute_code, analyze_code, format_code, lint_code, disassemble_code # Code Tools
from praisonaiagents.tools import execute_command, list_processes, kill_process, get_system_info # Shell Tools
from praisonaiagents.tools import duckduckgo # Web Search Tool



agent = Agent(
    instructions="You are a Programming Agent", self_reflect=True, min_reflect=5, max_reflect=10, 
    tools=[execute_code, analyze_code, format_code, lint_code, disassemble_code, execute_command, list_processes, kill_process, get_system_info, duckduckgo]
)
agent.start(
    "Write a react script that will have a form to create new tasks, display and list tasks, each row having an edit or delete button"
)