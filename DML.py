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

def product():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE product(
                product_id  INT AUTO_INCREMENT PRIMARY KEY,
                ID          INT NOT NULL,
                name_pro    VARCHAR(50) NOT NULL ,
                Description TEXT,
                price       DECIMAL(6,0),  
                stock       INT DEFAULT 0,
                CREAT       DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_up     DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (ID) REFERENCES CUSTOMER(USER_ID)
                )""")
    conn.commit()
    cur.close()
    conn.close()

def orders():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE orders(
                ORDER_ID    INT AUTO_INCREMENT PRIMARY KEY,
                UserId      INT NOT NULL,
                NAME_ORD    VARCHAR(50) NOT NULL,
                Status      ENUM('pending','paid','canceled') DEFAULT 'pending',
                FOREIGN KEY (UserId) REFERENCES CUSTOMER(USER_ID)

                
    )""")
        
    conn.commit()
    cur.close()
    conn.close()


if __name__=="__main__":
    database="shop_bot"
    database_exsist(database)
    customers()
    product()
    orders()