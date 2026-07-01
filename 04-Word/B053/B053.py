import docx
myDocument=docx.Document('李清照名篇.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in myDocument.paragraphs:
    #循环段落(myParagraph)的块(myRun)
    for myRun in myParagraph.runs:
        #在块(myRun)的文本底部添加点划线
        myRun.font.underline=docx.enum.text.WD_UNDERLINE.DOT_DASH
myDocument.save('我的Word文件-李清照名篇.docx')
