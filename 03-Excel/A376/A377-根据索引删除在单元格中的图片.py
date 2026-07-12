
import openpyxl
myBook=openpyxl.load_workbook('结果表-新书订购表.xlsx')
mySheet=myBook.active
#根据指定的索引删除在新书订购表中的图像
del mySheet._images[1]
myBook.save('结果表-新书订购表2.xlsx')
