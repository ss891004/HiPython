import docx
myDocument=docx.Document('背诵名篇.docx')
#创建background元素
myBackground=docx.oxml.shared.OxmlElement('w:background')
#设置该元素的color属性值为指定颜色E0E0E0
myBackground.set(docx.oxml.ns.qn('w:color'),'E0E0E0')
#在Word文件(myDocument)中添加background元素
myDocument.element.append(myBackground)
myDocument.save('我的Word文件-背诵名篇.docx')
