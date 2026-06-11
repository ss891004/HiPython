在Python3.7中，http.server提供了5种参数，调用下面帮助命令可显示如下：

python -m http.server --help


python -m http.server 8080
上面的代码用来启动http服务器，默认IP是电脑本地无线IPv4网络，默认目录为命令行运行的目录，如果想要改变参数，调用03种的可变参数即可。


改变服务器的目录
对于改变文件目录，小编改为D盘为可访问盘，命令如下，其他参数使用方法类似。

python -m http.server 8080 -d d: