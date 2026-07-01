import docx
myDocument=docx.Document('快捷键.docx')
myTable=myDocument.tables[0]
myTable.style='Table Grid'
# myTable.style='Colorful Grid Accent 1'
myDocument.save('我的Word文件-快捷键.docx')
