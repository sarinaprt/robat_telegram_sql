from mysql.connector import connection

def database_exsist(database):
    config={"user":"root","host":"localhost","password":"belive_god1527"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS  {database}")
    cur.execute(f"CREATE DATABASE {database}")
    conn.commit()
    cur.close()
    conn.close()

def customers():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE CUSTOMER(
                USERNAME  NVARCHAR(50) NOT NULL ,
                USER_ID   INT    AUTO_INCREMENT PRIMARY KEY,
                CHAT_ID   VARCHAR(100)UNIQUE NOT NULL,
                PHONE     VARCHAR(20) UNIQUE ,
                CREATE_AT DATETIME DEFAULT CURRENT_TIMESTAMP,
                STATUS    DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  

    ) """)
    conn.commit()
    cur.close()
    conn.close()


def book_info():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE BOOKS(
                bok_id    INT AUTO_INCREMENT PRIMARY KEY,
                title     NVARCHAR(50) NOT NULL ,
                gener     ENUM("Psychology","Novel","History","religious","Educational") NOT NULL,
                author    NVARCHAR(50),
                file_url  VARCHAR(225) NOT NULL,
                creat_at  DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    cur.close()
    conn.close()


def MUSIC_info():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE music(
                ID_M      INT AUTO_INCREMENT PRIMARY KEY,
                title     NVARCHAR(50) NOT NULL,
                file_url  VARCHAR(225) NOT NULL,
                Format    ENUM('MP3','WAV','FLAC'),
                Duration  TIME,
                singer    NVARCHAR(50),
                creat_at  DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    cur.close()
    conn.close()


def theater_ticket():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE ticket(
                tk_id     INT AUTO_INCREMENT PRIMARY KEY,
                title     NVARCHAR(50) NOT NULL,
                pic_url   VARCHAR(225) NOT NULL,
                text      NVARCHAR(100),
                Duration  TIME,
                price     DECIMAL(7,3) NOT NULL,
                actors    NVARCHAR(50),
                creat_at  DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    cur.close()
    conn.close()


def orders():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE orders(
                ord_id    INT AUTO_INCREMENT PRIMARY KEY,
                user_id   INT NOT NULL,
                creat_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY user_id REFERENCES CUSTOMER(USER_ID)
    )""")
    conn.commit()
    cur.close()
    conn.close()


def order_item():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE order_item(
                id INT    AUTO_INCREMENT PRIMARY KEY,
                ord_id    INT NOT NULL,
                ITEM_TYPE ENUM("📚 E-Books","🎵 Music","theaters"),
                quantity  INT DEFAULT 0,

    )""")
    conn.commit()
    cur.close()
    conn.close()


if __name__=="__main__":
    database="shop_bot"
    database_exsist(database)
    customers()
    orders()
    order_item()
    book_info()
    MUSIC_info()
    theater_ticket()
