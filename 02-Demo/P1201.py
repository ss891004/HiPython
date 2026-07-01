import mysql.connector

def P01_connect_to_mysql_with_mysql_connector_python():
    # pip install mysql-connector-python
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="ry_plus"
    )
    cursor = conn.cursor()
    print('1111')
    cursor.execute("select version();")
    print(cursor.fetchone())

    cursor.close()
    conn.close()

def P02_create_db():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
    )
    db = conn.cursor()
    db.execute("CREATE DATABASE py_db")
    db.execute("SHOW DATABASES")
    for x in db:
        print(x)


def P03_create_tbl():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="py_db",
    )
    db = conn.cursor()
    db.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))") 
    db.execute("SHOW TABLES")
    for x in db:
        print(x)


def P04_alter_tbl():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="py_db",
    )
    db = conn.cursor()
    db.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    db.execute("DESC sites")
    for x in db:
        print(x)


def P05_insert_tbl_1():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="py_db",
    )
    db = conn.cursor()
    sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val = ("RUNOOB", "https://www.runoob.com")
    db.execute(sql, val)
    
    conn.commit()    # 数据表内容有更新，必须使用到该语句
    
    print(db.rowcount, "记录插入成功。")

    for x in db:
        print(x)

def P05_insert_tbl_2():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="py_db",
    )
    db = conn.cursor()
    sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
    ]
    db.executemany(sql, val)
    
    conn.commit()    # 数据表内容有更新，必须使用到该语句
    
    print(db.rowcount, "记录插入成功。")

    for x in db:
        print(x)

def P06_select_tbl():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="py_db",
    )
    db = conn.cursor()
    sql = "select * from sites"
 
    db.execute(sql)
    results = db.fetchall()
    for x in results:
        print(x)

    print("------")
    db.execute(sql)
    results = db.fetchone()
    print(results)


if __name__ =="__main__":

    P06_select_tbl()