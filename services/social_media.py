import os
from openai import OpenAI
from dotenv import load_dotenv
from bot.config import COINS_PAIRS

# Загружаем переменные окружения из файла .env
load_dotenv()

# Инициализируем клиент OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Функция для выполнения запроса к модели
def get_crypto_info(coin_pair):
    # Формируем промпт с использованием криптовалютной пары
    prompt = f"Найдите последние новости и информацию о BTC/USDT." #{coin_pair}

    # Выполняем запрос к API OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Вы - полезный ассистент, предоставляющий информацию о криптовалютных парах."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.7
    )

    # Получаем ответ
    result = response.choices[0].message.content.strip()
    return result

# Основная логика для прохода по всем криптовалютным парам и получения информации
def main():
    for pair in COINS_PAIRS:
        print(f"Информация о {pair}:")
        info = get_crypto_info(pair)
        print(info)
        print("-" * 80)

if __name__ == "__main__":
    main()