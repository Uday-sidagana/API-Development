from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet(api_key="***REMOVED***")

response = composio_toolset.execute_action(action=Action.JIRA_GET_PROJECT, params={'projectIdOrKey':'CPG'})
print(response)