import telebot
import types

bot = telebot.TeleBot('5614260140:AAHKtiAW2Jcl1wb5F00CnpHi3zn2DqPOZOY')

@bot.message_handler(commands=['start'])

def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Сайт', url='https://pedobraz.ru/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Переход на сайт", reply_markup = markup)

@bot.message_handler(content_types = ["text"])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.fromuser.id, "Привет!")
    if message.text == "Наш сайт":
        bot.send_message(message.from_user.id, "https://pedobraz.ru/")
    if message.text == "help":
        bot.send_message(message.from_user.id, "Нажми на кнопку и получишь результат")
    if message.text == "/help":
        bot.send_message(message.fromuser.id, "Кнопка помощи")