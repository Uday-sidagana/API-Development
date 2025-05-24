// sgo23fdtwtdoy!5xhysewtp--- inserted !

import { OpenAIToolSet } from "composio-core";
import { OpenAI } from "openai";

const toolset = new OpenAIToolSet({apiKey:""});
const tools = await toolset.getTools({
  actions: ["SERPAPI_SEARCH"]
});

const client = new OpenAI();

const messages = [
  { role: "user",content: "Search for Composio and give a 3 line summary" }
];

while (true) {
  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages,
    tools,
    tool_choice: "auto"
  });

  const choice = response.choices[0].message;

  // Case: model responds with final answer, no tool call neededc
  if (!choice.tool_calls) {
    console.log("Final output:", choice.content || "");
    break;
  }

  // Handle the tool call
  const toolCallId = choice.tool_calls[0].id;

  const result = await toolset.handleToolCall(response);

  // Append tool call + tool result to messages
  messages.push({
    role: "assistant",
    tool_calls: choice.tool_calls
  });

  messages.push({
    role: "tool",
    tool_call_id: toolCallId,
    content: JSON.stringify(result)
  });
}
