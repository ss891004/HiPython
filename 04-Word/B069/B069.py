import docx
myDocument=docx.Document('哈佛大学简介.docx')
#在Word文件(myDocument)的末尾添加指定的图像
myImage=myDocument.add_picture('myimage.jpg')
myDocument.save('我的Word文件-哈佛大学简介.docx')
