import docx
myDocument=docx.Document('雨霖铃.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in  myDocument.paragraphs:
    #循环段落(myParagraph)的块(myRun)
    for myRun in myParagraph.runs:
        #创建w元素
        myW=docx.oxml.shared.OxmlElement('w:w')
        #使用w元素设置扁平拉伸值(默认值为100，即100%)
        myW.set(docx.oxml.ns.qn('w:val'),'200')
        #在块(myRun)中应用(添加)新的字符扁平拉伸效果
        myRun.element.rPr.append(myW)
myDocument.save('我的Word文件-雨霖铃.docx')
