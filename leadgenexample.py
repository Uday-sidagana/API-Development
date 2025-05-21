# from composio_llamaindex import ComposioToolSet, App, Action
# from llama_index.core.agent import FunctionCallingAgentWorker
# from llama_index.core.llms import ChatMessage
# from llama_index.llms.openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()
# toolset = ComposioToolSet()
# tools = toolset.get_tools(apps=[App.PEOPLEDATALABS, App.GOOGLESHEETS])

# llm = OpenAI(model="gpt-4o")

# spreadsheetid = '14ZXMZng--vldDj4cPAI7hHqLyBNXVhJzqreODQU_3g8'
# # Set up prefix messages for the agent
# prefix_messages = [
#     ChatMessage(
#         role="system",
#         content=( f"Get any information from the people data labs and fill it in the spreadsheet with spreadsheetID: {spreadsheetid}"
#         #     f"""
#         #     You are a lead research agent. Based on user input, find 10 relevant leads using people data labs.
#         #     After finding the leads, create a Google Sheet with the details for the lead description, and spreadsheet ID: ${spreadsheetid}.
#         #     Print the list of people and their details and the link to the google sheet."""
#         # ),
#         ),
#     )
# ]

# agent = FunctionCallingAgentWorker(
#     tools=tools, # type: ignore
#     llm=llm,
#     prefix_messages=prefix_messages,
#     max_function_calls=10,
#     allow_parallel_tool_calls=False,
#     verbose=True,
# ).as_agent()

# user_input = f"Create a list of 10 of company information and fill them in the spreadsheet with spreadsheet id {spreadsheetid}"
# response = agent.chat(user_input)




from composio_llamaindex import ComposioToolSet, App, Action
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
toolset = ComposioToolSet(api_key="")
tools = toolset.get_tools(apps=[App.PEOPLEDATALABS, App.GOOGLESHEETS])

llm = OpenAI(model="gpt-4o")

spreadsheetid = '14ZXMZng--vldDj4cPAI7hHqLyBNXVhJzqreODQU_3g8'
# Set up prefix messages for the agent
prefix_messages = [
    ChatMessage(
        role="system",
        content=(
            f"""
            You are a lead research agent. Based on user input, find 10 relevant leads using people data labs.
            After finding the leads, create a Google Sheet with the details for the lead description, and spreadsheet ID: ${spreadsheetid}.
            Print the list of people and their details and the link to the google sheet."""
        ),
    )
]

agent = FunctionCallingAgentWorker(
    tools=tools, # type: ignore
    llm=llm,
    prefix_messages=prefix_messages,
    max_function_calls=10,
    allow_parallel_tool_calls=False,
    verbose=True,
).as_agent()

lead_description = 'Senior frontend developers in San Francisco'
user_input = f"Create a lead list based on the description: {lead_description}"
response = agent.chat(user_input)