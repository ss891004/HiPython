import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#从员工表(mySheet)的第2行开始逐行循环(到最后一行)
for myRow in list(mySheet.rows)[1:]:
    myList=[]
    #获取行(myRow)的第2列(姓名列)的字符串(即将要拆分的字符串)
    myStr=myRow[1].value
    #在字符串(myStr)中统计字符('-')的个数
    myMax=myStr.count('-')
    myCount=1
    #有多少个字符('-')就循环多少次
    while myCount<=myMax:
      #根据字符('-')将字符串(myStr)拆分为三个成员
      myParts=list(myStr.partition('-'))
      #在列表(myList)中添加第1个成员
      myList+=[myParts[0]]
      #将包含多个字符('-')的第3个成员赋值给字符串(myStr),以再次拆分
      myStr=myParts[2]
      #如果是最后一次循环
      if myCount==myMax:
         #则在列表(myList)中添加第3个成员
         myList+=[myParts[2]]
      #累计循环次数
      myCount+=1
    #删除列表(myList)的第1个成员，即删除分公司
    del myList[0]
    #删除列表(myList)的第3个成员，即删除组名
    del myList[1]
    #使用字符('-')将列表(myList)的所有剩余成员连接成字符串
    myRow[1].value='-'.join(myList)
myBook.save('结果表-员工表.xlsx')
