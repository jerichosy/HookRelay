import os

import requests


async def send_webhook_message(webhook_id: str, webhook_token: str, embed_message: dict):
    webhook_url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"
    data = {
        "embeds": [embed_message]
    }
    response = requests.post(webhook_url, json=data)
    response.raise_for_status()