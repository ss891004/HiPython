import docx
myDocument=docx.Document('打折商品.docx')
#获取Word文件(myDocument)的第1节(注意：从第0节开始)
mySection1=myDocument.sections[1]
#设置第1节的页眉与页面上边缘的距离(0距离即为页面上边缘)
mySection1.header_distance=docx.shared.Cm(0)
# #如果该属性值等于页面上边距，则页眉从上方进入正文
# mySection1.header_distance=mySection1.top_margin
# #如果该属性值过大，则挤压正文
# mySection1.header_distance=docx.shared.Cm(10)
myDocument.save('我的Word文件-打折商品.docx')
