from exts.ext import dbs


class User(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True, autoincrement =True)
    username = dbs.Column(dbs.String(16))

    def save(self):
        dbs.session.add(self)
        dbs.session.commit()


class Student(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True)
    s_name = dbs.Column(dbs.String(20))
    s_password = dbs.Column(dbs.String(256))

class Person(dbs.Model):
	__tablename__='person'
	id = dbs.Column(dbs.Integer,primary_key=True)
	name = dbs.Column(dbs.String(16),unique=True)


class Animal(dbs.Model):
    __abstract__= True
    id = dbs.Column(dbs.Integer, primary_key=True, autoincrement =True)
    a_name = dbs.Column(dbs.String(16))

class Dog(Animal):
     d_legs = dbs.Column(dbs.Integer, default=4)

class Cat(Animal):
     c_eat = dbs.Column(dbs.String(16), default='fish')