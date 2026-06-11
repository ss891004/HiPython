import docx
myDocument=docx.Document('散文名篇.docx')
myDocument.paragraphs[0].paragraph_format.alignment=\
                    docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
myDocument.save('我的Word文件-散文名篇.docx')
