import telebot
import random
from emoji import emo   
# Инициализация бота с использованием его токена
bot = telebot.TeleBot('Token')

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
@bot.message_handler(commands=['Meow'])
def send_meow(message):
    bot.reply_to(message,'мяу')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'Список команд:/help - список всех комманд,/heh - пишет he указанное количество раз,/start,/hello - приветствие')

@bot.message_handler(commands=['Meow'])
def send_meow(message):
    bot.reply_to(message,'мяу')

@bot.message_handler(commands=['emoji'])
def send_emo(message):
    bot.reply_to(message,emo())


# Запуск бота
bot.polling()
