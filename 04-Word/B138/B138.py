import docx
myDocument=docx.Document('散文名篇.docx')
#设置Word文件(myDocument)的Normal样式的段落的首行缩进尺寸(2.5英寸)
myDocument.styles['Normal'].paragraph_format.\
                  first_line_indent=docx.shared.Inches(2.5)
myDocument.save('我的Word文件-散文名篇.docx')
