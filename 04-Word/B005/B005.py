import docx
myDocument=docx.Document('长寿湖简介.docx')
#循环Word文件(myDocument)的段落(myParagraph)
for myParagraph in  myDocument.paragraphs:
    #获取段落(myParagraph)的文本(myText)
    myText=myParagraph.text
    #在文本(myText)中将'长寿湖'替换为'长寿湖景区'
    myText=myText.replace('长寿湖','长寿湖景区')
    #使用替换之后的文本(myText)设置该段落
    myParagraph.text=myText
myDocument.save('我的Word文件-长寿湖简介.docx')
