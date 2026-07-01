import docx
myDocument=docx.Document('散文名篇.docx')
#循环Word文件(myDocument)的第2个段落的块(myRun)
for myRun in myDocument.paragraphs[1].runs:
    #设置块(myRun)的字体颜色为红色
    myRun.font.color.rgb=docx.shared.RGBColor(255,55,55)
    # #设置块(myRun)的字体颜色为绿色
    # myRun.font.color.rgb=docx.shared.RGBColor(55,255,55)
myDocument.save('我的Word文件-散文名篇.docx')
