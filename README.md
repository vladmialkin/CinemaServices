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