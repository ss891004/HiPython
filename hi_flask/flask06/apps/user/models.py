

from exts.ext import dbs
from datetime import datetime

class User(dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key=True,autoincrement=True)
    username=dbs.Column(dbs.String(15),nullable=False)
    password=dbs.Column(dbs.String(64),nullable=False)
    phone=dbs.Column(dbs.String(11),nullable=False)
    isdelete=dbs.Column(dbs.Boolean,default=False)
    rdatetime = dbs.Column(dbs.DateTime,default=datetime.now)

    def __str__(self):
        return self.username

'''
加密
md5， sha1 sha256  sha512
import hashlib


'''