from dataclasses import dataclass
from datetime import datetime

# Модель для рыночных данных
@dataclass
class MarketData:
    coin_id: str
    circulating_supply: float
    total_supply: float
    price: float
    volume_24h: float
    market_cap: float
    volatility: float
    timestamp: datetime = datetime.now()

# Модель для технических индикаторов
@dataclass
class TechnicalIndicator:
    coin_id: str
    macd_value: float
    rsi_value: float
    bollinger_upper: float
    bollinger_lower: float
    timestamp: datetime = datetime.now()