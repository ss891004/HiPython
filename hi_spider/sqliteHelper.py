
import atexit
import sqlite3
from contextlib import contextmanager, closing
from pathlib import Path

_conn = None
_config = {}

def db_config(database: str, **kw):
    global _config
    kw['database'] = str(database)
    _config = kw

def connect():
    global _conn
    if not _conn:
        _conn = sqlite3.connect(**_config)
        atexit.register(_conn.close)
    print(id(_conn))
    return _conn

@contextmanager
def trans():
    try:
        conn = connect()
        yield
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e

def execute(sql: str, params: list = []):
    return connect().execute(sql, params)

def executemany(sql: str, params: list = []):
    return connect().executemany(sql, params)

def executescript(sql: str):
    return connect().executescript(sql)

def executefile(pkg: str, filename: str):
    '''
    执行程序中附带的资源文件
    pkg         : 所在包的名称
    filename    : 相关于包的文件名，包括路径
    '''
    from pkgutil import get_data
    print(get_data)
    data = get_data(pkg, filename)
    print(data)
    sql = data.decode('utf8')
    print(sql)
    return executescript(sql)

def find(sql: str, params: list = [], multi=True):
    '''执行sql 语句，并返行多行或一行记录'''
    cur = execute(sql, params)
    with closing(cur):
        return cur.fetchall()if multi else cur.fetchone()

def findone(sql: str, params: list = []):
    '''执行 sql 语句，并返回一行记录'''
    return find(sql, params, multi=False)

def findvalue(sql: str, params: list = []):
    '''执行 sql 语句，并返回一个值 '''
    row = findone(sql, params)
    return row and row[0]

if __name__ == '__main__':
    db_config('xxxx.db')
    executescript('drop table if exists test;''drop table if exists school;')
    #executefile('.','D:/Python/test.sql')
    executescript('create table if not exists test(id  int  primary key,name text,age  int);''create table if not exists school(userid int primary key,class   text);')
    with trans():
        execute('insert into test values(?,?,?)',[4,'Tom',23])
        executemany('insert into test values(?,?,?)',[[5,'Alice',22],[6,'John',21]])


    usercount=findvalue('select count(id) from test')
    
    #id,name,age=findone('select * from test where name=?',['tom'])

    print(find('select * from test',[],False))
    
    for id,name,age in find('select * from test',[],False):
        print(id,name,age)
