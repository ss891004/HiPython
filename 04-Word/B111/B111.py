import docx
myDocument=docx.Document('背诵名篇.docx')
#获取Word文件(myDocument)的第1节(注意：从第0节开始)
mySection1=myDocument.sections[1]
#设置第1节(mySection1)的页面宽度
mySection1.page_width=docx.shared.Cm(14)
#设置第1节(mySection1)的页面高度
mySection1.page_height=docx.shared.Cm(20.3)
#以厘米为单位获取页面的宽度和高度
#print(mySection1.page_width.cm)
#print(mySection1.page_height.cm)
myDocument.save('我的Word文件-背诵名篇.docx')
