<p align="center">
  <img src="https://raw.githubusercontent.com/phaseworld-creator/phase-raid-bot/refs/heads/main/assets/phase.png?s=512" alt="Phase Raid Bot" width="200" height="200">
</p>

<h1 align="center">Phase Raid Bot</h1>

<p align="center">A powerful Discord bot built with discord.py for raiding, spamming, and destorying servers.</p>

---

## Features

| command | description |
|:--------|:------------|
| <img src="https://img.shields.io/badge/-Raid-5865F2?style=flat-square"> | Launch mass spam raids via interactive button panels |
| <img src="https://img.shields.io/badge/-Interaction%20Raid-9B59B6?style=flat-square"> | Farm interactions automatically with smart clickers |
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
