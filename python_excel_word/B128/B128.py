import docx
myDocument=docx.Document('苏轼名篇.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in myDocument.paragraphs:
    #循环段落(myParagraph)的块(myRun)
    for myRun in myParagraph.runs:
        #以雕刻效果显示块(myRun)的文本
        myRun.font.imprint=True
myDocument.save('我的Word文件-苏轼名篇.docx')
