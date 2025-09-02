import telebot
from telebot.types import ReplyKeyboardMarkup

token_api="8264677194:AAFqJObW7ujFUgLajGayei5_bF0dxwypQco"
bot=telebot.TeleBot(token_api)

command={
    "start" : "show information buttons"
}

@bot.message_handler(commands=["start"])
def send_information(message):
    cid=message.chat.id
    markup=ReplyKeyboardMarkup()
    markup.add("🛍️ Products", "🛒 Cart")
    markup.add("📦 Track Order", "☎️ Contact Us")
    bot.send_message(cid,"use buttons",reply_markup=markup)

@bot.message_handler(func=lambda mesg:mesg.text=="☎️ Contact Us")

@bot.message_handler(content_types=["text"])
def send_message(message):
    cid = message.chat.id       
    bot.send_message(cid,"can i help you ?")
bot.infinity_polling()
