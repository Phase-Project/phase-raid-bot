<p align="center">
  <img src="https://raw.githubusercontent.com/phaseworld-creator/phase-raid-bot/refs/heads/main/assets/phase.png?s=512" alt="Phase Raid Bot" width="200" height="200">
</p>

<h1 align="center">Phase Raid Bot</h1>

<p align="center">A powerful Discord bot built with discord.py for raiding, spamming, and destorying servers.</p>

---

## Features

- **Raid** — Launch mass spam raids via interactive button panels
- **Interaction Raid** — Farm interactions automatically with smart clickers
- **Spam / File Spam** — Send custom messages or files on repeat
- **Thug** — Gay porn spamming for fun
- **Fake Nitro** — Deploy fake nitro giveaways and hoaxes
- **Fake Giveaway** — Host counterfeit giveaways
- **Ghost** — Ghost mention and ghost ping tools
- **DM Raid** — Direct message flooding tools
- **Ads** — Automatic advertisement posting
- **Leaderboard** — Track top raiders with JSON file persistence
- **Admin Tools** — Reload cogs, set global messages, blacklist servers/users

---

## Installation

### Prerequisites

- [Python 3.10+](https://www.python.org/)

### Setup

```bash
# Clone the repo
git clone https://github.com/phaseworld-creator/phase-raid-bot
cd phase-raid-bot

# Create a virtual environment (standard venv)
python -m venv .venv

# On Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# On Linux / macOS
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

> **Optional:** If you prefer [uv](https://docs.astral.sh/uv/) for faster installs, you can use `uv venv` and `uv pip install -r requirements.txt` instead.

### Configuration

open config and fill in your values

### Running

```bash
python main.py
```

---

## Tech Stack

- [discord.py](https://discordpy.readthedocs.io/) — Discord API wrapper
- [LMDB](https://lmdb.readthedocs.io/) — High-performance leaderboard storage
- [aiohttp](https://docs.aiohttp.org/) — Async HTTP for API posting

> **uv** (optional) — Fast package & venv management, if you prefer it over standard `venv`/`pip`
