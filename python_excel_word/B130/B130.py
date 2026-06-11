import docx
myDocument=docx.Document('散文名篇.docx')
myDocument.paragraphs[0].runs[0].font.small_caps=True
myDocument.save('我的Word文件-散文名篇.docx')
