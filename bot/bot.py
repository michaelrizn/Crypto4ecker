from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Команда /start, отправляем приветствие пользователю
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Привет! Я бот для анализа криптовалют. Используй команду /predict для получения прогноза.")

# Команда /predict для предсказания цены
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Пример: получение данных для предсказания (в будущем здесь можно добавить вызов модели предсказания)
    await update.message.reply_text(f"Предсказание цены криптовалюты скоро будет доступно!")

def start_bot():
    # Получаем ключ API из переменных окружения
    telegram_api_key = os.getenv("TELEGRAM_API_KEY")

    # Создаем приложение бота
    application = ApplicationBuilder().token(telegram_api_key).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("predict", predict))

    # Запуск бота
    application.run_polling()