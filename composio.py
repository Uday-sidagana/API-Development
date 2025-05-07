from composio_openai import ComposioToolSet, Action
from openai import OpenAI

# Initialize Composio ToolSet
# It automatically picks up COMPOSIO_API_KEY from env vars
# Uses the 'default' entity_id if not specified
toolset = ComposioToolSet()
client = OpenAI()

#Composio Tools
tools = toolset.get_tools(actions=[Action.GITHUB_GET_THE_AUTHENTICATED_USER])

#OpenAI workflow
task = "Get my Github Username"

message = [
    {'role': 'system', 'content': 'You are expert in using tools'},
    {'role': 'client', 'content': task},
]

response = client.chat.completions.create(
    model='chatgpt-4o-latest',
    messages= message,
    tools=tools,
    tool_choice= 'auto',

)


#Use ComposioToolset to handle calls
result = toolset.handle_tool_calls(response)

print(result)
