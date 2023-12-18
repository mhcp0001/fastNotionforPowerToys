import os
from notion_client import Client

token = os.environ.get("NOTION_TOKEN")
client = Client(auth=token)  # token: インテグレーションのシークレット情報


def get_all_notion_users():
    response = client.users.list()
    return response
