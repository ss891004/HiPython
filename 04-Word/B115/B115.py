import docx
#根据元素和属性创建对应的集合(批量设置元素属性)
def createElementsWithAttr(elements,attrs):
 myElements=[]
 for element in elements:
     myElement=docx.oxml.shared.OxmlElement(element)
     for attr in attrs:
         myElement.set(docx.oxml.ns.qn(attr),attrs[attr])
     myElements.append(myElement)
 return myElements
myDocument=docx.Document('背诵名篇.docx')
myParagraphs=myDocument.paragraphs
for myParagraph in myParagraphs:
    myInnerSectPr=myParagraph._element.pPr.sectPr
    if(myInnerSectPr is not None):
        #创建pgBorders元素
        myInnerPgBorders=docx.oxml.shared.OxmlElement('w:pgBorders')
        #设置该元素的w:offsetFrom属性
        myInnerPgBorders.set(docx.oxml.ns.qn('w:offsetFrom'),'page')
        #设置子元素名称列表
        myInnerElements=['w:top','w:left','w:bottom','w:right']
        #设置子元素所对应的属性
        myInnerAttrs={'w:val':'double','w:sz':'4',
                                       'w:space':'24','w:color':'ff0000'}
        #根据元素和属性创建对应的集合
        myInnerElements=createElementsWithAttr(myInnerElements,myInnerAttrs)
        #通过循环操作将元素批量插入至pgBorders节点
        for myInnerElement in myInnerElements:
            myInnerPgBorders.append(myInnerElement)
        #将pgBorders插入至sectPr节点
        myInnerSectPr.append(myInnerPgBorders)
#获取sectPr节点(处理最后的章节)
mySectPr=myDocument._element.body.sectPr
#创建pgBorders元素
myPgBorders=docx.oxml.shared.OxmlElement('w:pgBorders')
#设置该元素的w:offsetFrom属性
myPgBorders.set(docx.oxml.ns.qn('w:offsetFrom'),'page')
#设置子元素名称列表
myElements=['w:top','w:left','w:bottom','w:right']
#设置子元素对应的属性
myAttrs={'w:val':'double','w:sz':'4','w:space':'24','w:color':'ff0000'}
#根据元素和属性创建对应的集合
myElements=createElementsWithAttr(myElements,myAttrs)
#通过循环操作插入pgBorders节点
for myElement in myElements:
    myPgBorders.append(myElement)
#将pgBorders插入至sectPr节点
mySectPr.append(myPgBorders)
myDocument.save('我的Word文件-背诵名篇.docx')
