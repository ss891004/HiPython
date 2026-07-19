

import pandas as pd
from docxtpl import DocxTemplate
from docx.shared import Mm
from docxtpl import DocxTemplate, RichText, InlineImage

# 有多行数据
def fun1():
    # 1. 读取 Excel 数据
    df = pd.read_excel('data.xlsx')

    # 2. 将 DataFrame 转换为字典列表，格式如：
    # [{'序号': 1, '项目': 'A项目', '金额': 100}, {'序号': 2, '项目': 'B项目', '金额': 200}]
    # 处理一下空值，防止 Word 里出现 nan
    records = df.where(pd.notnull(df), '').to_dict('records')

    # 3. 组装要传给 Word 的数据字典
    # 这里的键名 'items' 必须和 Word 模板里的 {% for item in items %} 对应
    context = {
        'title': '项目汇总表',  # 模板里其他普通的占位符，比如 {{ title }}
        'items': records        # 循环填入的数据
    }

    # 4. 渲染并保存
    doc = DocxTemplate("template.docx")
    doc.render(context)
    doc.save("output_single.docx")
    print("✅ 单个 Word 生成完毕！")


def fun2():
    # 初始化模板对象
    doc = DocxTemplate("./temp/cla_info.docx")

    # 待填充的字典数据，其中key对应word模板中的填充名
    context = {
        "school": "清华大学",
        "cls_name": "三年二班",
        "teacher": "高手工具箱",
        "students_num": 4,
        # 班级的图片
        'cls_img': InlineImage(doc, "img/cls_img.png", height=Mm(75)),  # 假设图片路径和文件名与'avater'列一致
        #学生信息列表
        "students": [
            {"name": "张三", "age": 15, "gender": "男", "address": "成都市","score": RichText('优秀', color='FF0000', size=20, ), },
            {"name": "李四", "age": 16, "gender": "女", "address": "成都市","score": RichText('良好', color='000000', size=20, ), },
            {"name": "王五", "age": 17, "gender": "男", "address": "成都市","score": RichText('一般', color='FF0000', size=20, ), },
            {"name": "赵六", "age": 18, "gender": "女", "address": "成都市","score": RichText('差劲', color='000000', size=20, ), },
        ],
    }

    # 开始渲染context数据到模板文件中
    doc.render(context)
    doc.save("./temp/结果文档.docx")

def  fun3():
    '''
context：是自定义字典，可以取任何变量名，里面的键可以在template.docx中获取到
DocxTemplate：这是主要的类，传入模板文档路径即可完成初始化
render()：将自定义的字典作为数据源给模板文档
save()：就是用来保存一个新文档的方法
----------------------------------
列表循环展示
模版：
{%for text in list%}
{{ text }}
{%endfor%}

代码：'list': ['a', 'b', 'c']

----------------------------------

{%for k in dict%}
{{ k }}, {{dict[k]}}
{%endfor%}

    context = {

    'dict': {
        '0': 'a',
        '1': 'b',
        '2': 'c'
    }

    }
-----------------------------------
条件判断

{%if value > 10%}
数据大于10
{%else%}
数据小于等于10
{%endif%}





    '''
    doc = DocxTemplate("./template2.docx")

    image = InlineImage(
    doc,
    '/Users/shuaishi/Documents/照片/06400730施帅.jpg',
    width=Mm(33),
    height=Mm(48))


    context = {
        'title': '我是代码里的标题','aa':'南京大学', 'bb':"法学专业",'cs':"1975.11",'nl':'(58岁)',
        'list': ['a', 'b', 'c'],
            'dict': {
        '0': 'aa',
        '1': 'bb',
        '2': 'cd'
            },
            "image":image,
            'family': [{'cw':'妻子','xm':'aaa','age':18},
                       {'cw':'妻子','xm':'aaa','age':18},
                         {'cw':""},  {'cw':""},  {'cw':""},  {},  
                       
                       ]
                       }

    doc.render(context)
    doc.save('./new.docx')



if __name__ =="__main__":

    fun3()