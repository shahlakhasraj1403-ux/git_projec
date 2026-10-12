import telebot

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.sad_message(message.chat.bot.id, 'wolcome in telegram')

@bot.message_handler(func=lambda message:True)
def reply(message):
    bot.send_message(message.chat.id,'پدر سگ')

bot.infinity_polling()