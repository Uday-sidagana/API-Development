# import os
# from composio_openai import ComposioToolSet, App, Tag
# from dotenv import load_dotenv

# load_dotenv()

# composio_toolset = ComposioToolSet(api_key=os.getenv("COMPOSIO_API_KEY"))

# tools = composio_toolset.get_tools(apps=[App.HUBSPOT], tags=[])
# print(f"Composio tools: {len(tools)}")

# # Print the names of all tools
# print("Tool names:")
# for tool in tools:
#     name = tool.get('function', {}).get('name', 'Unknown')
#     print(f"- {name}")

# # Try to find anything related to tags in the structure
# for tool in tools:
#     function_data = tool.get('function', {})
#     for key in function_data.keys():
#         if 'tag' in key.lower():
#             print(f"Potential tag field found: {key}")
#             print(f"Value: {function_data[key]}")

# print("\nAvailable tags in Tag enum:")
# for name in dir(Tag):
#     if not name.startswith('_'):  # Skip private attributes
#         print(f"- {name}")

# #------ Tool structure
# '''tools = composio_toolset.get_tools(apps=[App.HUBSPOT], tags=[])
# print(f"Composio tools: {len(tools)}")

# # Print the structure of the first tool
# if tools:
#     first_tool = tools[0]
#     print(f"First tool type: {type(first_tool)}")
#     print(f"First tool keys: {first_tool.keys() if hasattr(first_tool, 'keys') else 'No keys method'}")
#     print(f"First tool content: {first_tool}")'''



# print(f"Composio tools: {len(tools)}")
