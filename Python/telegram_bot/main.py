import telebot
from telebot import types

bot = telebot.TeleBot('5827315252:AAG3MaPfzVEPFkaawp7K53lF6xpNx0RCi70')


commands = {
    'Привет!': ('text', 'Здарова'),
    'help': ('text', 'Типа помощь'),
    'timothy': ('anim', 'https://thumbs.gfycat.com/UnrulyThriftyHedgehog-size_restricted.gif')
}


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    markup = types.ReplyKeyboardMarkup()
    for command in commands.keys():
        print(command)
        btn = types.KeyboardButton(text=command)
        markup.add(btn)
    bot.send_message(msg.chat.id, 'Привет!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(msg: types.Message):
    answer = commands.get(msg.text)
    if answer is None:
        bot.send_message(msg.chat.id, 'Не знаю такой команды')

    match answer[0]:
        case 'text':
            bot.send_message(msg.chat.id, answer[1])
        case 'anim':
            bot.send_animation(msg.chat.id, answer[1])



bot.polling()
