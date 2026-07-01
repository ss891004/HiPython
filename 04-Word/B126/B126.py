import docx
myDocument=docx.Document('宋词名篇.docx')
#获取Word文件(myDocument)的第2个段落的第1个块(myRun)
myRun=myDocument.paragraphs[1].runs[0]
#print(myRun.text)
#在第1个块(myRun)之后添加页中断WD_BREAK.PAGE,
#即将同一段落的两个块拆分到两个页面
myRun.add_break(docx.enum.text.WD_BREAK.PAGE)
myDocument.save('我的Word文件-宋词名篇.docx')
