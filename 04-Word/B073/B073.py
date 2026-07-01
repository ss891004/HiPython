import docx
myDocument=docx.Document('散文名篇.docx')
#获取Word文件(myDocument)的第2个段落的第1个块(myRun)
myRun=myDocument.paragraphs[1].runs[0]
#设置第1个块(myRun)的字体颜色为红色
#myRun.font.color.rgb=docx.shared.RGBColor(255,55,55)
#使用主题颜色设置第1个块(myRun)的字体颜色
myRun.font.color.theme_color=docx.enum.dml.MSO_THEME_COLOR.ACCENT_6
#myRun.font.color.theme_color=docx.enum.dml.MSO_THEME_COLOR.ACCENT_4
myDocument.save('我的Word文件-散文名篇.docx')
