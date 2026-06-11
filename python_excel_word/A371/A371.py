import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx')
mySheet=myBook.active
myNames=['Mark','Daniel','Jack','Cindy','King','Ken','Nora','Ben']
myRow=2
for myName in myNames:
    #创建批注
    myComment=openpyxl.comments.Comment('英文名：'+myName,'')
    myComment.height=24
    #在指定的单元格(mySheet['C'+str(myRow)])上设置批注(myComment)
    mySheet['C'+str(myRow)].comment=myComment
    myRow+=1
myBook.save('结果表-员工表.xlsx')
