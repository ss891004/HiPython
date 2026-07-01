import docx
myDocument=docx.Document('背诵名篇.docx')
#获取Word文件(myDocument)的第3节(注意：从第0节开始)
mySection=myDocument.sections[3]
#允许第3节与前一节连在一起(即不开启新页)
mySection.start_type=docx.enum.section.WD_SECTION.CONTINUOUS
myDocument.save('我的Word文件-背诵名篇.docx')
