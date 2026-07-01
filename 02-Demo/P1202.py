# 使用
from sqlalchemy import create_engine,text

def s01_select(engine):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT  * FROM sites"))
        for row in result:
            print(row)

def s02_select_some(engine):
    #2.3 Fetching Rows
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id,name FROM sites WHERE id > :id"), {"id": 2})
        for row in result:
            print(f"id: {row.id}  name: {row.name}")

def s03_insert(engine):
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO sites (name, url) VALUES (:x, :y)"),
            [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
        )
        conn.commit()

def s04_update(engine):
    # 2.4 Executing with an ORM Session
    from sqlalchemy.orm import Session

    stmt = text("SELECT id, name FROM sites WHERE id > :id ORDER BY id ")
    with Session(engine) as session:
        result = session.execute(stmt, {"id": 5})
        for row in result:
            print(row)

    with Session(engine) as session:
        result = session.execute(
            text("UPDATE sites SET name=:name WHERE id=:id"),
            [{"name": "sql_update", "id": 10}, {"name": "sql_update2", "id": 11}],
        )
        session.commit()

def s05_insert_with_Table(engine):
    from sqlalchemy import Table, Column, Integer, String,MetaData
    sites_table = Table(
    "sites",
    MetaData(),
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("url", String),)

    from sqlalchemy import insert
    stmt = insert(sites_table).values(name="spongebob", url="Spongebob Squarepants")
    with engine.connect() as conn:
        result = conn.execute(stmt)
        print(result)
        conn.commit()

    with engine.connect() as conn:
        result = conn.execute(
        insert(sites_table),
        [ {"name": "sandy", "url": "Sandy Cheeks"}, {"name": "patrick", "url": "Patrick Star"},],
        )
        conn.commit()

'''
sqlalchemy + mysql-connector-python
'''

from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()

"""
SQLAlchemy 类型	对应 MySQL 类型	说明
Integer	INT	整数类型
String(length)	VARCHAR(length)	可变长度字符串类型
Float	FLOAT	浮点类型
Boolean	TINYINT(1)	布尔类型（0 表示 False，1 表示 True）
DateTime	DATETIME	日期时间类型
Text	TEXT	长文本类型

"""
# ##################### 单表示例 #########################
# users表结构
class Users(Base):
    # 手动创建映射
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(256), nullable=False)
    age = Column(INTEGER)
    place = Column(VARCHAR(256), nullable=False)


    def __init__(self, id, name, age, place):
        self.id = id
        self.name = name
        self.age = age
        self.place = place

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
# ##################### 一对多示例 #########################
class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(INTEGER, primary_key=True)
    caption = Column(VARCHAR(50), default='篮球')


class Person(Base):
    __tablename__ = 'person'
    nid = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(32), index=True, nullable=True)
    hobby_id = Column(INTEGER, ForeignKey("hobby.id"))

    # 与生成表结构无关，仅用于查询方便
    hobby = relationship("Hobby", backref='pers')  # backref 反向查询


# ##################### 多对多示例 #########################

class Server2Group(Base):
    __tablename__ = 'server2group'
    id = Column(INTEGER, primary_key=True, autoincrement=True)  # 自增主键
    server_id = Column(INTEGER, ForeignKey('server.id'))
    group_id = Column(INTEGER, ForeignKey('group.id'))


class Group(Base):
    __tablename__ = 'group'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(64), unique=True, nullable=False)

    # 与生成表结构无关，仅用于查询方便
    servers = relationship('Server', secondary='server2group', backref='groups')  # secondary: 指定关系表


class Server(Base):
    __tablename__ = 'server'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    hostname = Column(VARCHAR(64), unique=True, nullable=False)

# ########################################################

#--------------------------------------------------------
# 初始化，创建表
def init_db():
    engine = create_engine("mysql+mysqlconnector://root:123456@127.0.0.1:3306/py_db", echo=True)
    Base.metadata.drop_all(engine) # 删除相关的表
    Base.metadata.create_all(engine) # 新建相关的表
    print('Create table successfully!')

#--------------------------------------------------------


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import text

def insert_data_DML():
    engine = create_engine("mysql+mysqlconnector://root:123456@127.0.0.1:3306/py_db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # 查询
    # cursor = session.execute('select * from users')
    # result = cursor.fetchall()

    # 添加
    with engine.connect() as con:
        data = ({'name': 'zhangsan', 'age': 20, 'value': 'zhangsan163@163.com'},
                 {'name': 'lisi', 'age': 20, 'value': 'li163@163.com'})
        statement = text("""insert into users(name,age,email) values(:name,:age,:value)""")
        for line in data:
            cursor = con.execute(statement, **line)

    print(cursor.lastrowid)
    session.close()



# 插入数据
def insert_data_ORM():
    # 初始化数据库连接
    engine = create_engine("mysql+mysqlconnector://root:123456@127.0.0.1:3306/py_db", echo=True)
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()
    # 插入单条数据
    # 创建新User对象
    new_user = Users(id=1, name='Jack', age=25, place='USA')
    # 添加到session
    session.add(new_user)
    # 提交即保存到数据库
    session.commit()

    # 插入多条数据
    user_list= [Users(id=2, name='Green', age=26, place='UK'),
                Users(id=3, name='Alex', age=31, place='GER'),
                Users(id=4, name='Chen', age=52, place='CHN'),
                Users(id=5, name='Zhang', age=42, place='CHN')
               ]
    session.add_all(user_list)
    session.commit()
    # 关闭session
    session.close()
    print('insert into db successfully!')


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 查询数据
def query_data():
    # 初始化数据库连接
    engine = create_engine("mysql+mysqlconnector://root:123456@127.0.0.1:3306/py_db", echo=True)

    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()

    # 查询所有place是CHN的人名
    # 创建Query查询，filter是where条件
    # 调用one()返回唯一行，如果调用all()则返回所有行:
    users = session.query(Users).filter(Users.place == 'CHN').all()
    print([use.name for use in users])
    # 输出：['Chen', 'Zhang']

    # 或者用如下查询
    users = session.query(Users.name).filter(Users.place == 'CHN').all()
    print(users)
    # 输出：[('Chen',), ('Zhang',)]

    session.close()
    print("select data successfully!")


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 更新数据
def update_data():
    # 初始化数据库连接
    engine = create_engine("mysql+mysqlconnector://root:123456@127.0.0.1:3306/py_db", echo=True)
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()

    # 数据更新，将Jack的place修改为CHN
    update_obj = session.query(Users).filter(Users.name=='Jack').update({"place":"CHN"})
    session.commit()

    session.close()
    print("Update data successfully!")


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 删除数据
def delete_data():
    # 初始化数据库连接
    engine = create_engine("mysql+mysqlconnector://root:123456@127.0.0.1:3306/py_db", echo=True)
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 创建session对象
    session = DBSession()

    # 数据更新，将Jack的记录删除
    update_obj = session.query(Users).filter(Users.name=='Jack').delete()
    session.commit()

    session.close()
    print("Delete data successfully!")


if __name__ =="__main__":
    # 1. Establishing Connectivity - the Engine
    #engine = create_engine("mysql+mysqlconnector://root:123456@127.0.0.1:3306/py_db", echo=True)
    # 2. Working with Transactions and the DBAPI

    #s01_select(engine)
    #s02_select_some(engine)
    #s03_insert(engine)
    #s04_update(engine)

    # 3. Working with Database Metadata
    #s05_insert_with_Table(engine)
    #s01_select(engine)

    init_db()
