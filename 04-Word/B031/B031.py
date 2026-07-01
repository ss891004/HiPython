import docx
myDocument=docx.Document('智慧书.docx')
myDocument.paragraphs[2].paragraph_format.page_break_before=True
myDocument.save('我的Word文件-智慧书.docx')
