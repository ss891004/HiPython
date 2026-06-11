import docx
myDocument=docx.Document('散文名篇.docx')
# for myParagraph in myDocument.paragraphs:
#     print(myParagraph.style.name)
#设置该Word文件的Normal样式的字体为“宋体”
myDocument.styles['Normal'].font.name='宋体'
myDocument.styles['Normal']._element.rPr.rFonts.set(
                               docx.oxml.ns.qn('w:eastAsia'),'宋体')
myDocument.save('我的Word文件-散文名篇.docx')
