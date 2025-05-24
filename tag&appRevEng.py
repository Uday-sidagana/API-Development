from composio import ComposioToolSet
from composio import Action, App
import requests

composio_toolset = ComposioToolSet()


def get_app_with_tags(app_name):
    app_data = composio_toolset.get_app(app=app_name)
    tags_data = requests.get(f"https://backend.composio.dev/api/v2/actions/list/tags?apps={app_name}").json()
    # Now you have tags_data, which includes actions and their tags
    return app_data, tags_data
