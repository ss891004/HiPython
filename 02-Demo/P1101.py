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