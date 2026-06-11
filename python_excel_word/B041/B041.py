import docx
myDocument=docx.Document('春江花月夜.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in myDocument.paragraphs:
    #循环段落(myParagraph)的块(myRun)
    for myRun in myParagraph.runs:
        #设置块(myRun)的文本显示轮廓线(即镂空效果)
        myRun.font.outline=True
myDocument.save('我的Word文件-春江花月夜.docx')
