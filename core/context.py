import discord
from discord.ext import commands
from core.config import DENY_EMOJI, SUCCESS_EMOJI, WARN_EMOJI


DENY_COLOR = 12395813
SUCCESS_COLOR = 5487909
WARN_COLOR = 12107045

def make_deny_embed(message: str) -> discord.Embed:
    return discord.Embed(description=f"{DENY_EMOJI} {message}", color=DENY_COLOR)


def make_success_embed(message: str) -> discord.Embed:
    return discord.Embed(description=f"{SUCCESS_EMOJI} {message}", color=SUCCESS_COLOR)


def make_warn_embed(message: str) -> discord.Embed:
    return discord.Embed(description=f"{WARN_EMOJI} {message}", color=WARN_COLOR)


class Context(commands.Context):
    """Extended command context with standardized embed helpers."""

    def deny(self, message: str) -> discord.Embed:
        return make_deny_embed(message)

    def success(self, message: str) -> discord.Embed:
        return make_success_embed(message)

    def warn(self, message: str) -> discord.Embed:
        return make_warn_embed(message)


async def _interaction_response_deny(self, message: str, **kwargs):
    return await self.send_message(embed=make_deny_embed(message), **kwargs)


async def _interaction_response_success(self, message: str, **kwargs):
    return await self.send_message(embed=make_success_embed(message), **kwargs)


async def _interaction_response_warn(self, message: str, **kwargs):
    return await self.send_message(embed=make_warn_embed(message), **kwargs)


async def _interaction_followup_deny(self, message: str, **kwargs):
    return await self.send(embed=make_deny_embed(message), **kwargs)


async def _interaction_followup_success(self, message: str, **kwargs):
    return await self.send(embed=make_success_embed(message), **kwargs)


async def _interaction_followup_warn(self, message: str, **kwargs):
    return await self.send(embed=make_warn_embed(message), **kwargs)


discord.InteractionResponse.deny = _interaction_response_deny
discord.InteractionResponse.success = _interaction_response_success
discord.InteractionResponse.warn = _interaction_response_warn

discord.Webhook.deny = _interaction_followup_deny
discord.Webhook.success = _interaction_followup_success
discord.Webhook.warn = _interaction_followup_warn
