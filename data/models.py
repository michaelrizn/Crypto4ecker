from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MarketData(Base):
    __tablename__ = 'market_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    coin_id = Column(String, nullable=False)
    price = Column(Float, nullable=True)
    volume_24h = Column(Float, nullable=True)
    volatility = Column(Float, nullable=True)

    def __repr__(self):
        return f"<MarketData(coin_id={self.coin_id}, price={self.price}, volume_24h={self.volume_24h})>"