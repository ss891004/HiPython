import docx
#自定义批量设置元素属性的函数
def setAttrs(rootElement,elements,attrs):
  for element in elements:
     myElement=rootElement.find(docx.oxml.ns.qn(element))
     if myElement is None:
        myElement=docx.oxml.OxmlElement(element)
        rootElement.append(myElement)
     for key in attrs:
        myElement.set(docx.oxml.ns.qn(key),attrs[key])
myDocument=docx.Document('新员工.docx')
#获取Word文件(myDocument)的第1个表格
myTable=myDocument.tables[0]
myTablePr=myTable._element.tblPr
#设置单元格的边框
#myElements=['w:top','w:left','w:bottom','w:right','w:insideH','w:insideV']
#设置表格的边框
myElements=['w:top','w:left','w:bottom','w:right']
# #设置表格的上下边框
# myElements=['w:top','w:bottom']
# #设置表格的左右边框
# myElements=['w:left','w:right']
#定义元素属性键值对
myAttrs={'w:val':'single','w:color':'000000','w:sz':'24'}
#遍历表格的所有行，自定义行的边框
for myRow in myTable.rows:
    myTr=myRow._element
    myTblPrEx=myRow._element.first_child_found_in("w:tblPrEx")
    if myTblPrEx is None:
       myTblPrEx=docx.oxml.OxmlElement('w:tblPrEx')
       myTr.append(myTblPrEx)
    myTblBorders=docx.oxml.OxmlElement('w:tblBorders')
    myTblPrEx.append(myTblBorders)
    setAttrs(myTblBorders,myElements,myAttrs)
myDocument.save('我的Word文件-新员工.docx')
