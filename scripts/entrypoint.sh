#!/bin/sh
set -e

mkdir -p /app/data /app/logs
chown -R botuser:botuser /app/data /app/logs || true

exec gosu botuser python /app/bot.py
