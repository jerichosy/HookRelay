from fastapi import APIRouter, HTTPException

from app.services import discord_service, processor_service

router = APIRouter()

@router.post("/api/webhooks/{webhook_id}/{webhook_token}")
def handle_webhook(webhook_id: str, webhook_token: str, payload: dict):
    try:
        embed_object, avatar_url = processor_service.process_webhook(payload)
        # TODO: Get the actual response (usually 204) and return it
        discord_service.send_webhook_message(webhook_id, webhook_token, embed_object, avatar_url)
        return {"message": "Webhook processed successfully"}
    except Exception as e:
        # TODO: Get the actual error and raise HTTPException
        # TODO: If underlying error was network related, get actual status code
        print(dir(e))
        raise HTTPException(status_code=400, detail=str(e))
