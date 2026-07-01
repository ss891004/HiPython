import docx
myDocument=docx.Document('新员工.docx')
#获取Word文件(myDocument)的第1个表格(myTable)
myTable=myDocument.tables[0]
#循环第1个表格(myTable)的列(myColumn)
for myColumn in myTable.columns:
     #如果列(myColumn)的标题包含'最高'
     if '最高' in myColumn.cells[0].text:
            #则删除列(myColumn)的所有单元格(即删除该列)
            for myCell in myColumn.cells:
                myCell._element.getparent().remove(myCell._element)
myDocument.save('我的Word文件-新员工.docx')
