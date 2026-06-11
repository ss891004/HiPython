import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook['一维表']
myRange=list(mySheet.values)[1:]
myTypes=list({myCell.value: '' for myCell in mySheet['B'][1:]})
#print(myTypes)
myQuarters=list({myCell.value: '' for myCell in mySheet['A'][1:]})
#print(myQuarters)
myNewBook=openpyxl.Workbook()
myNewSheet=myNewBook.active
myNewSheet.title='二维表'
myNewSheet.append(['季度'] + myTypes)
for myQuarter in myQuarters:
  mySets=[(myQuarter,myType) for myType in myTypes]
  myNewSheet.append([myQuarter]+[list(filter(lambda myParam:myParam[0]
   ==mySet[0] and myParam[1]==mySet[1],myRange))[0][2] for mySet in mySets])
myNewBook.save('结果表-收入表.xlsx')
