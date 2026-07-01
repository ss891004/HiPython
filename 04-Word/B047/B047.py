import docx
myDocument=docx.Document('散文名篇.docx')
#在第1个段落的末尾添加新块myRun0
myRun0=myDocument.paragraphs[0].add_run("Did Joe's sons become slaves to the digging? No, they were inspired because they had visions of what money could do for them and did not focus on the money itself. ")
#使用红色设置新块(myRun0)的文本颜色
myRun0.font.color.rgb=docx.shared.RGBColor(255,55,55)
#在第2个段落的末尾添加新块myRun1
myRun1=myDocument.paragraphs[1].add_run("乔的儿子们成为挖掘土地的奴隶了吗?不，他们只是一昧地幻想着金钱能为他们做什么，并被无数个幻想所激励，但从未考虑过获取金钱的正确途径。")
#使用红色设置新块(myRun1)的文本颜色
myRun1.font.color.rgb=docx.shared.RGBColor(255,55,55)
myDocument.save('我的Word文件-散文名篇.docx')
