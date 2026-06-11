import docx
myDocument=docx.Document('销量榜.docx')
#获取Word文件(myDocument)的第1个表格(myTable)
myTable=myDocument.tables[0]
#自定义第1个表格(myTable)的字体类型
myTable.style.font.name='Microsoft YaHei UI'
#自定义第1个表格(myTable)的字体大小
myTable.style.font.size=docx.shared.Inches(0.18)
myDocument.save('我的Word文件-销量榜.docx')
