# from composio import Composio

# # Initialize the Composio client
# composio = Composio(api_key="")
# app = composio.apps.get(name="jira")
# # Create a new integration
# integration = composio.integrations.create(
#     app_id=app.appId,
#     auth_config = {"oauth_redirect_uri":"https://backend.composio.dev/api/v1/auth-apps/add",
#                    "scopes":"read:jira-work,write:jira-work,manage:jira-project,manage:jira-configuration,read:jira-user,manage:jira-webhook,manage:jira-data-provider,read:servicedesk-request,manage:servicedesk-customer,write:servicedesk-request,read:servicemanagement-insight-objects,offline_access",
#                    "client_id": "",
#                    "client_secret": ""},
#     auth_mode="OAUTH2",
#     force_new_integration=True,
#     name="jira_AIAk",
#     use_composio_auth=False


# )

from composio import ComposioToolSet, App
toolset = ComposioToolSet()

integration = toolset.get_integration(id="5ad2748c-1a11-47ba-b2ae-400d32a7de45")
# Collect auth params from your users
print(integration.expectedInputFields)

connection_request = toolset.initiate_connection(
    integration_id=integration.id,
    entity_id="sdkstest",
)

# Redirect step require for OAuth Flow
print(connection_request.redirectUrl)
print(connection_request.connectedAccountId)

