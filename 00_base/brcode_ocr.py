import os

def get_jpg():
    jpgs = []
    path = os.getcwd()
    for i in os.listdir(path):  #获取文件列表
        if i.split(".")[-1] == "jpg":  #筛选jpg文件（截图）
            oldname=os.path.join(path,i)  #旧文件名
            i = i.replace('微信图片_','')
            newname=os.path.join(path,i)  #新文件名
            os.rename(oldname,newname)  #改名
            jpgs.append(i)
    return jpgs

# 识别条形码
# pyzbar
# pip3 install opencv-python
import pyzbar.pyzbar as pyzbar
import cv2

def get_barcode(img):
    image = cv2.imread(img)
    barcodes = pyzbar.decode(image)
    barcode = barcodes[0]
    barcode_data = barcode.data.decode("utf-8")
    return barcode_data


if __name__ =="__main__ ":   
    jpgs = get_jpg()
    data_m = []
    for i in jpgs:
        data = get_barcode(i)
        data_m.append(data)
    data_m