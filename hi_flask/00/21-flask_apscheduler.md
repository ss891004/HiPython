APScheduler 支持三种调度任务：固定时间间隔，固定时间点（日期），Linux 下的 Crontab 命令。
APScheduler 使用起来还算是比较简单。运行一个调度任务只需要以下三部曲。

新建一个 schedulers (调度器) 。
添加一个调度任务(job stores)。
运行调度任务
基础组件：

APScheduler 有四种组件，分别是：调度器(scheduler)，作业存储(job store)，触发器(trigger)，执行器(executor)。

schedulers（调度器）

它是任务调度器，属于控制器角色。它配置作业存储器和执行器可以在调度器中完成，例如添加、修改和移除作业。
它提供 7 种调度器，能够满足我们各种场景的需要。例如：后台执行某个操作，异步执行操作等。调度器分别是：

BlockingScheduler : 调度器在当前进程的主线程中运行，也就是会阻塞当前线程。
BackgroundScheduler : 调度器在后台线程中运行，不会阻塞当前线程。
AsyncIOScheduler : 结合 asyncio 模块（一个异步框架）一起使用。
GeventScheduler : 程序中使用 gevent（高性能的Python并发框架）作为IO模型，和 GeventExecutor 配合使用。
TornadoScheduler : 程序中使用 Tornado（一个web框架）的IO模型，用 ioloop.add_timeout 完成定时唤醒。
TwistedScheduler : 配合 TwistedExecutor，用 reactor.callLater 完成定时唤醒。
QtScheduler : 你的应用是一个 Qt 应用，需使用QTimer完成定时唤醒。
job stores（作业存储器）

job信息默认是存到内存里面，服务重启后job信息会消失，当使用场景的job是需要反复运行时，可以将job信息持久化。

触发器(trigger)

date是最基本的一种调度，作业任务只会执行一次。
interval触发器，固定时间间隔触发。
cron触发器，在特定时间周期性地触发，和Linux crontab格式兼容。它是功能最强大的触发器

1）date 触发器

date 是最基本的一种调度，作业任务只会执行一次。它表示特定的时间点触发。它的参数如下：
参数 说明
run_date (datetime 或 str) 作业的运行日期或时间
timezone (datetime.tzinfo 或 str) 指定时区
func 要运行的方法
trigger 触发器类型

def my_job():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# 在 2020-08-13 14:00:01 时刻运行一次 my_job 方法
scheduler .add_job(func="my_job", trigger='date', run_date='2020-08-13 14:00:01',id="1")
1
2
3
4
2）interval 触发器

固定时间间隔触发。interval 间隔调度，参数如下：
参数 说明
weeks (int) 间隔几周
days (int) 间隔几天
hours (int) 间隔几小时
minutes (int) 间隔几分钟
seconds (int) 间隔多少秒
start_date (datetime 或 str) 开始日期
end_date (datetime 或 str) 结束日期
timezone (datetime.tzinfo 或str) 时区
code:

# 在 2020-12-13 14:00:01 ~ 2020-12-13 15:00:10 之间, 每隔两分钟执行一次 job_func 方法
scheduler .add_job(job_func, 
'interval', minutes=2, 
start_date='2020-12-13 14:00:01' , 
end_date='2020-12-13 15:00:10')
1
2
3
4
5
3）cron 触发器

在特定时间周期性地触发，和Linux crontab格式兼容。它是功能最强大的触发器。
我们先了解 cron 参数：
参数 说明
year (int 或 str) 年，4位数字
month (int 或 str) 月 (范围1-12)
day (int 或 str) 日 (范围1-31
week (int 或 str) 周 (范围1-53)
day_of_week (int 或 str) 周内第几天或者星期几 (范围0-6，0是周一，6是周天 或者 mon,tue,wed,thu,fri,sat,sun)
hour (int 或 str) 时 (范围0-23)
minute (int 或 str) 分 (范围0-59)
second (int 或 str) 秒 (范围0-59)
start_date (datetime 或 str) 最早开始日期(包含)
end_date (datetime 或 str) 最晚结束时间(包含)
timezone (datetime.tzinfo 或str) 指定时区
code:

# 在每年 1-3、7-9 月份中的每个星期一、二中的 00:00, 01:00, 02:00 和 03:00 执行 job_func 任务
scheduler .add_job(job_func,
 'cron', month='1-3,7-9',day='0, tue', hour='0-3')
# 每周1到3 晚上11:10:00 执行job_func 任务
scheduler .add_job(job_func,
 'cron', day_of_week='0-2',hour='11', minute='10',second='00')
# 每周1和周3 晚上11:10:00 执行job_func 任务
scheduler .add_job(job_func,
 'cron', day_of_week='0,2',hour='11', minute='10',second='00')
1
2
3
4
5
6
7
8
9
持久化

持久化可以用redis,mysql,mongodb等多种数据库，下面用mysql作为示例：
设置持久化数据库地址后，会自动在库中新增apscheduler_jobs 表储存job 信息，里面记录job 的id,下一次运行时间，以及job状态，interval 类型job执行完后会自动从表中删除。

持久化配置：

# mysql 数据库持久化配置
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@127.0.0.1:3306/mocker-api"
    # 存储位置
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
    }
# MongoDB 数据库持久化配置
from apscheduler.jobstores.mongodb import MongoDBJobStore
SCHEDULER_JOBSTORES = {
        'default': MongoDBJobStore(host='mongoserver', port=27017)
    }
1
2
3
4
5
6
7
8
9
10
11
12
实战（任务增删改暂停启动查）

项目结构：
|—app
| |—init.py
| | ---- task.py
| | —settings.py
| | —extensions.py
| | —view.py

init.py:

from extensions import scheduler
def create_app(config_name=None):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	# 启动apscheduler服务
	scheduler.start()
1
2
3
4
5
6
extensions.py

from flask_apscheduler import APScheduler
# 实例APScheduler定时任务
scheduler = APScheduler()
1
2
3
settings.py

class DevelopmentConfig():
	SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@127.0.0.1:3306/mocker-api"
	# 调度器开关
	SCHEDULER_API_ENABLED = True
	# -------持久化配置---------
	# job存储位置
	SCHEDULER_JOBSTORES = {
	    'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
	}
	# 线程池配置
	SCHEDULER_EXECUTORS = {
	    'default': {'type': 'threadpool', 'max_workers': 10}
	}
1
2
3
4
5
6
7
8
9
10
11
12
13
task.py

def my_job():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
1
2
view.py

def my_job():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

view.py
"""
添加data类型定时任务
{
	"task_id": "2",
	"run_time": "2020-8-12 12:03:00",
	"trigger_type": "date"
}
添加interval类型定时任务
{
	"task_id": "5",
	"interval_time": 10,
	"trigger_type": "interval"
}
添加cron类型定时任务
{
	"task_id": "5",
	"run_time": {
		"day_of_week": "2",
		"hour": "16",
		"minute": "19",
		"second": "00"
	},
	"trigger_type": "cron"
}
"""
from extensions import scheduler
# 新增job
@app.route('/addCron', methods=['post'])
def add_cron():
    jobargs = request.get_json()
    id = jobargs['task_id']
    trigger_type = jobargs['trigger_type']
    if trigger_type == "date":
        run_time = jobargs['run_time']
        job = scheduler.add_job(func="task:my_job",
                                trigger=trigger_type,
                                run_date=run_time,
                                replace_existing=True,
                                coalesce=True,
                                id=id)
        print("添加一次性任务成功---[ %s ] " % id)
    elif trigger_type == 'interval':
        seconds = jobargs['interval_time']
        seconds = int(seconds)
        if seconds <= 0:
            raise TypeError('请输入大于0的时间间隔！')
        scheduler.add_job(func="task:my_job",
                          trigger=trigger_type,
                          seconds=seconds,
                          replace_existing=True,
                          coalesce=True,
                          id=id)
    elif trigger_type == "cron":
        day_of_week = jobargs["run_time"]["day_of_week"]
        hour = jobargs["run_time"]["hour"]
        minute = jobargs["run_time"]["minute"]
        second = jobargs["run_time"]["second"]
        scheduler.add_job(func="task:my_job", id=id, trigger=trigger_type, day_of_week=day_of_week,
                          hour=hour, minute=minute,
                          second=second, replace_existing=True)
        print("添加周期执行任务成功任务成功---[ %s ] " % id)
    return jsonify(msg="新增任务成功")

# 暂停
@app.route('/<task_id>/pause',methods=['GET'])
def pause_job(task_id):
    response = {'status': False}
    try:
        scheduler.pause_job(task_id)
        response['status'] = True
        response['msg'] = "job[%s] pause success!" % task_id
    except Exception as e:
        response['msg'] = str(e)
    return jsonify(response)

#启动
@app.route('/<task_id>/resume',methods=['GET'])
def resume_job(task_id):
    response = {'status': False}
    try:
        scheduler.resume_job(task_id)
        response['status'] = True
        response['msg'] = "job[%s] resume success!" % task_id
    except Exception as e:
        response['msg'] = str(e)
    return jsonify(response)

#删除
@app.route('/<task_id>/remove',methods=['GET'])
def resume_job(task_id):
    response = {'status': False}
    try:
        scheduler.remove_job(task_id)
        response['status'] = True
        response['msg'] = "job[%s] remove success!" % task_id
    except Exception as e:
        response['msg'] = str(e)
    return jsonify(response)

#编辑
编辑逻辑与新增大致相同，编辑时如果传的task_id 任务表中已存在，那么会直接替换原来的task_id。 

#查job信息，获取的信息包括了job类型和执行时间，可以打印出来结果再根据自己的代码逻辑进行编写
#查看所有的job信息
ret_list = scheduler.get_jobs()
# 查看指定的job信息
ret_list = scheduler.get_job(jid)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
定时任务重复启动解决办法

注意：
如果flask用多进程进行部署，定时任务会重复启动，解决办法:在启动任务时，设置文件锁，当能获取到文件锁时，不在启动任务。该方法只适用于任务写死的场景，想要动态添加任务，该方法会使动态添加任务场景无法添加任务:

def create_app():
    app =Flask(__name__)
    # 启动定时任务
    scheduler_init(app)
    return app

def scheduler_init(app):
    """
    保证系统只启动一次定时任务
    :param app:
    :return:
    """
    if platform.system() != 'Windows':
        fcntl = __import__("fcntl")
        f = open('scheduler.lock', 'wb')
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            scheduler.init_app(app)
            scheduler.start()
            app.logger.debug('Scheduler Started,---------------')
        except:
            pass

        def unlock():
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()

        atexit.register(unlock)
    else:
        msvcrt = __import__('msvcrt')
        f = open('scheduler.lock', 'wb')
        try:
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            scheduler.init_app(app)
            scheduler.start()
            app.logger.debug('Scheduler Started,----------------')
        except:
            pass

        def _unlock_file():
            try:
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            except:
                pass

        atexit.register(_unlock_file)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
在任务中获取程序上文进行操作

总的来说就是在extensions.py中生成scheduler，在settings.py中配置scheduler，然后在__init__.py中启动scheduler服务，task.py文件中引入extensions.py中的scheduler，然后在任务函数中使用with scheduler.app.app_context()环境

from extensions import scheduler
def task1():
	with scheduler.app.app_context():
	 	#数据库操作
		CronTab.query.filter_by(cron_task_id=datas["task_id"]).first()

