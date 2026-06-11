import docx
myDocument=docx.Document('快捷键.docx')
#获取Word文件(myDocument)的第2个表格
myTable1= myDocument.tables[1]._element
#删除Word文件(myDocument)的第2个表格
myTable1.getparent().remove(myTable1)
myDocument.save('我的Word文件-快捷键.docx')
