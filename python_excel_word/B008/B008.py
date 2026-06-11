import docx
myDocument=docx.Document('散文名篇.docx')
myDocument.paragraphs[0].paragraph_format.line_spacing=docx.shared.Inches(0.5)
myDocument.save('我的Word文件-散文名篇.docx')
