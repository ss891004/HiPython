import docx
myDocument=docx.Document('背诵名篇.docx')
#获取Word文件(myDocument的第1节(注意：从第0节开始)
mySection1=myDocument.sections[1]
#设置第1节(mySection1)的左边距
mySection1.left_margin=docx.shared.Cm(7)
#设置第1节(mySection1)的右边距
mySection1.right_margin=docx.shared.Cm(7)
# #设置第1节(mySection1)的上边距
# mySection1.top_margin=docx.shared.Cm(10)
# #设置第1节(mySection1)的下边距
# mySection1.bottom_margin=docx.shared.Cm(10)
myDocument.save('我的Word文件-背诵名篇.docx')
