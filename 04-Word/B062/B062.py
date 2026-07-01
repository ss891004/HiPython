import docx
myDocument=docx.Document('苏轼名篇.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in  myDocument.paragraphs:
    #循环段落(myParagraph)的块(myRun)
    for myRun in myParagraph.runs:
        #创建bdr元素(myBorder)
        myBorder=docx.oxml.shared.OxmlElement('w:bdr')
        #设置线框(myBorder)颜色为红色
        myBorder.set(docx.oxml.ns.qn('w:color'),'ff0000')
        # # 设置线框(myBorder)颜色为黑色
        # myBorder.set(docx.oxml.ns.qn('w:color'),'000000')
        # # 设置线框(myBorder)颜色为蓝色
        # myBorder.set(docx.oxml.ns.qn('w:color'),'0000ff')
        #设置线框(myBorder)类型为单细实线
        myBorder.set(docx.oxml.ns.qn('w:val'),'single')
        # # 设置线框(myBorder)类型为双细实线
        # myBorder.set(docx.oxml.ns.qn('w:val'),'double')
        # # 设置线框(myBorder)类型为点线
        # myBorder.set(docx.oxml.ns.qn('w:val'),'dotted')
        # 将线框(myBorder)应用于块(myRun)的文本
        myRun.element.rPr.append(myBorder)
myDocument.save('我的Word文件-苏轼名篇.docx')
