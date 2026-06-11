import docx
myDocument=docx.Document('李清照名篇.docx')
#循环Word文件(myDocument)的第2个段落的块(myRun)
for myRun in myDocument.paragraphs[1].runs:
    #在块(myRun)的文本底部添加点线
    myRun.font.underline=docx.enum.text.WD_UNDERLINE.DOTTED
myDocument.save('我的Word文件-李清照名篇.docx')
