from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

TOKEN = "8318731976:AAGRLByy52ordZtigWkkQ-Ux2Hf7x7AiLIE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    today = datetime.now().strftime("%d.%m.%Y")
    msg = f"Задачи на сегодня ({today}):"
    await update.message.reply_text(msg)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен... (заргужка)")
    app.run_polling()

if __name__ == "__main__":
    main()
