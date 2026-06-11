#创建自定义函数计算两列之和
def myFunc(x,y):
    if x.value is None:
       x.value=0
    if y.value is None:
       y.value=0
    return x.value+y.value
import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
#根据基本工资列和书报费列的数据，计算应发工资列的数据
myList=list(map(myFunc,list(myBook.active.columns)[3][1:],
                       list(myBook.active.columns)[4][1:]))
#在员工表(myBook.active)的应发工资列添加应发工资计算结果
myIndex=0
for myCell in list(myBook.active.columns)[5][1:]:
    myCell.value=myList[myIndex]
    myIndex+=1
myBook.save('结果表-员工表.xlsx')
