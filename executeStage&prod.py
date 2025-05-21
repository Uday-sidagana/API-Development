#wv6rkjbru4akztvfxwpl1s!  ---added ! to avoid github cred conflicts at the end



# from composio import ComposioToolSet
# from composio import Action, App

# composio_toolset = ComposioToolSet()

# response= composio_toolset.execute_action(entity_id="3",
#                                           action=Action.NOTION_GET_ABOUT_ME,
#                                           params={},)

# print(response)




from composio import ComposioToolSet
from composio import Action, App

composio_toolset = ComposioToolSet(api_key="", base_url="https://staging-backend.composio.dev/api")

response= composio_toolset.execute_action(entity_id="2",
                                          action=Action.NOTION_GET_ABOUT_ME,
                                          params={},)

print(response)