import docx
myDocument=docx.Document('水调歌头.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in myDocument.paragraphs:
   #循环段落(myParagraph)的块(myRun)
   for myRun in myParagraph.runs:
       #在块(myRun)的文本底部添加下划线
       myRun.underline=True
myDocument.save('我的Word文件-水调歌头.docx')
