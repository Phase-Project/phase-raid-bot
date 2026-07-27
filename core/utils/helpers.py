import discord
import aiohttp
from core.config import (
    OWNER_IDS,
    LOG_CHANNEL_ID,
    PHASE_INVITE,
)


user_farm_tokens: dict[int, list[str]] = {}


async def log_command(interaction: discord.Interaction, name: str, details: str):
    username = interaction.user.name
    user_mention = interaction.user.mention
    avatar_url = interaction.user.display_avatar.url
    channel = interaction.client.get_channel(LOG_CHANNEL_ID)

    class Components(discord.ui.LayoutView):
        container1 = discord.ui.Container(
            discord.ui.Section(
                discord.ui.TextDisplay(
                    content=f"# COMMAND USED\n\nuser: `{username}` ({user_mention})\ncommand `{name}`"
                ),
                accessory=discord.ui.Thumbnail(
                    media=avatar_url
                ),
            ),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.TextDisplay(content=f"details:\n```{details}```"),
        )

    view = Components()
    await channel.send(view=view)


async def send_message_http(session: aiohttp.ClientSession, application_id: int, interaction_token: str, content: str):
    """
    Sends an HTTP message to a Discord webhook.
    """
    url = f"https://discord.com/api/v10/webhooks/{application_id}/{interaction_token}"
    payload = {"content": content, "allowed_mentions": {"parse": ["everyone", "users", "roles"]}}
    async with session.post(url, json=payload) as resp:
        return resp.status
