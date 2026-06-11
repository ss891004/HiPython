import openpyxl
myBook=openpyxl.load_workbook('录取表.xlsx')
mySheet=myBook['录取表']
myRange=list(mySheet.values)
myNewSheet=myBook.copy_worksheet(mySheet)
myNewSheet.title='新录取表'
while myNewSheet.max_row>3:
      myNewSheet.delete_rows(4)
#从myRange的第4行开始，先根据总分列对行进行升序排列，然后再循环
for myRow in sorted(myRange[3:],key=lambda x:x[3]):
    #在新录取表(myNewSheet)中添加经过升序排列的考生
    myNewSheet.append(myRow)
myBook.save('结果表-录取表.xlsx')
