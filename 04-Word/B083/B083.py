import docx
myDocument=docx.Document('快捷键.docx')
myTable=myDocument.tables[0]
myColumn=myTable.columns[1]
for myCell in myColumn.cells:
    myCell._element.getparent().remove(myCell._element)
myDocument.save('我的Word文件-快捷键.docx')
