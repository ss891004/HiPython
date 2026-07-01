import docx
myDocument=docx.Document('散文名篇.docx')
#设置Word文件(myDocument)的Normal样式的高亮颜色为紫色
myDocument.styles['Normal'].font.highlight_color=\
                            docx.enum.text.WD_COLOR_INDEX.PINK
myDocument.save('我的Word文件-散文名篇.docx')
