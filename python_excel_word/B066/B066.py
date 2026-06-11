import docx
#创建自定义函数实现超链接功能
def addHyperlink(paragraph,url,text):
    myPart=paragraph.part
    myID=myPart.relate_to(url,
            docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    myHyperlink=docx.oxml.shared.OxmlElement('w:hyperlink')
    myHyperlink.set(docx.oxml.shared.qn('r:id'),myID)
    myRun=docx.oxml.shared.OxmlElement('w:r')
    #在超链接文本底部添加下划线(波浪线)
    rPr=docx.oxml.shared.OxmlElement('w:rPr')
    u=docx.oxml.shared.OxmlElement('w:u')
    u.set(docx.oxml.shared.qn('w:val'),'wave')
    rPr.append(u)
    #使用红色设置超链接的文本和下划线(波浪线)的颜色
    c=docx.oxml.shared.OxmlElement('w:color')
    c.set(docx.oxml.shared.qn('w:val'),'ff0000')
    rPr.append(c)
    myRun.append(rPr)
    myRun.text=text
    myHyperlink.append(myRun)
    paragraph._p.append(myHyperlink)
myDocument=docx.Document('苏轼简介.docx')
#获取Word文件(myDocument)的第2个段落(myParagraph)
myParagraph=myDocument.paragraphs[1]
#在第2个段落(myParagraph)的末尾添加超链接'使用百度搜索了解更多内容。'
addHyperlink(myParagraph,'https://www.baidu.com','使用百度搜索了解更多内容。')
myDocument.save('我的Word文件-苏轼简介.docx')
