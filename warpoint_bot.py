from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import logging

# Включаем логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

TOKEN = "8318731976:AAGRLByy52ordZtigWkkQ-Ux2Hf7x7AiLIE"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот запущен. Добро пожаловать!")

# Команда /today
async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%d.%m.%Y")
    msg = f"Задачи на сегодня ({now}):\n- пример задачи 1\n- пример задача 2"
    await update.message.reply_text(msg)

# Основной запуск
def main():
    app = ApplicationBuilder().token("8318731976:AAGRLByy52ordZtigWkkQ-Ux2Hf7x7AiLIE").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("today", today))
    app.run_polling()

if __name__ == "__main__":
    main()
