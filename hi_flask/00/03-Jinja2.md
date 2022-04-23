 模板
- 模板路径默认在Flask（app）创建的路径下
- 如果想自己指定模板路径
  - 在Flask创建的时候，指定template_folder
  - 在蓝图创建的时候，也可以template_folder
    - 蓝图指定此蓝图统一前缀  /xx
  - 模板中使用反向解析和在python代码中一样
    - url_for

静态资源
- 静态资源在Flask中是默认支持的
- 默认路径在和Flask同级别的static中
  - 可以Flask创建的时候指定 static_folder
  - 也可以在蓝图中指定
- 静态资源也是有路由的
  - endpoint是 static
  - 参数有一个filename
- {{ url_for('static', filename='xxx') }}



## 模板

+ 模板是呈现给用户的界面

在MVT中充当T的角色，实现了VT的解耦，开发中VT有这N:M的关系，一个V可以调用任意T，一个T可以被任意V调用

模板其实是一个包含响应文本的文件，其中用占位符(变量)表示动态部分，告诉模板引擎其具体的值需要从使用的数据中获取使用真实值替换变量，再返回最终得到的字符串，这个过程称为“渲染”

模板处理分为两个过程
	1. 加载
	2. 渲染 (render_template 函数的第一个参数是模板的文件名，后面的参数都是键值对，表示模板中变量对应的真实值。)

模板代码包含两个部分
	1. 静态HTML
	2. 动态插入的代码段


## Jinja2
模板语法
模板语法主要分为两种
	变量
	标签
	
+ 变量	{{   var  }}
	视图传递给模板的数据
	前面定义出来的数据
	变量不存在，默认忽略

+ 控制语句	{% tag  %}
	控制逻辑
	使用外部表达式
	创建变量
	宏定义


+ 判断语句
Jinja2 语法中的if语句跟 Python 中的 if 语句相似,后面的布尔值或返回布尔值的表达式将决定代码中的哪个流程会被执行:

{%if user.is_logged_in() %}
    <a href='/logout'>Logout</a>
{% else %}
    <a href='/login'>Login</a>
{% endif %}

过滤器可以被用在 if 语句中:

{% if comments | length > 0 %}
    There are {{ comments | length }} comments
{% else %}
    There are no comments
{% endif %}

+ 循环语句
我们可以在 Jinja2 中使用循环来迭代任何列表或者生成器函数

{% for post in posts %}
    <div>
        <h1>{{ post.title }}</h1>
        <p>{{ post.text | safe }}</p>
    </div>
{% endfor %}

在一个 for 循环块中你可以访问这些特殊的变量:

变量描述loop.index当前循环迭代的次数（从 1 开始）loop.index0当前循环迭代的次数（从 0 开始）loop.revindex到循环结束需要迭代的次数（从 1 开始）loop.revindex0到循环结束需要迭代的次数（从 0 开始）loop.first如果是第一次迭代，为 Trueloop.last如果是最后一次迭代，为 Trueloop.length序列中的项目数loop.cycle在一串序列间期取值的辅助函数

在循环内部,你可以使用一个叫做loop的特殊变量来获得关于for循环的一些信息

比如：要是我们想知道当前被迭代的元素序号，并模拟Python中的enumerate函数做的事情，则可以使用loop变量的index属性,例如:
{% for post in posts%}
{{loop.index}}, {{post.title}}
{% endfor %}

cycle函数会在每次循环的时候,返回其参数中的下一个元素,可以拿上面的例子来说明:
{% for post in posts%}
{{loop.cycle('odd','even')}} {{post.title}}
{% endfor %}

可以在循环的开始和结束位置放置一个 - 号去除for循环不换行情况下产生的空格



结构标签
block
	{% block xxx %}
	{% endblock %}
	块操作
		父模板挖坑，子模板填坑	
		
extends
	{% extends ‘xxx’ %}

	继承后保留块中的内容
	{{ super() }}

挖坑继承体现的是化整为零的操作

include
	{% include ’xxx’ %}
	包含，将其他html包含进来，体现的是由零到一的概念

marco
	{% marco hello(name) %}
		{{ name }}
	{% endmarco %}
	宏定义，可以在模板中定义函数，在其它地方调用

宏定义可导入
	{% from ‘xxx’ import xxx %}


### 模板继承
模板继承是为了重用模板中的公共内容。一般Web开发中，继承主要使用在网站的顶部菜单、底部。这些内容可以定义在父模板中，子模板直接继承，而不需要重复书写。

继承关键字
{% extends '父模板名' %}

标签定义的内容
{% block 块变量名称 %} {% endblock %}

相当于在父模板中挖个坑，当子模板继承父模板时，可以进行填充。
子模板使用 extends 指令声明这个模板继承自哪个模板
父模板中定义的块在子模板中被重新定义，在子模板中调用父模板的内容可以使用super()
父模板
base.html
{% block top %}
  顶部菜单
{% endblock top %}

{% block content %}
{% endblock content %}

{% block bottom %}
  底部
{% endblock bottom %}

子模板
extends指令声明这个模板继承自哪
{% extends 'base.html' %}
{% block content %}
 需要填充的内容
{% endblock content %}

模板继承使用时注意点：
不支持多继承
为了便于阅读，在子模板中使用extends时，尽量写在模板的第一行。
不能在一个模板文件中定义多个相同名字的block标签。
当在页面中使用多个block标签时，建议给结束标签起个名字，当多个block嵌套时，阅读性更好。

包含（Include）
包含(Include)。它的功能是将另一个模板整个加载到当前模板中，并直接渲染。 
定义hello.html文件
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
我是第一个hello网页文件
</body>
</html>

定义第二个hello2.py文件
{% include 'hello.html'%}

我是第二个hello网页文件

包含在使用时，如果包含的模板文件不存在时，程序会抛出TemplateNotFound异常，可加上ignore missing关键字。如果包含的模板文件不存在，会忽略这条include语句。
{% include 'hello3.html' ignore missing%}

我是第二个hello网页文件
在网页中显示为：（此时忽略了导入文件） 

### 过滤器
过滤器的本质就是函数。有时候我们不仅仅只是需要输出变量的值，我们还需要修改变量的显示，甚至格式化、运算等等，而在模板中是不能直接调用 Python 中的某些方法，那么这就用到了过滤器。

使用方式：

过滤器的使用方式为：变量名 | 过滤器。
{{variable | filter_name(*args)}}

如果没有任何参数传给过滤器,则可以把括号省略掉
{{variable | filter_name}}

+ default
如果传入变量代码块的值为 None，则传入默认值：
{{ post.date | default("2016-11-22") }}

+ float

将传入变量代码块中的值转换为浮点数，类似于 Python 的 float()
{{ 75 | float }}

+ int
类似于 Python 的 int()
{{ 75.5 | int }}

+ lenght
类似于 Python 中的 len()
The Count: {{ post.tags | lenght }}

+ title
将传入变量代码块的 String 的首字母转换成大写，成为一个合格的 Title。
{{ "post title" | title }}

+ round
类似于 Python 的 round() 定义浮点数的精度。

{{ 3.14159 | round(1) }}

+ common 参数：四舍五入
+ floor 参数：截取整数部分
+ ceil 参数：向上取整
{{ 4.7 | rount(1, "common")}}

+ join
将传入变量代码块的列表变量中的元素作为字符串连接起来，类似于 Python 的 join()

{{ ['JmilkFan', 'fanguiju' ] | join(',')}}

+ tojson
过滤器 tojoin 实际上是调用了 Python 的 json.dumps 函数来序列化对象，一样的需要确保传入变量代码块的是一个可以被序列化的对象 Dict。

{{ {"key": "value" | tojson }}}

如果我们采用将 SQLAlchemy models 的查询对象直接传入模板文件中进行渲染的方式来生成整个 HTML 页面时，我们就会常常使用到 tojson 过滤器，而且我们还需要将序列化后的结果进行 safe 处理，才能保证其安全性。

{{ posts | tojson | safe }}

+ truncate

用于截取指定长度的 String 对象，并在截取后的子字符串后添加省略号。

{{ "a long stringggggggggggggggggg " | truncate(5) }}

+ escape

如果传入变量代码块的是 HTML 字符串，则将该字符串中的 &、<、>、’、” 作为 HTML 的转义序列打印。

{{ "<h1>Title<\h1>" | escape }}

+ safe

safe 过滤器含有 escape 的功能，将传入到变量代码块中的 HTML 字符串中的特殊符号进行 HTML 转义，这是必要的安全手段。 
假如我们需要直接将 HTML 作为变量传入到变量代码块中，而且这个传入的接口是公开的话，我们就需要防止用户提交恶意的 HTML 代码。如果 Jinja 没有 HTML 转义功能的话，那么我们访问这个变量代码块的时候就会运行这些被提交的恶意 HTML 代码了。EG. 一个用户在回复框输入了含有 Script 标签的 HTML 代码，那么所有打开该页面的浏览器都会执行这些 Script。

但有一个问题就是：在有些情况下我们不应该对 HTML 进行转义且需要保证安全性的，对于这个问题，escape 过滤器是无法解决的。所以 Jinja 提供了 safe 过滤器。

{{ "<h1>Post Title"</h1> | safe }}



+ 注释代码块使用 {# doc #} 