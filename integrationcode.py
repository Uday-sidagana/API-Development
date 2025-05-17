'''from composio import Composio

# Initialize the Composio client
composio = Composio(api_key="***REMOVED***")
app = composio.apps.get(name="monday")
# Create a new integration
integration = composio.integrations.create(
    app_id=app.appId,
    auth_config = {"scopes":"account:read, assets:read, boards:read, boards:write, docs:read, docs:write, me:read, notifications:write, tags:read, teams:read, teams:write, updates:read, updates:write, users:read, users:write, webhooks:read, webhooks:write, workspaces:read, workspaces:write"},
    auth_mode="OAUTH2",
    force_new_integration=True,
    name="monday_P3NW",
    use_composio_auth=True
)
'''
# api_key="***REMOVED***"
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
