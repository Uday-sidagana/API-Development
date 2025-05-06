from composio_openai import ComposioToolSet, Action
from openai import OpenAI

# Initialize Composio ToolSet
# It automatically picks up COMPOSIO_API_KEY from env vars
# Uses the 'default' entity_id if not specified
toolset = ComposioToolSet()
client = OpenAI()
