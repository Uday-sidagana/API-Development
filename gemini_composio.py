from google.genai import types
import google.genai
from composio_gemini import Action, ComposioToolSet, App

client = google.genai.Client(api_key="")

toolset = ComposioToolSet()

tools = toolset.get_tools(
    apps=[
        App.GITHUB
    ]
)

config = types.GenerateContentConfig(tools=tools)

chat = client.chats.create(model="gemini-2.0-flash", config=config)

response = chat.send_message(
    "Can you get all my Repository",
)

print(response.text)
