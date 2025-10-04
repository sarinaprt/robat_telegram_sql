import telebot
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton
import DDL
import random

token_api="8264677194:AAFqJObW7ujFUgLajGayei5_bF0dxwypQco"
bot=telebot.TeleBot(token_api)

admin_id="5580972570"
command={
    "start" : "show information buttons",
    
}

admin_access={
    "add_Product":"add product to chanel"
}

categoey=["theaters","🎵 Music","📚 E-Books"]
products={
    "📚 E-Books":["📔 Psychology","📔 Novel","📔 History","📔 Art & Music","📔 Educational"],
     "theaters" :["🎭 Comedy","🎭 Drama","🎭 Children","🎭 Musical","🎭 Historical"],
     "Music"    :[]}

list=["➕️","number","➖","buy","cancel"]
status={}


@bot.message_handler(commands=["add_product"])
def learn_to_add_pro(message):
    cid=message.chat.id
    if cid==int(admin_id):
        bot.send_message(cid,"add your information like _\ngener:Psychology,Novel,History,Art & Music,Educational\nauthor:name_author_",parse_mode="Markdown")
    else:
        bot.send_message(cid,"can i help you ?")

@bot.channel_post_handler(content_types=["document"])
def channel_post(message):
    file_id=message.document.file_id
    name_douc=message.document.file_name
    caption=message.caption
    list_info=caption.split("\n")
    gener=list_info[0].split(":")[-1].strip().lower()
    author=list_info[1].split(":")[-1].strip().lower()
    DDL.insert_book(name_douc,gener,author,file_id)

@bot.message_handler(commands=["start"])
def send_information(message):
    cid=message.chat.id
    USERNAME=message.from_user.username  
    NAME=message.from_user.first_name 
    markup=ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛍️ Products", "🛒 Cart")
    markup.add("📦 Track Order", "☎️ Contact Us")
    id=DDL.chek_customer(cid)
    if not id:
        DDL.customer_add(USERNAME,cid,NAME)
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
    data=call.data.strip("📔 ")
    print(call)
    books=DDL.search_books(data)
    if books:
        for author,titles in books:
            title=titles.split(",")
            tt="\n".join([f"- {ti}" for ti in title])
            bot.send_message(cid, f"Author:{author}\nTitle:{tt}")  
        bot.send_message(cid,"write Author:....\nTitle: .....")
    else:
        bot.send_message(cid,"this gener is emoty")

@bot.callback_query_handler(func=lambda call:call.data=="random")
def random_book(call):
    cid=call.message.chat.id
    books=DDL.random_books()#[(,)]
    if books:
        chosen=random.choice(books)#tuple
        title=chosen[0]
        author=chosen[1]
        url=chosen[2]
        bot.send_document(cid,url,caption=f"title:{title}\nauthor:{author}")
    else:
        bot.send_message(cid,"this part is unvailable right now")

@bot.callback_query_handler(func=lambda call:call.data=="📝 Search by Title/Author")
def author_title(call):
    cid=call.message.chat.id
    bot.send_message(cid,"write author and title like:\n-author:author \n title:title-",parse_mode="Markdown")









def get_markup_button(quantity):
    markup=InlineKeyboardMarkup()
    markup=InlineKeyboardMarkup()
    add_but=InlineKeyboardButton(text="➕️" , callback_data=f"edit_{quantity+1}"if quantity>1 else "disabled")
    number_but=InlineKeyboardButton(text=str(quantity),callback_data="number")
    remove_but=InlineKeyboardButton(text="➖",callback_data=f"edit_{quantity-1}")
    next_but=InlineKeyboardButton(text="next",callback_data="next")
    cancel_but=InlineKeyboardButton(text="cancel",callback_data="cancel")
    markup.add(add_but,number_but,remove_but)
    markup.add(cancel_but,next_but)

@bot.callback_query_handler(func=lambda call:call.data in products["theaters"])
def threar(call):
    cid=call.from_user.id
    gener=call.data.strip("🎭 ")
    theat=DDL.theater(gener)
    if theat:
        len_list_thaeter=len(theat)
        index=0
        title=theat[index][0]
        text=theat[index][1]
        Duration=theat[index][2]
        price=theat[index][3]
        actors=theat[index][4]
        pic_url=theat[index][5]
        caption=f"{title}\n{text}\ntime:{Duration}\nprice:{price}\nactors:{actors}"
        buttons=get_markup_button(1)
        bot.send_photo(cid,pic_url,caption=caption,reply_markup=buttons)

@bot.callback_query_handler(func=lambda call:call.data in list)
def buton_shop(call):
    cid=call.from_user.id
    data=call.data
    if data=="➕️":
        bot.edit_message_reply_markup(cid)
    elif data=="➖":
            bot.edit_message_reply_markup(cid)
    elif data=="buy":
        pass
    elif data=="cancel":
        pass
            
            








@bot.callback_query_handler(func=lambda call:call.data in list)
def buy_or_cancel(call):
    pass   

@bot.channel_post_handler(content_types=["photo"])
def achive_photo(message):
    photo_url=message.photo[-1].file_id
    caption=message.caption.split("\n")
    title=caption[0]
    text=caption[1]
    Duration=caption[2]
    price=caption[3]
    actors=caption[4]
    DDL.insert_theater(title,photo_url,text,Duration,price,actors)


@bot.message_handler(content_types=["text"])
def message_find(message):
    if message.text.startswith(("Author","author")):#((text),index)
        cid=message.chat.id
        text=message.text.split("\n")
        author=text[0].split(":")[-1].strip("- ").lower()
        title=text[1].split(":")[-1].strip("- ").lower()
        url=DDL.file_url(author,title)
        if url:
            bot.send_document(cid,url)
        else:
            bot.send_message(cid,"sorry we dont have this book right know ")
    else:
        cid=message.chat.id
        print(message)
        bot.send_message(cid,"can i help you ?")

bot.infinity_polling()