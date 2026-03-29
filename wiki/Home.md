# Wicked Yoda's Little Helper Wiki

Last Updated: 2026-03-28

This folder contains internal project wiki docs for bot operations, command behavior, feed automation, and web admin usage.

Current feature areas include moderation commands, fun/community slash commands, feed automation, uptime monitoring, repo-backed Spicy Prompts content refresh, guild-scoped member activity reporting, and the multi-guild web admin portal with role-based access.

## Pages

- [Command Reference](./Command-Reference.md) - active slash commands, parameters, and permission behavior.
- [Feed Integrations](./Feed-Integrations.md) - Reddit, WordPress, YouTube, and LinkedIn automation configured from the web GUI.
- [Multi-Guild and Env Setup](./Multi-Guild-and-Env.md) - required/optional env vars and multi-guild startup patterns.
- [Web Admin Interface](./Web-Admin-Interface.md) - web GUI auth, pages, security controls, and operational notes.
- [Security Hardening](./Security-Hardening.md) - implemented runtime, auth, storage, and verification controls.

## Web Admin Routes

- Public health and status:
  - `/healthz`
  - `/status`
  - `/status/everything`
- Login/session:
  - `/login`
  - `/logout`
- Login required:
  - `/admin`
  - `/admin/home`
  - `/admin/overview`
  - `/admin/guilds`
  - `/admin/guild-settings`
  - `/admin/random-user`
  - `/admin/status`
  - `/admin/uptime-monitors`
  - `/admin/actions`
  - `/admin/member-activity`
  - `/admin/reddit`
  - `/admin/wordpress`
  - `/admin/linkedin`
  - `/admin/youtube`
  - `/admin/spicy-prompts`
  - `/admin/command-permissions`
  - `/admin/tag-responses`
  - `/admin/documentation`
  - `/admin/documentation/<page>`
  - `/admin/logs`
  - `/admin/logs/download`
  - `/admin/wiki`
  - `/admin/account`
- Admin-write pages and actions:
  - `/admin/users`
  - `/admin/guild-access`
  - `/admin/command-permissions`
  - `/admin/tag-responses`
  - `/admin/guild-settings`
  - `/admin/settings`
  - `/admin/observability`
  - `/admin/bot-profile`
- Admin write actions:
  - `/admin/users/add`
  - `/admin/users/update`
  - `/admin/users/delete`
  - `/admin/settings/save`
  - `/admin/restart` (only when `WEB_RESTART_ENABLED=true`)

## Maintenance Rule

Whenever a command is added, removed, or changed in `bot.py`:

1. Update [Command Reference](./Command-Reference.md) in the same commit/PR.
2. Verify command options, permission checks, and responses match code.
3. Keep the "Last Updated" date current.

Whenever a web-managed automation or admin capability is added or changed:

1. Update [Feed Integrations](./Feed-Integrations.md) if the change affects background notifications.
2. Update [Web Admin Interface](./Web-Admin-Interface.md) if the change affects the GUI, auth, or account management.
3. Update [Multi-Guild and Env Setup](./Multi-Guild-and-Env.md) if new env vars or guild-scoped behaviors are introduced.
4. Update the shipped examples (`env.env`, `docker-compose.yml`) when container paths or runtime storage defaults change.

Whenever activity reporting or analytics views change:

1. Update [Command Reference](./Command-Reference.md) if `/stats` behavior changes.
2. Update [Web Admin Interface](./Web-Admin-Interface.md) if `/admin/member-activity` layout, export, or permissions change.

## Source Of Truth

- Runtime behavior: `bot.py`
- Human documentation: this wiki folder


Recent updates include log retention controls, dashboard status cards for Spicy Prompts, command status visibility on the dashboard, and Spicy Prompts random category rotation with 4-hour repeat protection.
Additional updates include Guild Admin access groups, uptime monitors (HTTP/TCP/status pages), random user picker with 30-day exclusion window, and dashboard category listings for all web admin pages.
