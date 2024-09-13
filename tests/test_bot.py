import unittest
from telegram import Update
from telegram.ext import ContextTypes
from bot.bot import start, predict

class TestBot(unittest.TestCase):
    async def test_start_command(self):
        # Мокируем объект Update и Context
        update = Update(update_id=123, message=None)
        context = ContextTypes.DEFAULT_TYPE()

        # Вызываем команду /start
        response = await start(update, context)

        # Проверяем, что бот отправляет правильное сообщение
        self.assertIn("Привет", response.text)

    async def test_predict_command(self):
        # Мокируем объект Update и Context
        update = Update(update_id=124, message=None)
        context = ContextTypes.DEFAULT_TYPE()

        # Вызываем команду /predict
        response = await predict(update, context)

        # Проверяем, что бот отправляет сообщение о предсказании
        self.assertIn("Предсказание цены криптовалюты", response.text)

if __name__ == '__main__':
    unittest.main()