# Кофейня «Перемена»

Сайт кофейни из двух приложений:

- `vitrina` — витрина на Flask: меню напитков и карточки с описанием;
- `kalkulyator` — калькулятор заказа на FastAPI.

## Адреса приложений

Адреса открываются в сети кабинета (сервер `192.168.1.11`):

- Витрина: http://192.168.1.11:20430/
- Калькулятор заказа: http://192.168.1.11:20431/
- Документация API калькулятора: http://192.168.1.11:20431/docs

## Пример заказа

Два капучино с овсяным молоком: (180 + 30) × 2 = **420 ₽**.

## Запуск через Docker Compose

1. Подключитесь к серверу и создайте каталог проекта:
   `ssh student@192.168.1.11`, затем `newproject voinov-web-cafe`.
2. Загрузите код:
   ```bash
   cd ~/projects/voinov-web-cafe
   git init -q
   git remote add origin https://github.com/blassterxd/web_cafe.git
   git pull origin HEAD
   ```
3. В файле `.env` проверьте порты и адрес привязки:
   ```dotenv
   PORT1=20430
   PORT2=20431
   BIND_IP=0.0.0.0
   ```
4. Запустите: `docker compose up -d --build`, затем проверьте `docker compose ps`.

Обновление после изменений: `git pull origin HEAD`, затем `docker compose up -d --build`.

## Структура

```text
web_cafe/
├── compose.yaml
├── vitrina/      # Flask: app.py, templates/, static/
└── kalkulyator/  # FastAPI: main.py, index.html
```
