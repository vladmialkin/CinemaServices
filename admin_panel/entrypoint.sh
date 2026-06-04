#!/usr/bin/env bash
set -e

cd /app/admin_panel/src

POSTGRES_HOST="${POSTGRES_HOST:-postgres}"
POSTGRES_PORT="${POSTGRES_PORT:-5432}"

echo "Waiting for Postgres at ${POSTGRES_HOST}:${POSTGRES_PORT}..."
until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done
echo "Postgres is up."

echo "Applying migrations..."
python manage.py migrate --noinput

if [ "${DJANGO_COLLECTSTATIC:-0}" = "1" ]; then
  echo "Collecting static..."
  python manage.py collectstatic --noinput
fi

echo "Starting Django dev server..."
exec python manage.py runserver 0.0.0.0:${DJANGO_PORT:-8000}