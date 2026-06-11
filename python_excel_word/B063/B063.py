import docx
myDocument=docx.Document('苏轼名篇.docx')
#获取Word文件(myDocument)正文的第1个段落(myParagraph)
myParagraph=myDocument.paragraphs[1]
#创建em元素myEmphasize
myEmphasize=docx.oxml.shared.OxmlElement('w:em')
# 设置myEmphasize的着重号类型为小圆点
myEmphasize.set(docx.oxml.ns.qn('w:val'),'dot')
#循环段落(myParagraph)的块(myRun)
for myRun in myParagraph.runs:
    #在块(myRun)的文本中应用myEmphasize着重号(小圆点)
    myRun.element.rPr.append(myEmphasize)
myDocument.save('我的Word文件-苏轼名篇.docx')
