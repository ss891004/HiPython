import docx
myDocument=docx.Document('水调歌头.docx')
#循环Word文件(myDocument)正文的第1个段落的块(myRun)
for myRun in myDocument.paragraphs[1].runs:
    #为块(myRun)的每个字符添加独立的下划线
    myRun.underline=docx.enum.text.WD_UNDERLINE.WORDS
#循环Word文件(myDocument)正文的第2个段落的块(myRun)
for myRun in myDocument.paragraphs[2].runs:
    #为块(myRun)的字符添加普通下划线
    myRun.underline=True
myDocument.save('我的Word文件-水调歌头.docx')
