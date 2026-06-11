import docx
myDocument=docx.Document('散文名篇.docx')
#循环Word文件(myDocument)的第1个段落的块(myRun)
for myRun in myDocument.paragraphs[0].runs:
    #大写块(myRun)的所有字母
    myRun.font.all_caps=True
myDocument.save('我的Word文件-散文名篇.docx')
