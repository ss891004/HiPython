import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#按行获取员工表(mySheet)的单元格数据(第1行除外)
myRows=list(mySheet.values)[1:]
#在员工表(mySheet)中删除所有行(第1行除外)
while mySheet.max_row>1:
      mySheet.delete_rows(2)
#从myRows的第1行开始，根据间隔行数(1行)正序筛选所有行
for myRow in myRows[::2]:
    #在员工表(mySheet)中添加正序筛选的行
    mySheet.append(myRow)
myBook.save('结果表-员工表.xlsx')
