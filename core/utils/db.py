import asyncio
import json
import os
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

PRESETS_FILE = DATA_DIR / "presets.json"
GLOBAL_MESSAGE_FILE = DATA_DIR / "global_message.json"
BLACKLISTED_SERVERS_FILE = DATA_DIR / "blacklisted_servers.json"
BLACKLISTED_USERS_FILE = DATA_DIR / "blacklisted_users.json"


def _load_json(filepath: Path, default: Any) -> Any:
    if filepath.exists():
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load {filepath}: {e}")
    return default


def _save_json(filepath: Path, data: Any):
    tmp_path = filepath.with_suffix(".tmp")
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        tmp_path.replace(filepath)
    except OSError as e:
        logger.error(f"Failed to save {filepath}: {e}")


async def init_db():
    """Initialize JSON data files if they don't exist."""
    for filepath, default in [
        (PRESETS_FILE, {}),
        (GLOBAL_MESSAGE_FILE, {}),
        (BLACKLISTED_SERVERS_FILE, {}),
        (BLACKLISTED_USERS_FILE, {}),
    ]:
        if not filepath.exists():
            _save_json(filepath, default)
    logger.info("JSON database initialized")


# User Presets
async def get_user_presets(user_id: str) -> list[dict]:
    def _get():
        data = _load_json(PRESETS_FILE, {})
        return data.get(user_id, [])
    return await asyncio.to_thread(_get)


async def get_preset_by_title(user_id: str, title: str) -> str | None:
    def _get():
        data = _load_json(PRESETS_FILE, {})
        presets = data.get(user_id, [])
        for p in presets:
            if p.get("title") == title:
                return p.get("content")
        return None
    return await asyncio.to_thread(_get)


async def save_user_preset(user_id: str, title: str, content: str):
    def _save():
        data = _load_json(PRESETS_FILE, {})
        presets = data.get(user_id, [])
        
        found = False
        for p in presets:
            if p.get("title") == title:
                p["content"] = content
                found = True
                break
        if not found:
            presets.append({"title": title, "content": content, "uses": 0})
        
        data[user_id] = presets
        _save_json(PRESETS_FILE, data)
    await asyncio.to_thread(_save)


async def delete_user_preset(user_id: str, title: str):
    def _delete():
        data = _load_json(PRESETS_FILE, {})
        presets = data.get(user_id, [])
        presets = [p for p in presets if p.get("title") != title]
        data[user_id] = presets
        if not presets:
            data.pop(user_id, None)
        _save_json(PRESETS_FILE, data)
    await asyncio.to_thread(_delete)


# Global Default Message
async def get_global_default_message() -> str | None:
    def _get():
        data = _load_json(GLOBAL_MESSAGE_FILE, {})
        return data.get("message")
    return await asyncio.to_thread(_get)


async def set_global_default_message(message: str):
    def _set():
        _save_json(GLOBAL_MESSAGE_FILE, {"message": message})
    await asyncio.to_thread(_set)


# Blacklisted Servers
async def is_server_blacklisted(guild_id: str) -> bool:
    def _get():
        data = _load_json(BLACKLISTED_SERVERS_FILE, {})
        return guild_id in data
    return await asyncio.to_thread(_get)


async def set_server_blacklist(guild_id: str, state: bool):
    def _set():
        data = _load_json(BLACKLISTED_SERVERS_FILE, {})
        if state:
            data[guild_id] = True
        else:
            data.pop(guild_id, None)
        _save_json(BLACKLISTED_SERVERS_FILE, data)
    await asyncio.to_thread(_set)


# Blacklisted Users
async def is_user_blacklisted(user_id: str) -> bool:
    def _get():
        data = _load_json(BLACKLISTED_USERS_FILE, {})
        return user_id in data
    return await asyncio.to_thread(_get)


async def set_user_blacklist(user_id: str, state: bool):
    def _set():
        data = _load_json(BLACKLISTED_USERS_FILE, {})
        if state:
            data[user_id] = True
        else:
            data.pop(user_id, None)
        _save_json(BLACKLISTED_USERS_FILE, data)
    await asyncio.to_thread(_set)