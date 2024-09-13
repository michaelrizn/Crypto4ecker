import sqlite3
import os
from data.db_initializer import initialize_db  # Импортируем функцию для создания таблиц

# Указываем путь к базе данных в папке data
DB_PATH = os.path.join(os.path.dirname(__file__), '../data/crypto_bot.db')


def delete_all_tables():
    """
    Удаляет все таблицы из базы данных, кроме служебных таблиц SQLite.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Получаем все таблицы, кроме sqlite_sequence (служебная таблица SQLite)
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()

        # Удаляем каждую таблицу, кроме служебных
        for table_name in tables:
            table_name = table_name[0]
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            print(f"Таблица {table_name} удалена.")

        conn.commit()
        print("Все пользовательские таблицы удалены.")


# Запуск для удаления таблиц и их повторного создания
if __name__ == "__main__":
    delete_all_tables()  # Удаляем таблицы
    initialize_db()  # Создаем таблицы заново