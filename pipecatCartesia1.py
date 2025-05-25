import asyncio
import os
from dotenv import load_dotenv
from composio import ComposioToolSet
from pipecat.services.openai.llm import OpenAILLMService
from pipecat.processors.aggregators.openai_llm_context import OpenAILLMContext

async def main():
    # Load environment variables
    load_dotenv(override=True)

    # Initialize Composio toolset and select your action
    toolset = ComposioToolSet()
    tools = toolset.get_action('GMAIL_FETCH_EMAILS')  # replace '<action_name>' with your action key

    # Initialize OpenAI LLM service with tools
    llm = OpenAILLMService(
        api_key=os.getenv('OPENAI_API_KEY'),
        toolset=toolset,
        tools=tools,
    )

    # Set up conversation context
    system_message = {'role': 'system', 'content': 'You are a helpful text assistant.'}
    context = OpenAILLMContext([system_message])
    context_agg = llm.create_context_aggregator(context)

    print("Starting text-only assistant. Type 'exit' to quit.")
    while True:
        user_input = input('You: ')
        if user_input.lower() in ('exit', 'quit'):
            print('Goodbye!')
            break

        # Add user message to context
        await context_agg.user().add_messages(user_input)

        # Generate response
        resp_message = await llm.generate(context.get_messages())

        # Print assistant's reply
        print('Assistant:', resp_message)

        # Add assistant message to context
        await context_agg.assistant().add_messages(resp_message)

if __name__ == '__main__':
    asyncio.run(main())
