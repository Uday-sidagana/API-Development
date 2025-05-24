
# sgo23fdtwt!doy5xhysewtp--- inserted !

from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet(api_key="")

response = composio_toolset.execute_action(entity_id="notdefault",action="SERPAPI_DUCK_DUCK_GO_SEARCH", params={"query": "Composio"})

print(response)