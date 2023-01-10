import telebot
from telebot import types

bot = telebot.TeleBot('5827315252:AAG3MaPfzVEPFkaawp7K53lF6xpNx0RCi70')


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='На сайт!', url='https://педобраз.рф')
    markup.add(btn)
    bot.send_message(msg.chat.id, 'Привет!', reply_markup=markup)


bot.infinity_polling()
