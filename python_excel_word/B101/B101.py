import docx
myDocument=docx.Document('宋词名篇.docx')
#获取Word文件(myDocument)的第2个段落的第1个块(myRun)
myRun=myDocument.paragraphs[1].runs[0]
#print(myRun.text)
#在第1个块(myRun)之后添加行中断(break)
myRun.add_break()
myDocument.save('我的Word文件-宋词名篇.docx')
