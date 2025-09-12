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
    cur.execute("SELECT author,GROUP_CONCAT(title) as titles FROM books WHERE gener=%s GROUP BY author" ,(date,))
    book=cur.fetchall()
    cur.close()
    conn.close()
    if book:
        return book
    else:
        return None

def file_url(author,title):
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("SELECT file_url FROM books WHERE author=%s AND title=%s GROUP BY author",(author,title))
    url=cur.fetchone()
    cur.close()
    conn.close()
    if url:
        return url[0]
    else:
        return None
    
def random_books():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("SELECT title,author,file_url FROM books ")
    books=cur.fetchall()
    cur.close()
    conn.close()
    if books:
        print(books)
        return books
    else:
        return None
    
def author_title(title,author):
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("SELECT author,file_url FROM books WHERE title=%s AND author=%s",(title,author))
    cur.close()
    conn.close()

def find_author(author):
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("SELECT ")
    cur.close()
    conn.close()


if __name__=="__main__":
    search_books()
    author_title()
    random_books()
    customer_add()
    insert_book()
    insert_music()
    insert_theater()
    file_url()
    chek_customer()

