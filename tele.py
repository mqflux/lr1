import telebot
from telebot import types

TOKEN = '6276727396:AAHAbJRKugcBL8pVI5gsyMpbSvFOSLlaP3A'
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = types.ReplyKeyboardMarkup()
    user_markup.row('Изображение', 'Песня')
    user_markup.row('Репозиторий')
    bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=user_markup)


# Обработчик команды изображение
@bot.message_handler(commands=['Изображение'])
def handle_generate_image(message):
    bot.send_photo(message.chat.id, open("cat1.jpg", "rb"))


# Обработчик команды песня
@bot.message_handler(commands=['Песня'])
def handle_generate_audio(message):
    bot.send_audio(message.chat.id, open("music.mp3", "rb"))


# Обработчик команды репозиторий
@bot.message_handler(commands=['Репозиторий'])
def handle_repo_link(message):
    repo_link = 'NotYet'
    bot.send_message(message.from_user.id, f'Ссылка на репозиторий: {repo_link}')

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == 'Изображение':
        handle_generate_image(message)
    elif message.text == 'Песня':
        handle_generate_audio(message)
    elif message.text == 'Репозиторий':
        handle_repo_link(message)
    else:
        bot.send_message(message.from_user.id, 'Неизвестная команда. Используйте кнопки.')

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)