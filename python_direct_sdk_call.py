# export COMPOSIO_LOGGING_LEVEL=debug
from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet(api_key="***REMOVED***")

response = composio_toolset.execute_action(action="GMAIL_LIST_THREADS", params={})
                                           
print(response)


