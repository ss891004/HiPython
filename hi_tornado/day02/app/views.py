
import tornado.web

from app.models import create_db, drop_db, Student
from utils.conn import session

from sqlalchemy import not_, or_, and_


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('hello day02 tornado')


class XindexHandler(tornado.web.RequestHandler):

    def get(self):
        # 页面渲染
        items = ['Python', 'Php', 'C++', '精通']
        self.render('index.html', items=items, items2=items)


class DbHandler(tornado.web.RequestHandler):
    def get(self):
        create_db()
        self.write('创建表成功')


class DropDbHandler(tornado.web.RequestHandler):
    def get(self):
        drop_db()
        self.write('删除表成功')


class AddStuHandler(tornado.web.RequestHandler):

    def post(self):
        # 创建单条数据
        # stu = Student()
        # stu.s_name = 'xiaoming'
        # session.add(stu)
        # session.commit()
        # 创建多条数据
        stus = []
        for i in range(10):
            stu = Student()
            stu.s_name = 'xiaoming_%s' % i
            stus.append(stu)

        session.add_all(stus)
        session.commit()
        self.write('新增数据成功')


class StusHandler(tornado.web.RequestHandler):

    def get(self):
        # stu = Student.query.filter(Student.s_name == 'xiaoming_0').all()
        stus = session.query(Student).filter(Student.s_name == 'xiaoming_0').all()
        stus = session.query(Student).filter_by(s_name = 'xiaoming_0').all()

        print(stus)
        self.write('查询数据成功')

    def delete(self):
        # 实现删除，第一种方式，session.delete()
        stu = session.query(Student).filter(Student.s_name == 'xiaoming_0').first()
        if stu:
            session.delete(stu)
            session.commit()
        # 第二种: 调用delete()方法
        session.query(Student).filter(Student.s_name == 'xiaoming_1').delete()
        session.commit()
        self.write('删除成功')

    def patch(self):
        # 实现修改部分的属性
        # 第一种方式:
        stu = session.query(Student).filter(Student.s_name == 'xiaoming_2').first()
        stu.s_name = 'xiaohua'
        session.add(stu)
        session.commit()
        # 第二种方式: update()
        session.query(Student).filter(Student.s_name == 'xiaohua').update({'s_name': 'lisi'})
        session.commit()
        self.write('修改数据成功')
