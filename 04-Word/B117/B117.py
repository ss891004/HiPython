import docx
myDocument=docx.Document('背诵名篇.docx')
#获取Word文件(myDocument)的第3节(注意：从第0节开始)
mySection=myDocument.sections[3]
#强制第3节从奇数页开始
mySection.start_type=docx.enum.section.WD_SECTION.ODD_PAGE
myDocument.save('我的Word文件-背诵名篇.docx')
