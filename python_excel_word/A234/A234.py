import openpyxl
myBook=openpyxl.load_workbook('收入表.xlsx')
mySheet=myBook.active
#在收入表(mySheet)的末尾添加新行
mySheet.append({'C':'3季度','D':496008,'E':168123,'F':1246})
mySheet.append({'C':'4季度','D':120234,'E':499028,'F':118896})
myBook.save('结果表-收入表.xlsx')
