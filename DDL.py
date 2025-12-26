from mysql.connector import connection



def customer_add(USERNAME,CHAT_ID,NAME):
    try:
        config={"user":"root","host":"localhost","password":".......","database":"shop_bot"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute("INSERT INTO CUSTOMER(USERNAME,CHAT_ID,NAME)VALUES(%s,%s,%s)",(USERNAME,CHAT_ID,NAME))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        print(f"problem in ad_custom {e}⚠️ ")

def chek_customer(CHAT_ID):
    try:
        config={"user":"root","host":"localhost","password":".........","database":"shop_bot"}
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
    except Exception as e :
        print(f"problem in check_custom {e}⚠️ ")

    
def find_user_id(CHAT_ID):
    try:
        config={"user":"root","host":"localhost","password":"........","database":"shop_bot"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute("SELECT USER_ID FROM CUSTOMER WHERE CHAT_ID=%s",(CHAT_ID,))
        user_id=cur.fetchone()
        cur.close()
        conn.close()
        if user_id:
            return user_id[0]
        else:
            return None
    except Exception as e :
        print(f"problem in find_user {e}⚠️ ")

def insert_book(title ,gener,author,file_url):
    try:
        config={"user":"root","host":"localhost","password":".........","database":"shop_bot"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute("INSERT INTO BOOKS(title ,gener,author,file_url)VALUES (%s,%s,%s,%s)",(title ,gener,author,file_url))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        print(f"problem in ad_book {e}⚠️ ")


def search_books(date):
    try:
        config={"user":"root","host":"localhost","password":".........","database":"shop_bot"}
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
    except Exception as e:
        print(f"problem in search_book {e}⚠️ ")


def file_url_book(author,title):
    try:
        config={"user":"root","host":"localhost","password":".........","database":"shop_bot"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute("SELECT file_url FROM books WHERE author=%s AND title=%s",(author,title))
        url=cur.fetchall()
        cur.close()
        conn.close()
        if url:
            return url[0][0]
        else:
            return None
    except Exception as e :
        print(f"problem in book_url {e}⚠️ ")

    
def random_books():
    try:
        config={"user":"root","host":"localhost","password":"........","database":"shop_bot"}
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
    except Exception as e :
        print(f"problem in random_book {e}⚠️ ")

def insert_theater(title,pic_url,text,Duration,price,actors,stock,gener):
    try:
        config={"user":"root","host":"localhost","password":".........","database":"shop_bot"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute("INSERT INTO ticket(title,pic_url,text,Duration,price,actors,stock,gener)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(title,pic_url,text,Duration,price,actors,stock,gener))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        print(f"problem in ad_theater {e}⚠️ ")

                
def theater(gener):
    try:
        config={"user":"root","password":"..........","host":"localhost","database":"shop_bot"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute("SELECT title,text,Duration,price,actors,pic_url,tk_id,stock FROM ticket WHERE gener=%s",(gener,))
        url=cur.fetchall()
        cur.close()
        conn.close() 
        if url:
            return url
        else:
            return None
    except Exception as e:
        print(f"problem in select_theater {e}⚠️ ")


def add_orders(user_id,ITEM_TYPE,quantity):
    try:
        config={"user":"root","password":".........","host":"localhost","database":"shop_bot"} 
        conn=connection.MySQLConnection(**config) 
        cur=conn.cursor()
        cur.execute("INSERT INTO orders(user_id,ITEM_TYPE,quantity)VALUES(%s,%s,%s)",(user_id,ITEM_TYPE,quantity))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"problem in ad_orders {e}⚠️ ")

def REPORT():
    try:
        config={"user":"root","host":"localhost","password":"........","database":"shop_bot"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute("""SELECT c.CHAT_ID, c.USERNAME
                        FROM customer c
                        INNER JOIN orders o ON c.user_id = o.user_id
                        GROUP BY c.user_id
                        HAVING DATE(MAX(o.creat_at)) = DATE(NOW());
                        """)
        active=cur.fetchall()
        cur.close()
        conn.close()
        if active:
            print(active)
            return active
        else:
            return None
    except Exception as e:
        print(f"problem in report {e}⚠️ ")

def update_quantity(quantity,tk_id):
    try:
        config={"user":"root","password":"........","host":"localhost","database":"shop_bot"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute("update ticket set stock=stock-%s where tk_id=%s",(quantity,tk_id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        print(f"problem in ad_custom {e}⚠️ ")

def check_stock(tk_id):
    try:
        config={"user":"root","password":"..........","host":"localhost","database":"shop_bot"}
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute("select stock from ticket where tk_id=%s",(tk_id,))
        stock=cur.fetchone()
        cur.close()
        conn.close()
        if stock:
            return stock[0]
        else:
            return None
    except Exception as e :
        print(f"problem in check_stock {e}⚠️ ")


if __name__=="__main__":
    search_books()
    random_books()
    customer_add()
    insert_book()
    insert_theater()
    file_url_book()
    chek_customer()
    theater()
    add_orders()
    REPORT()
    find_user_id()
    update_quantity()
    check_stock()
