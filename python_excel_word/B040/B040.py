import docx
myDocument=docx.Document('春江花月夜.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in myDocument.paragraphs:
  #循环段落(myParagraph)的块(myRun)
  for myRun in  myParagraph.runs:
     #设置块(myRun)的字体类型
     myRun.font.name='隶书'
     #myRun.font.element.rPr.rFonts.set(docx.oxml.ns.qn('w:eastAsia'),'楷体')
     myRun.font.element.rPr.rFonts.set(docx.oxml.ns.qn('w:eastAsia'),'隶书')
     #设置块(myRun)的字体大小
     myRun.font.size=docx.shared.Pt(16)
myDocument.save('我的Word文件-春江花月夜.docx')
