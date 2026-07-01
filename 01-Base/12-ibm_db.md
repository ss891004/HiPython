离线安装ibm_db大概步骤如下：

1.下载ibm_db安装压缩包，地址如下：
http://pypi.org     ibm-db

2.将ibm_db-x.y.z.tar.gz解压，然后将解压后的文件夹复制到 ..\Lib\site-packages（根据自己python安装目录修改）目录下

3.下载 DB2数据库的ODBC驱动相关文件，地址如下：
https://public.dhe.ibm.com/ibmdl/export/pub/software/data/db2/drivers/odbc_cli/
需要根据不同的系统，不同的位数来下载。

4.将nt32_odbc_cli.zip解压（解压后的文件夹为 clidriver）

5.将clidriver文件夹复制到 ..\Lib\site-packages\ibm_db-2.0.9 目录下，即setup.py的同级目录

6.打开命令行，在..\Lib\site-packages\ibm_db-2.0.9目录下 执行命令  python setup.py install 

7.进入python交互模式， 输入import ibm_db，如果没有报错即安装成功