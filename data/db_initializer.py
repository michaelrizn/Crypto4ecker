from data.database import connect_db

def create_tables():
    with connect_db() as conn:
        # Создание таблицы market_data
        conn.execute('''
            CREATE TABLE IF NOT EXISTS market_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                coin_id TEXT NOT NULL,
                circulating_supply REAL,
                total_supply REAL,
                price REAL,
                volume_24h REAL,
                market_cap REAL,
                volatility REAL
            );
        ''')

        # Создание таблицы macro_factors
        conn.execute('''
            CREATE TABLE IF NOT EXISTS macro_factors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                country TEXT NOT NULL,
                inflation_rate REAL,
                economic_uncertainty TEXT
            );
        ''')

        # Создание таблицы social_media
        conn.execute('''
            CREATE TABLE IF NOT EXISTS social_media (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                coin_id TEXT NOT NULL,
                twitter_mentions INTEGER,
                reddit_posts INTEGER,
                news_sentiment TEXT
            );
        ''')

        # Создание таблицы liquidity_data
        conn.execute('''
            CREATE TABLE IF NOT EXISTS liquidity_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                exchange_id TEXT NOT NULL,
                coin_id TEXT NOT NULL,
                trading_volume_24h REAL
            );
        ''')

        # Создание таблицы news_data
        conn.execute('''
            CREATE TABLE IF NOT EXISTS news_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source TEXT NOT NULL,
                title TEXT,
                content TEXT,
                sentiment TEXT
            );
        ''')

        # Создание таблицы defi_data
        conn.execute('''
            CREATE TABLE IF NOT EXISTS defi_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                project_id TEXT NOT NULL,
                tvl REAL
            );
        ''')

        # Создание таблицы price_predictions
        conn.execute('''
            CREATE TABLE IF NOT EXISTS price_predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                coin_id TEXT NOT NULL,
                predicted_price REAL,
                confidence REAL
            );
        ''')

        # Создание таблицы exchanges
        conn.execute('''
            CREATE TABLE IF NOT EXISTS exchanges (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                country TEXT
            );
        ''')

        # Создание таблицы technical_indicators
        conn.execute('''
            CREATE TABLE IF NOT EXISTS technical_indicators (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                coin_id TEXT NOT NULL,
                macd_value REAL,
                rsi_value REAL,
                bollinger_upper REAL,
                bollinger_lower REAL,
                ema_short REAL,
                ema_long REAL,
                stochastic_k REAL,
                stochastic_d REAL,
                atr_value REAL,
                parabolic_sar REAL,
                cci_value REAL,
                fibonacci_level REAL,
                ichimoku_cloud REAL
            );
        ''')

    print("Все таблицы проверены и созданы при необходимости.")

def initialize_db():
    create_tables()
    print("Инициализация базы данных завершена.")