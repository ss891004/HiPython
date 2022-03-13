

from exts.ext import dbs
from datetime import datetime

# 实体模型，对应数据库中的一张表
class User(dbs.Model):
    __tablename__="tb_user"
    id = dbs.Column(dbs.Integer, primary_key=True,autoincrement=True)
    username=dbs.Column(dbs.String(15),nullable=False)
    password=dbs.Column(dbs.String(64),nullable=False)
    phone=dbs.Column(dbs.String(11),nullable=False)
    isdelete=dbs.Column(dbs.Boolean,default=False)
    rdatetime = dbs.Column(dbs.DateTime,default=datetime.now)

    def __str__(self):
        return self.username

    def save(self):
        dbs.session.add(self)
        dbs.session.commit()

    def delete(self):
        dbs.session.delete(self)
        dbs.session.commit()

    def update(self):
        dbs.session.add(self)
        dbs.session.commit()


'''
加密
md5， sha1 sha256  sha512
import hashlib
'''