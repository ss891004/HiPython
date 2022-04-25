from exts.ext import dbs
from datetime import datetime


class UserModel(dbs.Model):
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