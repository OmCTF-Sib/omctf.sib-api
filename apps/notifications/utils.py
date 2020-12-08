from discord import RequestsWebhookAdapter, Webhook
from django.conf import settings


def send_discord_message(text: str) -> None:
    webhook = Webhook.from_url(settings.DISCORD_WEBHOOK_URL, adapter=RequestsWebhookAdapter())
    webhook.send(text)
