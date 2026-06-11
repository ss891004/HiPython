import docx
myDocument=docx.Document('雨霖铃.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in  myDocument.paragraphs:
    #循环段落(myParagraph)的块(myRun)
    for myRun in myParagraph.runs:
        #创建spacing元素(mySpacing)
        mySpacing=docx.oxml.shared.OxmlElement('w:spacing')
        #设置spacing元素(mySpacing)的字符间距
        mySpacing.set(docx.oxml.ns.qn('w:val'),'50')
        #在块(myRun)中应用(添加)新的字符间距
        myRun.element.rPr.append(mySpacing)
myDocument.save('我的Word文件-雨霖铃.docx')
