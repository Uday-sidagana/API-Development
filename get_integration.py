# api_key="***REMOVED***"
from composio import ComposioToolSet, App
toolset = ComposioToolSet()

integration = toolset.get_integration(id="5ac_E2Tj2Drr6iOH")

print(integration.expectedInputFields)
connection_request = toolset.initiate_connection(
integration_id=integration.id,
entity_id="default",
)

print(connection_request.redirectUrl)
print(connection_request.connectedAccountId)



