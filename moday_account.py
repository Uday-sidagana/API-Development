from composio import ComposioToolSet, App
toolset = ComposioToolSet()

integration = toolset.get_integration(id="6d0fc0ac-fe8b-4d83-8d4f-fab7d9742d2c")
# Collect auth params from your users
print(integration.expectedInputFields)

connection_request = toolset.initiate_connection(
    integration_id=integration.id,
    entity_id="default",
)

# Redirect step require for OAuth Flow
print(connection_request.redirectUrl)
print(connection_request.connectedAccountId)