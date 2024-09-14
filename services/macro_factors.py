import os
from datetime import datetime
from data.database import connect_db
from fredapi import Fred  # FRED API для получения данных
from dotenv import load_dotenv

# Загружаем ключи из .env
load_dotenv()

# Логинимся в FRED API
fred = Fred(api_key=os.getenv('FRED_API_KEY'))  # API-ключ FRED из .env

# Путь к базе данных
DB_PATH = os.path.join(os.path.dirname(__file__), '../data/crypto_bot.db')

def fetch_inflation_rate(country_code):
    """
    Получает уровень инфляции для указанной страны с использованием FRED API.
    """
    try:
        # Получаем данные для каждой страны на основе кода страны
        if country_code == 'US':
            inflation_series = fred.get_series('CPIAUCSL')  # Индекс потребительских цен для США
        elif country_code == 'CN':
            inflation_series = fred.get_series('CHNCPIALLMINMEI')  # Индекс потребительских цен для Китая
        elif country_code == 'IN':
            inflation_series = fred.get_series('INDCPIALLMINMEI')  # Индекс потребительских цен для Индии
        elif country_code == 'BR':
            inflation_series = fred.get_series('BRACPIALLMINMEI')  # Индекс потребительских цен для Бразилии
        elif country_code == 'KR':
            inflation_series = fred.get_series('KORCPIALLMINMEI')  # Индекс потребительских цен для Южной Кореи
        elif country_code == 'JP':
            inflation_series = fred.get_series('JPNCPIALLMINMEI')  # Индекс потребительских цен для Японии
        elif country_code == 'VN':
            inflation_series = fred.get_series('VNCPIALLMINMEI')  # Индекс потребительских цен для Вьетнама
        elif country_code == 'NG':
            inflation_series = fred.get_series('NGACPIALLMINMEI')  # Индекс потребительских цен для Нигерии
        elif country_code == 'DE':
            inflation_series = fred.get_series('DEUCPIALLMINMEI')  # Индекс потребительских цен для Германии
        elif country_code == 'SG':
            inflation_series = fred.get_series('SGPCPIALLMINMEI')  # Индекс потребительских цен для Сингапура
        else:
            inflation_series = None  # Если страна не поддерживается

        if inflation_series is not None:
            inflation_rate = inflation_series[-1]  # Берём последнее значение
            return inflation_rate
        return None
    except Exception as e:
        print(f"Error fetching inflation data from FRED for {country_code}: {e}")
        return None

def fetch_economic_uncertainty(country):
    """
    Получает данные об экономической неопределенности для указанной страны.
    В данном случае данные могут быть взяты из анализа новостей или отчетов, пока временно возвращаем None.
    """
    return "Moderate uncertainty"  # Пример значения, можно заменить на данные с внешнего источника

def insert_macro_factors(country, inflation_rate, economic_uncertainty):
    """
    Вставляет макроэкономические данные в таблицу macro_factors.
    """
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO macro_factors (timestamp, country, inflation_rate, economic_uncertainty)
            VALUES (?, ?, ?, ?)
        ''', (
            datetime.now(),
            country,
            inflation_rate,
            economic_uncertainty
        ))
        conn.commit()

def update_macro_factors():
    """
    Обновляет данные по макроэкономическим факторам для списка стран.
    """
    countries = [
        {'name': 'United States', 'code': 'US'},
        {'name': 'China', 'code': 'CN'},
        {'name': 'India', 'code': 'IN'},
        {'name': 'Brazil', 'code': 'BR'},
        {'name': 'South Korea', 'code': 'KR'},
        {'name': 'Germany', 'code': 'DE'},
    ]

    for country in countries:
        inflation_rate = fetch_inflation_rate(country['code'])
        economic_uncertainty = fetch_economic_uncertainty(country['name'])

        if inflation_rate is not None:
            insert_macro_factors(country['name'], inflation_rate, economic_uncertainty)
            print(f"Данные по макроэкономическим факторам для {country['name']} успешно обновлены.")
        else:
            print(f"Не удалось обновить данные по макроэкономическим факторам для {country['name']}.")

if __name__ == "__main__":
    update_macro_factors()