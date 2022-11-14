# 毎日の測定データは正弦波かどうかを確認するプログラムである。

import os
import openpyxl
import csv
import create_graph as cg





floder = 'C://Users/qq914/Desktop/123/'

# すべてのcsvファイル名前をfile_listに入れる
file_list = []


for file in os.listdir(floder):
    if '.csv' in file:
        file_list.append(file)

for csv_name in file_list:
    wb = openpyxl.Workbook()
    ws = wb.active
    print(csv_name)
    csv_file = floder + csv_name
    xlsx_file = floder + csv_name.split('.')[0] + '.xlsx'
    with open(csv_file,'r') as f :
        for row in csv.reader(f):
            ws.append(row)

    data = []
    with open(csv_file) as f:
        for row in f:
            data.append(row)

    data_adress = []
    check = 0
    start_point = 0

    for i in range(data.__len__()):
        if 'ch0' in data[i]:
            start_point = i + 2
            if check == 0:
                start_check = 1
        if 'henkoudo' in data[i]:
            check = 0
            data_adress.append([start_point, i])

    for k in data_adress:
        for i in range(k[0], k[1] + 1):
            for j in range(1, 8):
                ws.cell(i, j).data_type = 'float'

    for k in data_adress:
        for i in range(1, 8):
            ws.cell(k[1] + 2, i).data_type = 'float'

    for i in range(36):
        ws.cell(i+3,8).value = i*5

    wb.save(xlsx_file)

    for k in data_adress:
        cg.create_scatter(xlsx_file,'Sheet','角度','照度','偏光','H'+str(k[0]),[8,3,8,39,2,k[0],2,k[1]])
        cg.create_scatter(xlsx_file,'Sheet','角度','照度','ch1 and ch2','O'+str(k[0]),[8,3,8,39,3,k[0],3,k[1]],[8,3,8,39,4,k[0],4,k[1]])
        cg.create_scatter(xlsx_file,'Sheet','角度','照度','lux1 and lux2','H'+str(k[0]+17),[8,3,8,39,5,k[0],5,k[1]],[8,3,8,39,6,k[0],6,k[1]])


# 直接転換しても行けると思う。
# 1.先にcsvファイルとxlsxファイルの有無を確認する。


# ----------------------------------------


# 2.次にデータの番号（xlsxの何番目にある）を確認する
# ------------------------------------------
print(data_adress)


# 3.最後グラフを作って保存する
# ------------------------------------------
# print(data_adress)