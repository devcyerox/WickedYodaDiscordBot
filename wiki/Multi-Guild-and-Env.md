# Multi-Guild and Env Setup

Last Updated: 2026-03-19

## Required vs Optional Vars

- Required:
  - `DISCORD_TOKEN`
- Optional:
  - `MANAGED_GUILD_IDS`
  - `GUILD_ID`
  - `Bot_Log_Channel`
  - Web/admin integration vars (`WEB_*`)
  - Storage vars (`DATA_DIR`, `ACTION_DB_PATH`, `LOG_DIR`)
  - Feed integration timeouts (`YOUTUBE_REQUEST_TIMEOUT_SECONDS`, `WORDPRESS_REQUEST_TIMEOUT_SECONDS`, `LINKEDIN_REQUEST_TIMEOUT_SECONDS`)

## Storage Paths

- In the shipped Docker Compose example, `DATA_DIR` in `env.env` is the host-side bind path for persistent data.
- In the shipped Docker Compose example, `LOG_DIR` in `env.env` is the host-side bind path for persistent logs.
- `docker-compose.yml` overrides the bot's in-container `DATA_DIR` to `/app/data` and `LOG_DIR` to `/app/log`.
- `ACTION_DB_PATH` defaults to the in-container `DATA_DIR/mod_actions.db` when unset.
- `LOG_DIR` defaults under the in-container `DATA_DIR` when unset or invalid, but the shipped Compose example pins it to `/app/log`.
- The shipped `docker-compose.yml` example bind-mounts `${DATA_DIR:-/root/docker/wickedyodabot}` to `/app/data`.
- The shipped `docker-compose.yml` example bind-mounts `${LOG_DIR:-/root/docker/wickedyodabot/log}` to `/app/log`.
- Start Compose with `docker compose --env-file env.env up -d` so the bind path comes from `env.env`.

## How Guild Selection Works

- `MANAGED_GUILD_IDS` set:
  - Bot only manages/syncs commands to those guild IDs.
  - Recommended for production control.
- `MANAGED_GUILD_IDS` not set:
  - Bot manages all guilds it is currently in.
- `GUILD_ID` set:
  - Used as legacy/default fallback for some seed settings.
- `GUILD_ID` not set:
  - Bot still starts in multi-guild mode.

## Logging Channel Behavior

- Primary mode is per-guild log channel from `/admin/guild-settings`.
- Fallback mode uses global `Bot_Log_Channel` if set.
- If neither is configured, Discord log-channel posting is skipped, but file/SQLite logging still runs.

## Guild-Scoped Feed Automation

Feed subscriptions are configured per guild from the web GUI. The selected guild in the top nav controls which server you are editing for:

- Reddit feeds
- WordPress feeds
- LinkedIn feeds
- YouTube feeds

Feed source URLs, selected notify channels, and last-seen state do not cross between guilds.

## Recommended Multi-Guild Example

```env
DISCORD_TOKEN=your-token
MANAGED_GUILD_IDS=111111111111111111,222222222222222222
WEB_ENABLED=true
WEB_BIND_HOST=0.0.0.0
WEB_PORT=8080
WEB_TLS_ENABLED=true
WEB_TLS_PORT=8081
DATA_DIR=/root/docker/wickedyodabot
LOG_DIR=/root/docker/wickedyodabot/log
```

## Single-Guild Legacy Example

```env
DISCORD_TOKEN=your-token
GUILD_ID=111111111111111111
Bot_Log_Channel=333333333333333333
WEB_ENABLED=true
WEB_PORT=8080
WEB_TLS_ENABLED=true
WEB_TLS_PORT=8081
DATA_DIR=/root/docker/wickedyodabot
LOG_DIR=/root/docker/wickedyodabot/log
```
