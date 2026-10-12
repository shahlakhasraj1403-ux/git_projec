import telebot
import base
import home_api

bot = telebot.TeleBot(base.TOKEN)

print("bot API2 created...")


@bot.message_handler(commands=['gender'])
def call_api(message):
    msg = bot.send_message(message.chat.id,"Enter a name:")
    bot.register_next_step_handler(msg, get_gender)

def get_gender(message):
    name = message.text
    result = home_api.get_gender_by_name(name)
    if result == "ERROR":
        bot.send_message(message.chat.id,"Something went wrong pls try agian" )
    else:
        bot.send_message(message.chat.id,f"Gender: {result[0]}\n"f"Probability: {result[1]}")


if __name__ == "__main__":
    bot.infinity_polling()