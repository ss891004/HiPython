#导入openpyxl库
import openpyxl as myOpenpyxl

#设置分公司名称列表(myNames)
myNames=['北京分公司','上海分公司','深圳分公司','西安分公司',
         '沈阳分公司','重庆分公司','武汉分公司']
#根据“利润表.xlsx”文件创建工作簿(myBook)
myBook=myOpenpyxl.load_workbook('利润表.xlsx')

i=0
#在while循环中批量创建与“利润表.xlsx”内容完全相同的Excel文件
while i<len(myNames):
      #根据分公司名称设置各个Excel文件的名称
      myPath='结果表-'+myNames[i]+'2020年度利润表.xlsx'
      i+=1
      #保存工作簿(myBook)或者说将工作簿(myBook)另存为Excel文件
      myBook.save(myPath)
