import requests

import pyastodon


def get(url: str, endpoint: str, token=True, **params) -> str:
    client = pyastodon.Client.get()
    auth = {"Authorization": str(client.token)} if token else {}
    
    response = requests.get(f"https://{url}/{endpoint}", params, headers=auth)
    return response.content.decode("utf-8")

def post(url: str, endpoint: str, token=True, **data) -> str:
    client = pyastodon.Client.get()
    auth = {"Authorization": str(client.token)} if token else {}

    response = requests.post(f"https://{url}/{endpoint}", data, headers=auth)
    return response.content.decode("utf-8")