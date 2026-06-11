import docx
myDocument=docx.Document('新员工.docx')
#获取Word文件(myDocument)的第1个表格(myTable)
myTable=myDocument.tables[0]
#循环第1个表格(myTable)的行(myRow)
for myRow in myTable.rows:
    #循环行(myRow)的单元格(myCell)
    for myCell in myRow.cells:
        #如果单元格(myCell)的文本包含'投资'
        if '投资' in myCell.text:
            #则删除行(myRow)
            myRow._element.getparent().remove(myRow._element)
            #然后跳出该行，执行下一行的循环
            break
myDocument.save('我的Word文件-新员工.docx')
