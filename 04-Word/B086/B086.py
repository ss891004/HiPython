import docx
myDocument=docx.Document('新员工.docx')
#获取Word文件(myDocument)的第1个表格(myTable)
myTable=myDocument.tables[0]
#在第1个表格(myTable)的右侧添加列(myColumn)
myColumn=myTable.add_column(docx.shared.Inches(1.2))
myItems=['最高学历','博士','硕士','硕士']
i=0
#设置列(myColumn)各个单元格的文本
for myCell in myColumn.cells:
    myCell.text=myItems[i]
    i+=1
myDocument.save('我的Word文件-新员工.docx')
