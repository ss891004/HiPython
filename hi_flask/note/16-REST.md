## 几个版本
+ pip install flask-restplus  停更
+ pip install Flask-RESTful     
+ pip install flask-restx   是flask-restful 的分支


## REST
CBV（class base views） 就是在视图里使用类处理请求。

REST: 资源（Resources）是构建在Flask可拔插视图之上，只要在资源上定义方法就能够访问多个HTTP方法。

开发一个接口的步骤:
A. 实例化一个 Api 对象
B. 时候后初始化中的个Api对象( 防止对象被重复引用)
C. 创建一个model 类，并迁移到相应的数据库中。
D. 创建一个继承Resource 的资源类， 并生成 GET，POST，DELETE，PUT等等方法。
E. 在Api 对象中增加资源类，并设置访问path（或在增加一个namespace）