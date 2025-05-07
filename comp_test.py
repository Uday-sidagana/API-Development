from google.genai import types
from google import genai
from composio_gemini import Action, ComposioToolSet, App
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
toolset = ComposioToolSet(api_key=os.getenv('COMPOSIO_API_KEY'))


#Composio Tools
# tools = toolset.get_tools(actions=[Action.GITHUB_GET_THE_AUTHENTICATED_USER])
tools = toolset.get_tools(actions=[Action.GITHUB_GET_THE_AUTHENTICATED_USER])

config = types.GenerateContentConfig(tools = tools)

#OpenAI workflow
# task = "Get my Github Username"

# message = [
#     {'role': 'system', 'content': 'You are expert in using tools'},
#     {'role': 'client', 'content': task},
# ]

# response = client.chat.completions.create(
#     model='chatgpt-4o-latest',
#     messages= message,
#     tools=tools,
#     tool_choice= 'auto',

# )


chat = client.chats.create(model='gemini-2.0-flash', config=config)
response = chat.send_message(
    "Get my Github Username"
)

print(response.text)

#Use ComposioToolset to handle calls
# result = toolset.handle_tool_calls(response)

# print(result)
