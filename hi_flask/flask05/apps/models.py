from exts.ext import dbs
from datetime import datetime


class User(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True, autoincrement =True)
    username = dbs.Column(dbs.String(16),nullable=False)
    password = dbs.Column(dbs.String(50),nullable=False)
    sex= dbs.Column(dbs.String(2),nullable=False)
    age=dbs.Column(dbs.Integer,nullable=True)
    phone = dbs.Column(dbs.String(11), unique=True)
    insert_time = dbs.Column(dbs.DateTime, default=datetime.now)

    def save(self):
        dbs.session.add(self)
        dbs.session.commit()


class Student(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    s_name = dbs.Column(dbs.String(20))
    s_password = dbs.Column(dbs.String(256))

class Person(dbs.Model):
	__tablename__='person'      # 表名
	id = dbs.Column(dbs.Integer,primary_key=True)
	name = dbs.Column(dbs.String(16),unique=True)


class Animal(dbs.Model):
    __abstract__= True  # 抽象的模型是不会在数据库中产生映射的
    id = dbs.Column(dbs.Integer, primary_key=True, autoincrement =True)
    a_name = dbs.Column(dbs.String(16))

class Dog(Animal):
     d_legs = dbs.Column(dbs.Integer, default=4)

class Cat(Animal):
     c_eat = dbs.Column(dbs.String(16), default='fish')