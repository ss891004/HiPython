import docx
myDocument=docx.Document('散文名篇.docx')
#循环Word文件(myDocument)的第2个段落的块(myRun)
for myRun in myDocument.paragraphs[1].runs:
    #在块(myRun)的文本底部添加下划线
    myRun.font.underline=True
    #设置块(myRun)的下划线颜色为红色
    myRun.element.rPr.u.set(docx.oxml.ns.qn('w:color'),'ff0000')
    # # 设置块(myRun)的下划线颜色为黑色
    # myRun.element.rPr.u.set(docx.oxml.ns.qn('w:color'),'000000')
myDocument.save('我的Word文件-散文名篇.docx')
