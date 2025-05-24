// ***REMOVED***

// api-keysgo23fdtwtdoy5xhysewtp
import { ComposioToolSet } from "composio-core"

const toolset = new ComposioToolSet({ apiKey: "" })

// const res = await toolset.executeAction({ entityId:"issueTest",actionName: "LINKEDIN_CREATE_LINKED_IN_POST", params: { author: "urn:li:person:s6v7d9qvl2", commentary: "ComposioTest" } })

const res = await toolset.executeAction({ entityId:"notdefault",actionName: "SERPAPI_SEARCH", params: { query: "Composio"} })

console.log(res)