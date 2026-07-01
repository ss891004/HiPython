import docx
myDocument=docx.Document('散文名篇.docx')
#删除Word文件(myDocument)的指定样式['Body Text 3']
myDocument.styles['Body Text 3'].delete()
myDocument.save('我的Word文件-散文名篇.docx')
