import unittest
from data.database import execute_query, fetch_query
from data.db_initializer import initialize_db

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Инициализируем базу данных и создаём таблицы перед тестами
        initialize_db()

    def test_insert_and_fetch_market_data(self):
        # Добавляем данные в таблицу market_data
        execute_query(
            "INSERT INTO market_data (coin_id, price, volume_24h, market_cap) VALUES (?, ?, ?, ?)",
            ("BTC", 50000, 1000000, 900000000)
        )

        # Проверяем, что данные были добавлены корректно
        results = fetch_query("SELECT coin_id, price FROM market_data WHERE coin_id=?", ("BTC",))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], "BTC")
        self.assertEqual(results[0][1], 50000)

if __name__ == '__main__':
    unittest.main()