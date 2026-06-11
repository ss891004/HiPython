import openpyxl
myBook=openpyxl.Workbook()
mySheet=myBook.active
mySheet.title='九九表'
#表示从1循环到9
for x in range(1,10):
    #表示从1循环到x
    for y in range(1,x+1):
        #在单元格中写入口诀数据
        mySheet.cell(x,y,'%d×%d=%d'%(y,x,x*y))
myBook.save('结果表-九九乘法表.xlsx')
