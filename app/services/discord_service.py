import requests


def send_webhook_message(webhook_id: str, webhook_token: str, embed_object: dict, avatar_url: str = None):
    webhook_url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"
    # JSON/Form param options: https://discord.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "embeds": [embed_object],
        # "allowed_mentions": { "parse": [] }  # No need if mention is in embed since it won't ping
    }
    if avatar_url is not None:
        data["avatar_url"] = avatar_url
    response = requests.post(webhook_url, json=data)
    response.raise_for_status()