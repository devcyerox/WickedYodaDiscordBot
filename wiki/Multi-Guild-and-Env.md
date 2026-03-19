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

- `DATA_DIR` is the primary writable container path for SQLite, member activity data, feed state, and logs.
- `ACTION_DB_PATH` defaults to `DATA_DIR/mod_actions.db` when unset.
- `LOG_DIR` defaults under `DATA_DIR` when unset or invalid.
- The shipped `docker-compose.yml` example mounts `wickedyoda_data` to `${DATA_DIR:-/app/data}`.
- Docker Compose resolves `${DATA_DIR:-...}` from the shell or `.env`, not from `env.env`, so keep the Compose mount target and `env.env` value aligned.

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
DATA_DIR=/app/data
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
DATA_DIR=/app/data
```
