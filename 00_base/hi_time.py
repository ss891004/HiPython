import time


'''
三种时间状态：时间戳、时间元组、字符串
四个转换函数：localtime、strftime、strptime、mktime

'''

print("获取当前时间戳:%s"%time.time())
print("获取当前时间元组:",time.localtime())
print("获取当前时间字符串:",time.strftime("%Y/%m/%d %H:%M:%S",time.localtime()))



import time
# 获取当前时间戳,从1970年1月1日开始经历过的秒数
print("获取当前时间戳:%s"%time.time())
# 时间戳 => 时间元组
print(time.localtime(time.time()-60*60*24))
print("获取当前时间元组:",time.localtime())
p_tuple=time.localtime()
# 时间元组转字符串format
print(time.strftime("%Y-%m-%d",p_tuple))
print(time.strftime("%Y/%m/%d %H:%M:%S",p_tuple))
# 字符串转时间元祖parse
print(time.strptime("2019-6-18 12:05:34","%Y-%m-%d %H:%M:%S"))
# 时间元组转时间戳
print(time.mktime(p_tuple))



