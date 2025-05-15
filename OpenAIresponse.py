from openai import OpenAI
from composio_openai import ComposioToolSet, Action

openai_client = OpenAI()
composio_toolset = ComposioToolSet()

tools = composio_toolset.get_tools(actions=["GMAIL_LIST_THREADS"])

assistant_instruction = "You are a super intelligent personal assistant"

assistant = openai_client.beta.assistants.create(
  name="Personal Assistant",
  instructions=assistant_instruction,
  model="gpt-4o",
  tools=tools,
)

thread = openai_client.beta.threads.create()
my_task = "List all Gmail Threads in a good format"
message = openai_client.beta.threads.messages.create(thread_id=thread.id,role="user",content=my_task)

run = openai_client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id)

response_after_tool_calls = composio_toolset.wait_and_handle_assistant_tool_calls(
    client=openai_client,
    run=run,
    thread=thread,
)

print(response_after_tool_calls)
print("Successful run")



# from openai import OpenAI
# from composio_openai import Action, ComposioToolSet

# # Initialize clients
# openai_client = OpenAI()
# composio_toolset = ComposioToolSet()

# # Get Gmail tool schema (for function calling)
# tools = composio_toolset.get_tools(actions=[Action.GMAIL_LIST_THREADS])

# # User request
# messages = [{"role": "user", "content": "List all my Gmail threads in a structured format."}]

# # Make Chat Completion request
# response = openai_client.chat.completions.create(
#     model="gpt-4-turbo-preview",  # or "gpt-3.5-turbo"
#     messages=messages,
#     tools=tools,
#     tool_choice="auto",  # Let the model decide whether to call the tool
# )

# # Check if the model wants to call the Gmail tool
# response_message = response.choices[0].message
# tool_calls = response_message.tool_calls

# if tool_calls:
#     # Handle tool execution (ComposioToolSet can help here)
#     tool_outputs = []
#     for tool_call in tool_calls:
#         if tool_call.function.name == "GMAIL_LIST_THREADS":
#             # Execute the Gmail tool
#             result = composio_toolset.handle_tool_calls(
#                 tool_call=tool_call,
#                 client=openai_client,
#             )
#             tool_outputs.append({
#                 "tool_call_id": tool_call.id,
#                 "role": "tool",
#                 "name": tool_call.function.name,
#                 "content": str(result),
#             })
    
#     # Submit tool outputs back to OpenAI for a final response
#     messages.append(response_message)  # Add assistant's tool request
#     messages.extend(tool_outputs)      # Add tool responses

#     # Get the final assistant response
#     final_response = openai_client.chat.completions.create(
#         model="gpt-4-turbo-preview",
#         messages=messages,
#     )
#     print(final_response.choices[0].message.content)
# else:
#     print(response_message.content)