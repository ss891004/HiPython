import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
#按照大写首字母，小写其余字母的规则更正员工表的英文名字列的单词
myList=list(map(lambda myCell:
                myCell.value[0:1].upper()+myCell.value[1:].lower(),
                list(myBook.active.columns)[3][1:]))
myIndex=0
for myCell in list(myBook.active.columns)[3][1:]:
    myCell.value=myList[myIndex]
    myIndex+=1
myBook.save('结果表-员工表.xlsx')
