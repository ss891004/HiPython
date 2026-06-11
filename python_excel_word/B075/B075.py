import docx
myDocument=docx.Document('快捷键.docx')
#获取Word文件(myDocument)的第1个表格(myTable)
myTable=myDocument.tables[0]
#在第1个表格(myTable)的末尾添加新行(myRow)
myRow=myTable.add_row();
#在新行(myRow)的第1个单元格中写入内容
myRow.cells[0].text='全选文本'
#在新行(myRow)的第2个单元格中写入内容
myRow.cells[1].text='Ctrl+A'
#在新行(myRow)的第3个单元格中写入内容
myRow.cells[2].text='Cmd+A'
myDocument.save('我的Word文件-快捷键.docx')
