import telebot
import base
import app_api
bot = telebot.TeleBot(base.TOKEN)

print('bot created ...')

@bot.message_handler(commands=['start'])
def send_message(message):
    #print(message)
    bot.send_message(message.chat.id, test='wellcome to bot')

@bot.message_handler(commands=['help','support'])
def reply_message(message):
    bot.reply_to(message , text='درصورت نیاز به پیشتبانی با شماره 1505تماس بگیرید')


@bot.message_handler(commands=['news'])
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 =   telebot.types.InlineKeyboardButton(text= 'اخبار ورزشی' , url='https://varzesh3.com')
    btn2 =   telebot.types.InlineKeyboardButton(text= 'اخبار عمومی',url= 'https://entekhab.ir')
    btn3 =   telebot.types.InlineKeyboardButton(text='آپارت اسپرت',url= 'https://aparatsport.ir')

    markup.add(btn1 , btn2 , btn3)
    bot.send_message(message.chat.id, text="یکی از گزینه های زیر را انتخاب کنید ", reply_markup= markup) 

@bot.message_handler(commands= ['menu'])
def show_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    btn1  = telebot.types.KeyboardButton(text="درباره ما")
    btn2  = telebot.types.KeyboardButton(text= 'تماس با ما')
    btn3 = telebot.types.KeyboardButton(text= 'بازگشت')
    markup.add(btn1 , btn2 , btn3)
    bot.send_message(message.chat.id,text='یکی از گزینه های زیر را انتخاب کنید', reply_markup=markup)

@bot.message_handler(commands=['movie'])
def show_msg(message):
    msg = bot.send_message(message.chat.id, 'نام فیلم را وارد کنید')
    bot.register_next_step_handler(msg, show_movie_info)

def show_movie_info(message):
    movie_name = message.text

    result = app_api.get_movie_info_by_name(movie_name)
    info = f'title: {result[0]} / year: {result[1]}'
    bot.send_message(message.chat.id, info)

@bot.message_handler(func=lambda message:True)
def answer_to_other_mag(message):
    if message.text == 'درباره ما':
        description = 'بهترین بات آموزشی خوزستان'
        bot.send_message(message.chat.id, text=description)

    elif message.text == 'تماس با ما':
        email = 'shala@gmail.com'
        mobile = '09036477875575'
        office_add = 'ahavz'
        info = f'mobile = {mobile} and email = {email} and also office_add = {office_add}'
        bot.reply_to(message, text= info )

    elif message.text == 'بازگشت':
        markup = telebot.types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, text="بازگشت به صفحه اصلس", reply_markup= markup)

    else:
        bot.send_message(message.chat.id, text = "غیر قابل قبول")

if  __name__ == '__main__': 
    bot.infinity_polling()
