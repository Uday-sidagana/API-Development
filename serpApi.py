
from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet()

response = composio_toolset.execute_action( action="SERPAPI_DUCK_DUCK_GO_SEARCH", params={"query": "Composio"})

print(response)