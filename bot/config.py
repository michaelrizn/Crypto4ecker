import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Настройки API
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET = os.getenv("BINANCE_SECRET")

# Путь к базе данных
DATABASE_PATH = './data/crypto_bot.db'

# Логирование
LOGGING_LEVEL = 'INFO'

# Топ криптовалютные пары к USDT
COINS_PAIRS = [
    "BTC/USDT", "ETH/USDT", "BNB/USDT", "XRP/USDT", "ADA/USDT",
    "SOL/USDT", "DOT/USDT", "DOGE/USDT", "SHIB/USDT", "LTC/USDT",
    "AVAX/USDT", "LINK/USDT", "UNI/USDT", "ATOM/USDT", "TRX/USDT",
    "XLM/USDT", "BCH/USDT", "ALGO/USDT", "VET/USDT", "AXS/USDT",
    "TON/USDT"
]