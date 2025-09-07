import telebot
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton

token_api="8264677194:AAFqJObW7ujFUgLajGayei5_bF0dxwypQco"
bot=telebot.TeleBot(token_api)

command={
    "start" : "show information buttons"
}

categoey=["theaters","🎵 Music","📚 E-Books"]
products={
    "📚 E-Books":["Psychology","Novel","History","Art & Music","Educational"],
     "theaters" :["Comedy","Social","History"],
     "Music"    :[]}


@bot.message_handler(commands=["start"])
def send_information(message):
    cid=message.chat.id
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛍️ Products", "🛒 Cart")
    markup.add("📦 Track Order", "☎️ Contact Us")
    bot.send_message(cid,"use buttons",reply_markup=markup)

@bot.message_handler(func=lambda mesg:mesg.text=="☎️ Contact Us")
def contact_answer(message):
    cid=message.chat.id
    print(message)
    text="📞 Contact Us:\n\n[Telegram Channel](https://google.com)\n[WhatsApp](https://google.com)"
    bot.send_message(cid,text,parse_mode="Markdown")

@bot.message_handler(func=lambda mesg:mesg.text=="🛍️ Products")
def product_answer(message):
    cid=message.chat.id
    markup=InlineKeyboardMarkup()
    buttons=[InlineKeyboardButton(text=categ ,callback_data=categ)  for categ in categoey]
    for i in range(0,len(buttons),3):
        markup.row(*buttons[i:i+3])
    bot.send_message(cid,"chose on category",reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data in categoey)
def answer_call_pro(call):
    cid = call.message.chat.id    
    if call.data=="📚 E-Books":
        markup=InlineKeyboardMarkup()
        buttons=[InlineKeyboardButton(text=book ,callback_data=book) for book in products["📚 E-Books"]]
        for i in range(0,len(buttons),3):
            markup.row(*buttons[i:i+3])
        random_but=InlineKeyboardButton(text="random",callback_data="random")
        user_enter=InlineKeyboardButton(text="📝 Search by Title/Author",callback_data="📝 Search by Title/Author")
        markup.add(random_but,user_enter)
        bot.answer_callback_query(call.id,"✅ You clicked the  E-Books button!")
        bot.send_message(cid,"✨ Pick a way to search for books",reply_markup=markup)

    elif call.data=="🎵 Music":
        cid=call.message.chat.id
        bot.send_message(cid,"wite name or singer or a part of the lyrics and let me find it for you ")
        bot.answer_callback_query(call.id,"✅ You clicked the  Music button!")

    elif call.data=="theaters":
        cid=call.message.chat.id
        markup=InlineKeyboardMarkup()
        buttons=[InlineKeyboardButton(text=theater , callback_data=theater)for theater in products["theaters"]]
        for i in range(0,len(buttons),3):
            markup.row(*buttons[i:i+3])
        bot.send_message(cid,"chose theater you want",reply_markup=markup)
        bot.answer_callback_query(call.id,"✅ You clicked the theater button!")




@bot.callback_query_handler(func=lambda call:call.data in products["📚 E-Books"])
def book_send(call):
    cid=call.message.chat.id
    bot.send_message(cid,"")

@bot.callback_query_handler(func=lambda call:call.data in products["theaters"])
def threar(call):
    bot.send_message()

@bot.callback_query_handler(func=lambda call:call.data in products["Music"])
def music_Answer(call):
    bot.send_message()

@bot.message_handler(content_types=["text"])
def send_message(message):
    cid = message.chat.id       
    bot.send_message(cid,"can i help you ?")

bot.infinity_polling()