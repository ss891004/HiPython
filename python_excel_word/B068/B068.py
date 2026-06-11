import docx
myDocument=docx.Document('折扣商品.docx')
#获取Word文件(myDocument)的所有图像,并以独立文件形式将每个图像保存在当前目录中
for myShape in myDocument.inline_shapes:
    myBlip=myShape._inline.graphic.graphicData.pic.blipFill.blip
    myID=myBlip.embed
    myImage=myDocument.part.related_parts[myID]
    myFile=open(myID+".jpg", "wb")
    myFile.write(myImage._blob)
    myFile.close()
