import docx
myDocument=docx.Document('快捷键.docx')
myTable=myDocument.tables[0]
myRow=myTable.rows[2]
myRow._element.getparent().remove(myRow._element)
myDocument.save('我的Word文件-快捷键.docx')
