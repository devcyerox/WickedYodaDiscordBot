import sqlite3
from pathlib import Path

from web_admin import create_app


def _bot_snapshot() -> dict:
    return {
        "bot_name": "Test Bot",
        "guild_id": 1234567890,
        "latency_ms": 42,
        "commands_synced": 6,
        "started_at": "2026-01-01T00:00:00+00:00",
    }


def test_healthz_route(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("WEB_ADMIN_DEFAULT_USERNAME", "admin@example.com")
    monkeypatch.setenv("WEB_ADMIN_DEFAULT_PASSWORD", "TestPass123!")
    app = create_app(str(tmp_path / "actions.db"), _bot_snapshot)
    client = app.test_client()

    response = client.get("/healthz")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["status"] == "ok"
    assert "timestamp" in payload


def test_admin_redirects_to_login_when_not_authenticated(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("WEB_ADMIN_DEFAULT_USERNAME", "admin@example.com")
    monkeypatch.setenv("WEB_ADMIN_DEFAULT_PASSWORD", "TestPass123!")
    app = create_app(str(tmp_path / "actions.db"), _bot_snapshot)
    client = app.test_client()

    response = client.get("/admin", follow_redirects=False)

    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_login_and_dashboard_access(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("WEB_ADMIN_DEFAULT_USERNAME", "admin@example.com")
    monkeypatch.setenv("WEB_ADMIN_DEFAULT_PASSWORD", "TestPass123!")
    app = create_app(str(tmp_path / "actions.db"), _bot_snapshot)
    client = app.test_client()

    response = client.post(
        "/login",
        data={"username": "admin@example.com", "password": "TestPass123!"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Latest Actions" in response.data


def test_actions_list_renders_existing_records(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("WEB_ADMIN_DEFAULT_USERNAME", "admin@example.com")
    monkeypatch.setenv("WEB_ADMIN_DEFAULT_PASSWORD", "TestPass123!")
    db_path = tmp_path / "actions.db"

    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS actions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                action TEXT NOT NULL,
                status TEXT NOT NULL,
                moderator TEXT,
                target TEXT,
                reason TEXT,
                guild TEXT
            )
            """
        )
        conn.execute(
            """
            INSERT INTO actions (created_at, action, status, moderator, target, reason, guild)
            VALUES ('2026-01-01 00:00:00', 'kick', 'success', 'mod', 'user', 'reason', 'guild')
            """
        )
        conn.commit()

    app = create_app(str(db_path), _bot_snapshot)
    client = app.test_client()
    client.post("/login", data={"username": "admin@example.com", "password": "TestPass123!"}, follow_redirects=True)

    response = client.get("/admin/actions")

    assert response.status_code == 200
    assert b"kick" in response.data
