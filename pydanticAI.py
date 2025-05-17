from dotenv import load_dotenv
import os

from composio import Action
from composio_pydanticai import ComposioToolSet
from pydantic_ai import Agent

# Initialize toolset
composio_toolset = ComposioToolSet(api_key= os.getenv("COMPSIO_API_KEY"))

# Configure max retries for specific tools
max_retries = {
    Action.NOTION_GET_ABOUT_ME: 5   # Fewer retries for creation
}

# Get GitHub tools with retry configuration
tools = composio_toolset.get_tools(
    actions=[Action.NOTION_GET_ABOUT_ME],
    max_retries=max_retries,
    default_max_retries=3  # Default retries for tools not specified in max_retries
)


# Create an agent with the tools
agent = Agent(
    model="openai:gpt-4",  # Using a known model name
    tools=tools,
    system_prompt="""YYou are an Agent that interacts with Notion. When given a Task use the appropriate tools to complete the task.""",
)


# Define task
task = "Fetch my details from Notion and structure them"

# Run the agent synchronously
result = agent.run_sync(task)
print("Result:", result.data)
print("Trace:\n\n", result.all_messages())