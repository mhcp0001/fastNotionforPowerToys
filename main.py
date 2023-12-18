import os
from notion_client import Client
from settings import *


token = NOTION_API_TOKEN
database_id = NOTION_DATABASE_ID
client = Client(auth=token)  # token: インテグレーションのシークレット情報


def add_row_to_notion_database(database_id):
    response = client.pages.create(
        **{
            "parent": {"database_id": database_id},
            # ページのプロパティを指定する
            "properties": {
                "名前": {"title": [{"text": {"content": "Pythonで追加"}}]},
                "Status": {
                    "status": {
                        "name": "未着手",  # Done, In progress, Not started
                    }
                },
                "気持ち": {
                    "rich_text": [
                        {
                            "text": {
                                "content": f"test",
                            }
                        }
                    ]
                },
            },  # end properties
        }
    )

    print("notion database create completed")
    print(response)  # 追加した内容を表示する


print(add_row_to_notion_database(database_id))
