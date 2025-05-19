import { openai } from "@ai-sdk/openai";  
import { VercelAIToolSet } from "composio-core";  
import { generateText } from 'ai';  
  
// Create a minimal schema processor function  
function fixSchema({ actionName, toolSchema }) {  
  // Make a deep copy of the schema  
  const modifiedSchema = JSON.parse(JSON.stringify(toolSchema));  
    
  // Only add additionalProperties: false to the parameters object  
  if (modifiedSchema.parameters) {  
    modifiedSchema.parameters.additionalProperties = false;  
  }  
    
  return modifiedSchema;  
}  
  
// Initialize the VercelAIToolSet  
const toolset = new VercelAIToolSet();  
  
// Add the schema processor  
toolset.addSchemaProcessor(fixSchema);  
  
// Get the tools with the fixed schema  
const tools = await toolset.getTools({ actions: ["GMAIL_LIST_THREADS"] }, "test");  
  
// Generate text using the OpenAI Responses API  
const output = await generateText({  
    model: openai.responses('gpt-4'),  
    prompt: 'List all the Gmail Threads Title and subjects',  
    tools: tools  
});  
  
console.log(output);