# CinemaServices

## Менеджер пакетов

Чтобы добавить пакет через poetry, нужно добавить его в определенную группу:

- auth
- api
- dev
- ugc
- admin_panel

```bash
poetry add <имя пакета> --group auth 
```

Чтобы установить зависимости определенной группы выполните команду:

```bash
poetry install --only auth
```

## AdminPanel

Запустить контейнеры для админ панели

```bash
docker compose -f path/to/admin_panel/compose.yml --env-file path/to/.env up -d --build
```

Удалить контейнеры со всеми volume
```bash
docker compose -f path/to/admin_panel/compose.yml down -v 
```