import telebot
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton

token_api="8264677194:AAFqJObW7ujFUgLajGayei5_bF0dxwypQco"
bot=telebot.TeleBot(token_api)

command={
    "start" : "show information buttons"
}
products=["📚 E-Books", "🎵 Music", "🎮 Game Keys"]

@bot.message_handler(commands=["start"])
def send_information(message):
    cid=message.chat.id
    markup=ReplyKeyboardMarkup()
    markup.add("🛍️ Products", "🛒 Cart")
    markup.add("📦 Track Order", "☎️ Contact Us")
    bot.send_message(cid,"use buttons",reply_markup=markup)

@bot.message_handler(func=lambda mesg:mesg.text=="☎️ Contact Us")
def contact_answer(message):
    cid=message.chat.id
    text="📞 Contact Us:\n\n[Telegram Channel](https://google.com)\n[WhatsApp](https://google.com)"
    bot.send_message(cid,text,parse_mode="Markdown")

@bot.message_handler(func=lambda mesg:mesg.text=="🛍️ Products")
def product_answer(message):
    cid=message.chat.id
    print(message)
    markup=InlineKeyboardMarkup()
    buttons=[InlineKeyboardButton(text=product ,callback_data=product)  for product in products]
    for i in range(0,len(buttons),3):
        markup.row(*buttons[i:i+3])
    bot.send_message(cid,"chose on category",reply_markup=markup)

@bot.message_handler(content_types=["text"])
def send_message(message):
    cid = message.chat.id       
    bot.send_message(cid,"can i help you ?")

bot.infinity_polling()