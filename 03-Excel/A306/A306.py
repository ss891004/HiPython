import openpyxl
#读取“录取表.xlsx”文件
myBook=openpyxl.load_workbook('录取表.xlsx')
mySheet=myBook['录取表']
#按行获取录取表(mySheet)的单元格数据(myRange)
myRange=list(mySheet.values)
#根据录取表(mySheet)创建(复制)新录取表(myNewSheet)
myNewSheet=myBook.copy_worksheet(mySheet)
myNewSheet.title='新录取表'
#删除新录取表(myNewSheet)第3行之后的行(即删除所有考生)
while myNewSheet.max_row>3:
      myNewSheet.delete_rows(4)
#从myRange的第4行开始，先排序再循环,
#然后在新录取表(myNewSheet)中添加经过升序排列的考生
for myRow in sorted(myRange[3:]):
    myNewSheet.append(myRow)
#保存工作簿(myBook)，即保存“结果表-录取表.xlsx”文件
myBook.save('结果表-录取表.xlsx ')
