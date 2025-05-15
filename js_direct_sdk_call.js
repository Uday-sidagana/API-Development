import { ComposioToolSet } from "composio-core"

const toolset = new ComposioToolSet({ apiKey: "***REMOVED***" })

const res = await toolset.executeAction({ actionName: "GOOGLEDRIVE_DOWNLOAD_FILE", params: { file_id: "1oyOTbM5PGP3uR1hwIikhjtPAV9LYFM97" } })
console.log(res)