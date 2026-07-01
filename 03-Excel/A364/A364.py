import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
#根据员工表的基本工资列的数据，按照2%的比例计算书报费
myList=list(map(lambda myCell:myCell.value*0.02,
            list(myBook.active.columns)[4][1:]))
#在员工表的书报费列添加计算结果
myIndex=0
for myCell in list(myBook.active.columns)[5][1:]:
    myCell.value=myList[myIndex]
    myIndex+=1
myBook.save('结果表-员工表.xlsx')
