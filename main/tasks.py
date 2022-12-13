from time import sleep
from clothes.celery import app
from telebot import TeleBot
from .models import RSSSubs

@app.task
def add_two_numbers(a: int, b: int) -> int:
    sleep(5)
    return a + b

BOT_API_KEY = 'YOUR'

@app.task
def send_message_to_user() -> str:
    users = [1342536, 1232435, 456534, 124354532, 1324353]
    bot = TeleBot(BOT_API_KEY)
    message = 'Привет, это тестовое сообщение'
    for user_id in users:
        try:
            bot.send_message(chat_id=user_id, text=message)
        except Exception as e: # обработать ошибку неправильного id
            print(e)
    return f'Сообщение пользователю {user_id} отправляется'


@app.task
def send_message_to_user_by_telegram() -> str:
    users = RSSSubs.objects.all()
    bot = TeleBot(BOT_API_KEY)
    message = 'Привет, это тестовое сообщение'
    for user in users:
        try:
            bot.send_message(chat_id=user.telegram_id, text=message)
        except Exception as e:
            print(e)
    return f'Сообщение пользователю {user.telegram_id} отправляется'

# send_message_to_user.delay() # запуск задачи в селери
# send_message_to_user()  обычный запуск