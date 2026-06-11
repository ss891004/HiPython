import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
#从员工表(mySheet)的第2行开始逐行循环(到最后一行)
for myRow in list(mySheet.rows)[1:]:
    for myCell in myRow:
        #在单元格(myCell)中使用‘巴南区’替换‘巴县’
        myCell.value=myCell.value.replace('巴县','巴南区')
        #在单元格(myCell)中使用‘渝北区’替换‘江北县’
        myCell.value=myCell.value.replace('江北县','渝北区')
myBook.save('结果表-员工表.xlsx')
