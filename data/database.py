import sqlite3
import os
from contextlib import closing

# Указываем путь к базе данных в папке data
DB_PATH = os.path.join(os.path.dirname(__file__), 'crypto_bot.db')

# Подключение к базе данных
def connect_db():
    return sqlite3.connect(DB_PATH)

# Функция для выполнения запросов
def execute_query(query, params=()):
    with closing(connect_db()) as conn:
        with conn:
            conn.execute(query, params)

# Функция для получения данных
def fetch_query(query, params=()):
    with closing(connect_db()) as conn:
        cursor = conn.execute(query, params)
        return cursor.fetchall()