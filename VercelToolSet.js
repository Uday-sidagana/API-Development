import { openai } from "@ai-sdk/openai";
import { VercelAIToolSet } from "composio-core";
import { generateText } from "ai";

const toolset = new VercelAIToolSet();


const tools = await toolset.getTools({ actions: ["GMAIL_LIST_THREADS"] });

const output = await generateText({
    model: openai("gpt-4"),
    streamText: false,
    tools,
    prompt: 'List all the Gmail Threads"',
    maxToolRoundtrips: 5,
});


console.log(output);
