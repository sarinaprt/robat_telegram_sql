from mysql.connector import connection

def database_exsist(database):
    config={"user":"root","host":"localhost","password":"belive_god1527"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute(f"DROP DATABASE IF EXSIST {database}")
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
                ID        INT    AUTO_INCREMENT PRIMARY KEY,
                CHAT_ID   VARCHAR(100)UNIQUE NOT NULL,
                PHONE     VARCHAR(20) UNIQUE ,
                CREATE_AT DATETIME DEFAULT CURRENT_TIMESTAMP,
                STATUS    DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  

    ) """)
    conn.commit()
    cur.close()
    conn.close()

def user_active():
    config={"user":"root","host":"localhost","password":"belive_god1527","database":"shop_bot"}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE user_active(
                ID           INT NOT NULL UNIQUE,
                CONTENT_TYPE VARCHR(20) NOT NULL ,
                TEXT         NVARCHAR(70) ,


                
    )""")
    conn.commit()
    cur.close()
    conn.close()