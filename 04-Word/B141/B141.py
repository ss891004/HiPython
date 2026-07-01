#导入python-docx库
import docx
#导入正则表达式
import re
#根据Word文件“样式范例.docx”创建myDocument
myDocument=docx.Document('样式范例.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in myDocument.paragraphs:
    #如果段落(myParagraph)的样式名称包含Heading,则删除该段落
    if re.match("^Heading [1-3]",myParagraph.style.name):
       myElement=myParagraph._element
       myElement.getparent().remove(myElement)
#将Word文件(myParagraph)保存为“我的Word文件-样式范例.docx”
myDocument.save('我的Word文件-样式范例.docx')
