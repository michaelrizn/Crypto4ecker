import unittest
from data.models import MarketData, TechnicalIndicator
from datetime import datetime

class TestModels(unittest.TestCase):
    def test_market_data_model(self):
        # Создаём объект MarketData
        market_data = MarketData(
            coin_id="BTC",
            circulating_supply=18500000,
            total_supply=21000000,
            price=60000,
            volume_24h=1500000,
            market_cap=1100000000000,
            volatility=0.05
        )

        # Проверяем, что атрибуты объекта корректны
        self.assertEqual(market_data.coin_id, "BTC")
        self.assertEqual(market_data.price, 60000)
        self.assertEqual(market_data.volatility, 0.05)

    def test_technical_indicator_model(self):
        # Создаём объект TechnicalIndicator
        tech_ind = TechnicalIndicator(
            coin_id="ETH",
            macd_value=1.2,
            rsi_value=55.0,
            bollinger_upper=3000,
            bollinger_lower=2800
        )

        # Проверяем атрибуты
        self.assertEqual(tech_ind.coin_id, "ETH")
        self.assertEqual(tech_ind.rsi_value, 55.0)
        self.assertEqual(tech_ind.bollinger_upper, 3000)
        self.assertEqual(tech_ind.bollinger_lower, 2800)

if __name__ == '__main__':
    unittest.main()