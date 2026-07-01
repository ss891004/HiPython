import docx
myDocument=docx.Document('快捷键.docx')
myData=[['功能说明','Windows','Mac OS'],
        ['编辑菜单','Alt+E','Ctrl+F2+F'],
        ['文件菜单','Alt+F','Ctrl+F2+E'],
        ['视图菜单','Alt+V','Ctrl+F2+V']]
#在Word文件(myDocument)中根据行数、列数和样式创建表格
myTable=myDocument.add_table(rows=4,cols=3,style='Table Grid')
#在单元格中写入数据(文本)
for i in range(len(myData)):
    for j in range(len(myData[i])):
        myTable.rows[i].cells[j].text=myData[i][j]
myDocument.save('我的Word文件-快捷键.docx')
