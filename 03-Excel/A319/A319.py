import openpyxl
myBook=openpyxl.load_workbook('员工表.xlsx',data_only=True)
mySheet=myBook.active
for myRow in range(mySheet.max_row,1,-1):
    #获取员工的工资等级(myRank)
    myRank=mySheet[myRow][6].value
    myMark='★'
    #使用星号个数代表员工的工资等级(myRank)
    mySheet[myRow][6].value=myMark*myRank
myBook.save('结果表-员工表.xlsx')
