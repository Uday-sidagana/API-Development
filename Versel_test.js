import { openai } from "@ai-sdk/openai";
import { VercelAIToolSet } from "composio-core";
import { generateText } from 'ai';

const toolset = new VercelAIToolSet();


const tools = await toolset.getTools({ actions: ["GMAIL_LIST_THREADS"] }, "test");
// if (!tools.length) {
//   console.error("❌ Tool 'GMAIL_LIST_THREADS' not found.");node 
//   process.exit(1);
// }

const output = await generateText({
    model: openai("gpt-4"),
    streamText: false,
    tools,
    prompt: 'List all the Gmail Threads."',
    maxToolRoundtrips: 5,
});


console.log(output);