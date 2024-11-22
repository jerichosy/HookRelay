from fastapi import APIRouter, HTTPException

from app.services import discord_service, processor_service

router = APIRouter()

@router.post("/api/webhooks/{webhook_id}/{webhook_token}")
async def handle_webhook(webhook_id: str, webhook_token: str, payload: dict):
    try:
        embed_message = processor_service.process_webhook(payload)
        await discord_service.send_webhook_message(webhook_id, webhook_token, embed_message)
        return {"message": "Webhook processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
