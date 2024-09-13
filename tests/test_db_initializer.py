import unittest
import os
from data.db_initializer import initialize_db
from data.database import DB_PATH, connect_db

class TestDBInitializer(unittest.TestCase):
    def setUp(self):
        # Удаляем файл базы данных в папке data, если он существует, перед каждым тестом
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)

    def test_initialize_db(self):
        # Проверяем создание базы данных и таблиц
        initialize_db()

        # Отладочный вывод для проверки пути к БД
        print(f"База данных проверяется по пути: {DB_PATH}")

        # Проверяем, что таблица market_data создана
        with connect_db() as conn:
            cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='market_data';")
            result = cursor.fetchone()
            self.assertIsNotNone(result, "Таблица market_data не была создана")

            cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='macro_factors';")
            result = cursor.fetchone()
            self.assertIsNotNone(result, "Таблица macro_factors не была создана")

if __name__ == '__main__':
    unittest.main()