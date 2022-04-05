
import csv

## 生产csv 和excel 的集中方法

def  write_csv_file():
    with open("my.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "predict", "score"])
        row = [['1', 1, 1], ['2', 2, 2], ['3', 3, 3]]
        for r in row:
            writer.writerow(r)



import openpyxl as xl
import os


def write_excel_file(folder_path):
    result_path = os.path.join(folder_path, "my.xlsx")
    print(result_path)
    print('***** 开始写入excel文件 ' + result_path + ' ***** \n')
    if os.path.exists(result_path):
        print('***** excel已存在，在表后添加数据 ' + result_path + ' ***** \n')
        workbook = xl.load_workbook(result_path)
    else:
        print('***** excel不存在，创建excel ' + result_path + ' ***** \n')
        workbook = xl.Workbook()
        workbook.save(result_path)
    sheet = workbook.active
    headers = ["URL", "predict", "score"]
    sheet.append(headers)
    result = [['1', 1, 1], ['2', 2, 2], ['3', 3, 3]]
    for data in result:
        sheet.append(data)
    workbook.save(result_path)
    print('***** 生成Excel文件 ' + result_path + ' ***** \n')


def write_excel_pandas():
    import pandas as pd
    result_list = [['1', 1, 1], ['2', 2, 2], ['3', 3, 3]]
    columns = ["URL", "predict", "score"]
    dt = pd.DataFrame(result_list, columns=columns)
    dt.to_excel("result_xlsx.xlsx", index=0)
    dt.to_csv("result_csv.csv", index=0)




if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # write_excel_file(BASE_DIR)
    write_excel_pandas()


