from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from composio_langchain import ComposioToolSet,Action
import logging

prompt = hub.pull("hwchase17/openai-functions-agent")
composio_toolset = ComposioToolSet(api_key="", entity_id="")
tools = composio_toolset.get_tools(actions=['YOUTUBE_SEARCH_YOU_TUBE'])

def filter_youtube_results(result: dict) -> dict:
    """Filters youtube list to only include descirption and title."""
    # Pass through errors or unsuccessful executions unchanged
    if not result.get("successful") or "data" not in result:
        return result

    original_messages = result["data"].get("messages", [])
    if not isinstance(original_messages, list):
        return result # Return if data format is unexpected

    filtered_results = []
    for result in original_messages:
        filtered_results.append({
            "title": result.get("title"),
            "description": result.get("description"),
        })

    # Construct the new result dictionary
    processed_result = {
        "successful": True,
        # Use a clear key for the filtered data
        "data": {"summary": filtered_results},
        "error": None
    }
    return processed_result

# Get tools with the postprocessor
processed_tools = composio_toolset.get_tools(
    actions=[Action.YOUTUBE_VIDEO_DETAILS],
    processors={
        "post": {Action.YOUTUBE_SEARCH_YOU_TUBE: filter_youtube_results}
    }
)
# Use processed_tools in the agent
agent = create_openai_functions_agent(processed_tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=processed_tools, verbose=False)
task = "Go to youtube and search for 'NCERT Class 10 Science Chapter 1' and return top 10 search results."
result = agent_executor.invoke({"input": task})