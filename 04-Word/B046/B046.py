import docx
myDocument=docx.Document('散文名篇.docx')
#循环Word文件(myDocument)的第2个段落的块(myRun)
for myRun in myDocument.paragraphs[1].runs:
   #print(myRun.text)
   if '然而，事实上是乔对英国的语言理解得还不够透彻。' in myRun.text:
      #隐藏块(myRun)
      myRun.font.hidden=True
myDocument.save('我的Word文件-散文名篇.docx')
