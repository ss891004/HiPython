import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
#根据基本工资列和书报费列的数据，计算应发工资列的数据
myList=list(map(lambda myCell3,myCell4:myCell3.value+myCell4.value,
                  list(myBook.active.columns)[3][1:],
                  list(myBook.active.columns)[4][1:]))
#在员工表的应发工资列添加应发工资计算结果
myIndex=0
for myCell in list(myBook.active.columns)[5][1:]:
    myCell.value=myList[myIndex]
    myIndex+=1
myBook.save('结果表-员工表.xlsx')
