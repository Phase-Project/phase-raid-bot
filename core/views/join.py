import discord
from core.config import MAIN_SERVER_ID, VERIFIED_ROLE_ID, PHASE_INVITE, ICON

REQUIRED_SERVER_ID = MAIN_SERVER_ID

FALLBACK_ICON = ICON


def get_access_denied_view(bot: discord.ClientUser) -> discord.ui.LayoutView:
    if bot and hasattr(bot, "display_avatar") and bot.display_avatar and bot.display_avatar.url:
        avatar_url = bot.display_avatar.url
    else:
        avatar_url = FALLBACK_ICON

    class Components(discord.ui.LayoutView):
        container1 = discord.ui.Container(
            discord.ui.Section(
                discord.ui.TextDisplay(content="# **access denied**\nyou need to be verified and in the server in order to use this bot."),
                accessory=discord.ui.Thumbnail(
                    media=avatar_url,
                ),
            ),
            discord.ui.Separator(visible=True, spacing=discord.SeparatorSpacing.small),
            discord.ui.ActionRow(
                    discord.ui.Button(
                        url=PHASE_INVITE,
                        style=discord.ButtonStyle.link,
                        label="join",
                    ),
            ),
        )

    return Components()
