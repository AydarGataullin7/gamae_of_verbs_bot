# Игра глаголов — боты для Telegram и ВКонтакте

Боты для онлайн-издательства "Игра глаголов". Отвечают на типовые вопросы через DialogFlow, сложные перенаправляют операторам.

## Как запустить

1. Установи зависимости:
    ```bash
    pip install -r requirements.txt
    ```
    Создай файлы `.env` в папках `code_for_tg` и `code_for_vk`:

Для Telegram:

```text
TG_BOT_TOKEN=ваш_токен
PROJECT_ID=games-of-verbs-bot
GOOGLE_APPLICATION_CREDENTIALS=путь_к_json
```

Для VK:

```text
VK_TOKEN=ваш_токен
PROJECT_ID=games-of-verbs-bot
GOOGLE_APPLICATION_CREDENTIALS=путь_к_json
```

2. Запуск бота:

```bash
## Telegram
cd code_for_tg
python bot.py
```

```bash
## VK
cd code_for_vk
python vk_bot.py
```

## Структура

`code_for_tg/` — Telegram-бот

`code_for_vk/` — VK-бот

`games-of-verbs-bot-*.json` — ключ для Google Cloud
