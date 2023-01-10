import telebot
import types

bot = telebot.TeleBot('5968657096:AAHy1 LMUOs0RWu2ccUbT15BIPMe6luJ2IYM')


@bot.message_handler(commands=['start'])
# def url(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='На сайт', url='https://pedobraz.ru/')
#     markup.add(btn1)
#     bot.send_message(message.from_user.id, "Нажми на кнопку", reply_markup=markup)
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра", reply_markup = markup)