import docx
myDocument=docx.Document('散文名篇.docx')
#获取Word文件(myDocument)的第2个段落的第1个块(myRun)
myRun=myDocument.paragraphs[1].runs[0]
#设置第1个块(myRun)的文本以斜体风格显示
myRun.italic=True
#设置第1个块(myRun)的文本以粗体风格显示
myRun.bold=True
myDocument.save('我的Word文件-散文名篇.docx')
