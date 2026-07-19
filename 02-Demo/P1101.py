import re
text = "hello......word"

x= re.search("^hell",text)
print(x)

x1= re.findall("o",text)
print(x1)

x2=re.split("\s",text)
print(x2)

x3= re.sub("h","H",text)
print(x3)


p=re.compile('[abce]')

x4=p.findall(text)
print(x4)

'''
特殊字符
[] 列表符   [a-c]
. 点符号
^ 开始符
$ 结束符
*
+
？
{}
|

'''