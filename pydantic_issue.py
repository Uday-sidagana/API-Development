
from dotenv import load_dotenv
import os

from composio import Action
from composio_pydanticai import ComposioToolSet
from pydantic_ai import Agent


agent = Agent(
    model="openai:gpt-4o-mini",
    system_prompt="Always use Notion tools if they help the user."
)

print("TOOLS  before register:", list_agent_tools(agent))   # → []

# ── register every Composio action as a tool ───────────────────────
for schema in ComposioToolSet.get_action_schemas():
    tool = ComposioToolSet
    agent.add_tool(tool)

print("TOOLS after  register:", list_agent_tools(agent))    # still []

# quick test run
result = agent.run_sync(
    "Listar tareas con Status In progress de DATABASE_ID=abc"
)
print("LLM reply:", result.output)