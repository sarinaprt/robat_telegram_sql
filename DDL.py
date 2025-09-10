from mysql.connector import connection



def customer_add(USERNAME,CHAT_ID,NAME):
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("INSERT INTO CUSTOMER(USERNAME,CHAT_ID,NAME)VALUES(%s,%s,%s)",(USERNAME,CHAT_ID,NAME))
    conn.commit()
    cur.close()
    conn.close()

def insert_book(title ,gener,author,file_url):
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("INSERT INTO BOOKS(title ,gener,author,file_url)VALUES (%s,%s,%s,%s)",(title ,gener,author,file_url))
    conn.commit()
    cur.close()
    conn.close()

def insert_music():
    config={"user":"root","host":"localhost","password":"belive_gof1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""""")
    conn.commit()
    cur.close()
    conn.close()

def insert_theater():
    config={"user":"root","host":"localhost","password":"belive_gof1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""""")
    conn.commit()
    cur.close()
    conn.close()

def chek_customer(CHAT_ID):
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("SELECT CHAT_ID FROM customer where CHAT_ID=%s",(CHAT_ID,))
    chat_id=cur.fetchone()
    cur.close()
    conn.close()
    if chat_id:
        print(chat_id)
        return chat_id[0]
    else:
        return None
    
def search_books(date):
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("SELECT author,gener,title FROM books WHERE gener=%s",(date,))
    book=cur.fetchall()
    cur.close()
    conn.close()
    if date:
        return book
    else:
        return None


if __name__=="__main__":
    search_books()
    chek_customer()
    customer_add()
    insert_book()