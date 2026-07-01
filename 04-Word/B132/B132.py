import docx
myDocument=docx.Document('世界杯.docx')
#设置分散对齐Word文件(myDocument)的第2个段落的4个图像
myDocument.paragraphs[1].alignment=\
          docx.enum.text.WD_ALIGN_PARAGRAPH.DISTRIBUTE
myDocument.save('我的Word文件-世界杯.docx')
