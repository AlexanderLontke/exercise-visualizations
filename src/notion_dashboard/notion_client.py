import json
import requests
from typing import Dict, Optional


class NotionClient:
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    def query_database(self, database_id: str, query_params: Optional[Dict] = None):
        if not query_params:
            query_params = {}
        url = f"https://api.notion.com/v1/databases/{database_id}/query"

        payload = json.dumps(query_params)
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-02-22",
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
