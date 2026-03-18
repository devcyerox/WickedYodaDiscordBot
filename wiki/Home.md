# WickedYoda's Little Helper Wiki

Last Updated: 2026-03-18

This folder contains internal project wiki docs for bot operations, command behavior, feed automation, and web admin usage.

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
  - `/admin/guilds`
  - `/admin/status`
  - `/admin/actions`
  - `/admin/reddit`
  - `/admin/wordpress`
  - `/admin/linkedin`
  - `/admin/youtube`
  - `/admin/documentation`
  - `/admin/logs`
  - `/admin/wiki`
  - `/admin/account`
- Admin-write pages and actions:
  - `/admin/users`
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

## Source Of Truth

- Runtime behavior: `bot.py`
- Human documentation: this wiki folder
