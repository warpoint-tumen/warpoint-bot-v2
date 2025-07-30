# WarPoint Telegram Bot 🤖

Автономный Telegram-бот для проекта WarPoint, созданный для:
- ежедневных напоминаний о задачах
- сбора статусов
- отправки отчётов

## 🚀 Как запустить на Render

1. Развёртывание через GitHub (репозиторий `warpoint-bot-v2`)
2. Используем Python 3.10+
3. Команда запуска:

```bash
python warpoint_bot.py
```

## 📦 Зависимости

Все указаны в `requirements.txt`. Render установит автоматически:

- python-telegram-bot==20.7
- apscheduler==3.10.4

## 🔐 Токен

Не забудьте указать актуальный Telegram Bot Token в `warpoint_bot.py`:

```python
TOKEN = "8318731976:AAGRLByy52ordZtigWkkQ-Ux2Hf7x7AiLIE"
```

