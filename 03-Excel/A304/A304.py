import openpyxl
#根据“录取表.xlsx”文件创建工作簿(myBook)
myBook=openpyxl.load_workbook('录取表.xlsx')
#创建列表(myNewRows)
myNewRows=[]
#循环工作簿(myBook)的工作表(mySheet)
for mySheet in myBook:
    #将工作表(mySheet)的考生数据添加到myNewRows
    myNewRows+=[[myCell.value for myCell in myRow]
               for myRow in mySheet.rows][1:]
#创建新工作表(myNewSheet),即录取表
myNewSheet=myBook.create_sheet('录取表')
#设置新工作表(myNewSheet)的表头
myNewSheet.append(['录取院校','专业','考生姓名','总分'])
#在新工作表(myNewSheet)中添加所有考生
for myNewRow in myNewRows:
    myNewSheet.append(myNewRow)
#保存工作簿，即将拼接多个工作表的结果保存为'结果表-录取表.xlsx'文件
myBook.save('结果表-录取表.xlsx')
