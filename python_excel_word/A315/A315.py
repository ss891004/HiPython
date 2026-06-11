import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取收入表(mySheet)的单元格数据(myValues)
myValues=list(mySheet.values)
#创建空白的工作簿和工作表(即空白的新收入表)
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='收入表'
myNewSheet.append(['姓名','月份','金额'])
#从myValues的第2行开始逐行循环(到最后一行)
for myRow in myValues[1:]:
    mySum=0
    myMonth=0
    #从行的第2列开始逐列循环
    for myCell in myRow[1:]:
        myMonth+=1
        #累加行每个单元格的数据
        mySum+=myCell
        #如果累加之和大于10000
        if mySum>=10000:
           #则在新收入表(myNewSheet)中添加姓名、月份及累加之和
           myNewSheet.append([myRow[0],str(myMonth)+'月份',mySum])
           #并跳出行的循环(即停止累加)，直接进入下一循环
           break
myNewBook.save('结果表-收入表.xlsx')
