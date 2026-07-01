import docx
myDocument=docx.Document('智慧书.docx')
myDocument.paragraphs[1].paragraph_format.keep_with_next=True
myDocument.save('我的Word文件-智慧书.docx')
