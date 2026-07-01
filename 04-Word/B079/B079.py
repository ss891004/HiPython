import docx
myDocument=docx.Document('快捷键.docx')
myTable=myDocument.tables[0]
myTable.rows[0].height=docx.shared.Inches(0.5)
# myTable.rows[1].height=docx.shared.Inches(0.5)
myDocument.save('我的Word文件-快捷键.docx')
