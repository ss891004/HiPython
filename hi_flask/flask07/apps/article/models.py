

from exts.ext import dbs
from datetime import datetime


# 实体模型，对应数据库中的一张表
class User(dbs.Model):
    __tablename__="tb_user"
    id = dbs.Column(dbs.Integer, primary_key=True,autoincrement=True)
    username=dbs.Column(dbs.String(15),nullable=False)
    password=dbs.Column(dbs.String(64),nullable=False)
    phone=dbs.Column(dbs.String(11),nullable=False)
    email=dbs.Column(dbs.String(50))
    isdelete=dbs.Column(dbs.Boolean,default=False)
    rdatetime = dbs.Column(dbs.DateTime,default=datetime.now)

    # 这关系可以在本模型中，也可以在有外键的模型中，但是只能出现一次
    # 这关系只限制在代码层面，不涉及数据库
    articles=dbs.relationship('Article', backref='br_user')

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



# 用户和文章的关系  1:n
# 文章
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

    comments = dbs.relationship('Comment', backref='br_xy')


    def __str__(self):
        return self.title

    def save(self):
        dbs.session.add(self)
        dbs.session.commit()

    def delete(self):
        dbs.session.delete(self)
        dbs.session.commit()

    def update(self):
        dbs.session.add(self)
        dbs.session.commit()


# 文章和评论的关系 m：n
# 评论
class Comment(dbs.Model):
    __tablename__="tb_comment"
    id=dbs.Column(dbs.Integer,primary_key=True,autoincrement=True)
    user_id= dbs.Column(dbs.Integer,dbs.ForeignKey('tb_user.id'),nullable=False)
    article_id =dbs.Column(dbs.Integer,dbs.ForeignKey('article.id'),nullable=False)
    content=dbs.Column(dbs.Text,nullable=False)
    cdatetime=dbs.Column(dbs.DateTime,default=datetime.now)
    def __str__(self):
        return self.content

    def save(self):
        dbs.session.add(self)
        dbs.session.commit()

    def delete(self):
        dbs.session.delete(self)
        dbs.session.commit()

    def update(self):
        dbs.session.add(self)
        dbs.session.commit()