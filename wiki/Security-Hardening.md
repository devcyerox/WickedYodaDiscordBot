# Security Hardening

Last Updated: 2026-03-17

This document tracks the active security controls implemented in the bot and web admin.

## Web Admin Controls

- No public self-signup route
- Admin-controlled user provisioning
- Two web roles:
  - `Admin`: full read/write access
  - `Read-only`: can view the full portal but cannot make changes
- Admin self-demotion protection
- Account self-service for:
  - display name
  - email
  - password
- Password policy:
  - minimum 12 characters
  - at least one lowercase letter
  - at least one uppercase letter
  - at least one number
- Forced password rotation every 90 days
- Login attempt throttling per client IP
- CSRF validation for state-changing requests
- Same-origin enforcement with CSRF-aware proxy compatibility
- Session cookie protections:
  - `HttpOnly`
  - `SameSite`
  - optional `Secure`
- Security headers:
  - CSP
  - `X-Frame-Options: DENY`
  - `X-Content-Type-Options: nosniff`
  - `Referrer-Policy: no-referrer`
  - no-store cache controls

## Persistence Controls

- SQLite connections use:
  - WAL mode
  - foreign key enforcement
  - busy timeout
- Best-effort restrictive filesystem permissions:
  - data directories target `0700`
  - env/db/log files target `0600`
- Avatar uploads are bounded by request size and explicit file-size checks

## Bot Runtime Controls

- Discord privileged intents default to least privilege
- Moderation commands require Discord permission checks
- Command-permission overrides support:
  - default policy
  - public access
  - custom role restrictions
- Guild-scoped settings isolate data between servers
- Bot log channel validation checks:
  - guild ownership
  - text-channel compatibility
  - send/embed permissions

## Local Verification

Recommended local checks before merge:

1. `ruff format --check .`
2. `ruff check .`
3. `pytest -q`
4. `bandit -q -c pyproject.toml -r .`
5. `pip-audit -r requirements.txt`

## Notes

- If `WEB_ADMIN_DEFAULT_PASSWORD` is used instead of a precomputed hash, it must satisfy the password policy.
- Existing password hashes are upgraded to the current Werkzeug default format after successful login when needed.
