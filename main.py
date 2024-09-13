import os
from bot.bot import start_bot
from services.scheduler import start_scheduler
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

def main():
    # Запуск планировщика задач для получения данных с API
    start_scheduler()

    # Запуск Telegram бота
    start_bot()

if __name__ == "__main__":
    main()