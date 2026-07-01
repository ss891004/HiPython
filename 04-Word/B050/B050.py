import docx
myDocument=docx.Document('雨霖铃.docx')
#循环Word文件(myDocument)的第2个段落的块(myRun)
for myRun in myDocument.paragraphs[1].runs:
    #在块(myRun)的文本底部添加波浪线
    myRun.font.underline=docx.enum.text.WD_UNDERLINE.WAVY
    ##在块(myRun)的文本底部添加双波浪线
    #myRun.font.underline=docx.enum.text.WD_UNDERLINE.WAVY_DOUBLE
myDocument.save('我的Word文件-雨霖铃.docx')
