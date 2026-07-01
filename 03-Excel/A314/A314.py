import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#循环收入表(mySheet)的1-4列
for myCol in range(1,5):
    #如果myCol是偶数
    if myCol%2==0:
       #将数字列号转换为字母列号
       myColLetter=openpyxl.utils.get_column_letter(myCol)
       #循环偶数列的5-8行
       for myRow in range(5,9):
           #清空偶数列的5-8行的所有单元格数据，如mySheet['D6']=''
           mySheet[myColLetter+str(myRow)]=''
myBook.save('结果表-收入表.xlsx')
