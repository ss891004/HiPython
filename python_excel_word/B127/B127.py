import docx
myDocument=docx.Document('散文名篇.docx')
#获取Word文件(myDocument)的第2个段落的第1个块(myRun)
myRun=myDocument.paragraphs[1].runs[0]
# for myStyle in  myDocument.styles:
#     print(myStyle.name)
#使用“Intense Emphasis(明显强调)”样式设置第1个块(myRun)的样式
myRun.style=myDocument.styles['Intense Emphasis']
myDocument.save('我的Word文件-散文名篇.docx')
