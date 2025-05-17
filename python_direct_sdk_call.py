# export COMPOSIO_LOGGING_LEVEL=debug
# COMPOSIO_LOG_VERBOSITY=3COMPOSIO_LOG_VERBOSITY=3
# ***REMOVED***
from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet(api_key="")

response = composio_toolset.execute_action(entity_id="usefulagents",
                                           action="SNOWFLAKE_DESCRIBE_TABLE",
                                            params={"database":"TESTCOMPOSIO", "schema_name":"TESTCOMPOSIO", "table_name":"USERS"})
# Direct Execution targeting a specific connection
# response= composio_toolset.execute_action(connected_account_id="ca_j876qdxfdUuN",
#                                           action=Action.GMAIL_SEND_EMAIL,
#                                           params={"recipient_email":"uday.sidgana@gmail.com", "body":"Hell there, this is a test"},
#                                           )

print(response)

# AccountID = composio_toolset.get
# print(AccountID)


