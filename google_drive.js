import { ChatOpenAI } from "@langchain/openai";
import { createOpenAIFunctionsAgent, AgentExecutor } from "langchain/agents";
import { LangchainToolSet } from "composio-core";
import { pull } from "langchain/hub";
const llm = new ChatOpenAI({
  model: "gpt-4-turbo",
  temperature: 0,
});

const prompt = await pull("hwchase17/openai-functions-agent");

const toolset = new LangchainToolSet({ apiKey: "***REMOVED***" });
const tools = await toolset.getTools({ actions: ["GOOGLEDRIVE_DOWNLOAD_FILE"] });

const agent = await createOpenAIFunctionsAgent({llm, tools, prompt});
const agentExecutor = new AgentExecutor({ agent, tools, verbose: true });

const response = await agentExecutor.invoke({ input: "Download this file 'https://drive.google.com/file/d/1oyOTbM5PGP3uR1hwIikhjtPAV9LYFM97/view?usp=drive_link'" });
console.log(response);


// import { ComposioToolSet } from "composio-core"

// const toolset = new ComposioToolSet({ apiKey: "***REMOVED***" })

// const res = await toolset.executeAction({ actionName: "GOOGLEDRIVE_DOWNLOAD_FILE", params: { file_id: "1oyOTbM5PGP3uR1hwIikhjtPAV9LYFM97" } })
// console.log(res)