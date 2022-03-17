

from exts.ext import dbs
from datetime import datetime


class Article(dbs.Model):
    id=dbs.Column(dbs.Integer,primary_key=True,autoincrement=True)
    title = dbs.Column(dbs.String(50),nullable=False)
    content=dbs.Column(dbs.Text,nullable=False)
    pdatetime=dbs.Column(dbs.DateTime,default=datetime.now)
    click_num=dbs.Column(dbs.Integer,default=0)
    save_num=dbs.Column(dbs.Integer,default=0)
    love_num=dbs.Column(dbs.Integer,default=0)

    # 1对n 的关系
    user_id= dbs.Column(dbs.Integer,dbs.ForeignKey('tb_user.id'),nullable=False)
