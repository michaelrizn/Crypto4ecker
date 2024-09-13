import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Настройки API
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
COINGECKO_API_URL = os.getenv("COINGECKO_API_URL")
COINLORE_API_URL = os.getenv("COINLORE_API_URL")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WORLD_BANK_API_URL = os.getenv("WORLD_BANK_API_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")