import docx
myDocument=docx.Document('散文名篇.docx')
myParagraph2=myDocument.paragraphs[1]
#设置第2个段落左缩进1.5英寸
myParagraph2.paragraph_format.left_indent=docx.shared.Inches(1.5)
#设置第2个段落首行缩进-1.5英寸(特别注意：缩进值是负数)
myParagraph2.paragraph_format.first_line_indent=docx.shared.Inches(-1.5)
myDocument.save('我的Word文件-散文名篇.docx')
