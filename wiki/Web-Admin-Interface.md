# Web Admin Interface

Last Updated: 2026-03-17

The web admin is served by `web_admin.py` and is mobile-friendly.

## Authentication and Session

- Login with `WEB_ADMIN_DEFAULT_USERNAME` / `WEB_ADMIN_DEFAULT_PASSWORD`.
- Optional "Keep me signed in" uses 5-day remember mode.
- Inactivity timeout uses `WEB_SESSION_TIMEOUT_MINUTES`.
- Login attempts are rate-limited per IP.
- Password rotation is enforced every 90 days.
- Existing users can update their own email, name, and password in `My Account`.
- Admins can manage other web users.
- Read-only users can view the full portal but cannot submit changes.

## Security Controls

- CSRF enforcement: `WEB_ENFORCE_CSRF` (default `true`)
- Same-origin POST enforcement: `WEB_ENFORCE_SAME_ORIGIN_POSTS` (default `true`)
- Security headers are applied on responses (CSP, frame deny, no-store, etc.).
- Web audit logs are written to `web_gui_audit.log`.
- Avatar upload requests are bounded by request-size and per-file-size limits.
- SQLite storage uses WAL mode and foreign key enforcement.

## Navigation and Themes

- Light/Black theme switch in top nav (saved in browser storage).
- "Go to page..." quick selector in nav.
- Guild selector at top controls the active guild context for guild-scoped pages.

## Key Pages

- Dashboard: `/admin`
- Actions: `/admin/actions`
- YouTube subscriptions: `/admin/youtube`
- Logs: `/admin/logs`
- Wiki viewer: `/admin/wiki`
- Account management: `/admin/account`
- Users: `/admin/users` (login required, admin writes only)
- Command permissions: `/admin/command-permissions` (login required, admin writes only)
- Tag responses: `/admin/tag-responses` (login required, admin writes only)
- Guild settings: `/admin/guild-settings` (login required, admin writes only)
- Runtime settings editor: `/admin/settings` (login required, admin writes only)
- Observability: `/admin/observability` (login required)
- Bot profile: `/admin/bot-profile` (login required, admin writes only)
  - Update bot username
  - Update or clear guild nickname
  - Upload bot avatar (`WEB_AVATAR_MAX_UPLOAD_BYTES`)

## Public Status

- `/status` redirects to `/status/everything`
- `/status/everything` shows public status/health summary without login.

## Restart Control

- `/admin/restart` is only useful when `WEB_RESTART_ENABLED=true`.
- Intended for containerized environments where process exit triggers container restart.
