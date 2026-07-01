import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取员工表(mySheet)的单元格数据(myValues)
myValues=list(mySheet.values)
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='员工表'
myNewSheet.append(['工号','分公司','部门','组名',
                   '姓名','最高学历','专业','出生年份'])
#从myValues的第2行开始逐行循环(到最后一行)
for myRow in myValues[1:]:
    myList=[]
    #拼接行(myRow)的第1列单元格的数据
    myList+=[myRow[0]]
    #获取行(myRow)的第2列单元格的数据(即将要拆分的字符串)
    myStr=myRow[1]
    #统计字符'-'的个数
    myMax=myStr.count('-')
    myCount=1
    #有多少个指定字符('-')就循环多少次
    while myCount<=myMax:
      #根据指定字符('-')将字符串(myStr)拆分为三个成员
      myParts=list(myStr.partition('-'))
      #在列表(myList)中添加第一个成员
      myList+=[myParts[0]]
      #将包含多个指定字符的第三个成员myParts[2]赋值给myStr，
      #以进行下次循环(即再次拆分)
      myStr=myParts[2]
      #如果是最后一次循环
      if myCount==myMax:
         #则在列表(myList)中添加第三个成员myParts[2]
         myList+=[myParts[2]]
      #累计循环次数
      myCount+=1
    #拼接行(myRow)的第3列及后面的所有单元格数据
    myList+=myRow[2:]
    myNewSheet.append(myList)
myNewBook.save('结果表-员工表.xlsx')
