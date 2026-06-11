import docx
myDocument=docx.Document('快捷键.docx')
myTable=myDocument.tables[0]
myTable.alignment=docx.enum.table.WD_TABLE_ALIGNMENT.CENTER
myDocument.save('我的Word文件-快捷键.docx')
