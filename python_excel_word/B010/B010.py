import docx
myDocument=docx.Document('散文名篇.docx')
myParagraph2=myDocument.paragraphs[1]
myParagraph2.paragraph_format.first_line_indent=docx.shared.Inches(2)
myDocument.save('我的Word文件-散文名篇.docx')
