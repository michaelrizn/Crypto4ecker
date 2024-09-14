import os
import sqlite3
import requests
from datetime import datetime
import numpy as np  # Для расчета волатильности
from data.database import connect_db
from bot.config import COINS_PAIRS  # Импортируем криптовалютные пары из config.py
from dotenv import load_dotenv

# Загружаем ключи Binance из .env
load_dotenv()
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET = os.getenv("BINANCE_SECRET")

# Путь к базе данных
DB_PATH = os.path.join(os.path.dirname(__file__), '../data/crypto_bot.db')


def fetch_market_data_binance(symbol, interval='1d', limit=30):
    """
    Получает исторические данные за несколько дней для криптовалюты с использованием Binance API.
    """
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    headers = {
        'X-MBX-APIKEY': BINANCE_API_KEY
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Возвращает список данных
    else:
        print(f"Error fetching data from Binance API for {symbol}: {response.status_code}")
        return None


def calculate_volatility(price_list):
    """
    Рассчитывает волатильность на основе исторических данных о ценах.
    """
    prices = [float(p[4]) for p in price_list]  # Берем закрывающие цены
    if len(prices) > 1:
        return np.std(prices)  # Стандартное отклонение (волатильность)
    else:
        return None


def insert_market_data(data_binance, symbol):
    """
    Вставляет рыночные данные в таблицу market_data.
    """
    with connect_db() as conn:
        cursor = conn.cursor()
        # Вставляем последнюю запись из данных за несколько дней
        last_data = data_binance[-1]  # Последняя запись в массиве данных (содержит последние цены)

        # Рассчитываем волатильность
        volatility = calculate_volatility(data_binance)

        cursor.execute('''
            INSERT INTO market_data (timestamp, coin_id, price, volume_24h, volatility)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            datetime.now(),  # Текущее время
            symbol,  # Символ криптовалютной пары
            float(last_data[4]),  # Закрывающая цена за последний день
            float(last_data[5]),  # Объем торгов за последний день
            volatility  # Волатильность, рассчитанная на основе исторических данных
        ))
        conn.commit()


def update_market_data():
    """
    Получает и записывает данные по криптовалютным парам за несколько дней.
    """
    for pair in COINS_PAIRS:
        symbol = pair.replace("/", "")  # Пример: BTC/USDT -> BTCUSDT

        # Получаем данные с Binance за последние несколько дней
        market_data_binance = fetch_market_data_binance(symbol, interval='1d', limit=30)

        if market_data_binance:
            insert_market_data(market_data_binance, symbol)
            print(f"Данные по {symbol} успешно обновлены.")
        else:
            print(f"Не удалось получить данные по {symbol}.")


if __name__ == "__main__":
    update_market_data()