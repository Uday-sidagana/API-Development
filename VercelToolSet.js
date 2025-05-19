import { openai } from "@ai-sdk/openai";
import { VercelAIToolSet } from "composio-core";
import { generateText } from 'ai';

const toolset = new VercelAIToolSet();


// const tools = await toolset.getTools({ actions: ["GMAIL_LIST_THREADS"] });

// const output = await generateText({
//     model: openai("gpt-4"),
//     streamText: false,
//     tools,
//     prompt: 'List all the Gmail Threads"',
//     maxToolRoundtrips: 5,
// });


// console.log(output);

const tools = await toolset.getTools({ actions: ["GMAIL_LIST_THREADS"] },"test");
console.log(tools[0])

tools[0].parameters.additionalProperties = false;

const output = await generateText({
    // --- Responses API -----------------------------------------------------
    model: openai.responses('gpt-4'),      // <-- MUST use openai.responses
    prompt: 'List all the Gmail Threads Title and subjects',
    tools: tools
    
  });

console.log(output);

// 1 Install:  npm i ai @ai-sdk/openai
// 2 Set env:  export OPENAI_API_KEY="sk-..."



// async function main() {
//   const { text } = await generateText({
//     // --- Responses API -----------------------------------------------------
//     model: openai.responses('gpt-4o'),      // <-- MUST use openai.responses
//     prompt: 'Say hello from the Responses API',
//     tools:
//   });

//   console.log(text);                        // ➜  "Hello from GPT-4o!"
// }

// main().catch(console.error);