# 毎日の測定データは正弦波かどうかを確認するプログラムである。

import os
import openpyxl

floder = 'C:/Users/zyxx/Downloads/11月-20221114T072437Z-001/11月/'
file_name = '2022-11-12-n.csv'
csv_file = floder + file_name

# 1.先にcsvファイルとxlsxファイルの有無を確認する

# ----------------------------------------

# 2.次にデータの番号（xlsxの何番目にある）を確認する
data = []
with open(csv_file) as f:
    for row in f:
        data.append(row)

data_adress = []
check = 0
start_point = 0

for i in range(data.__len__()):
    if 'ch0' in data[i]:
        start_point = i +2
        if check == 0:
            start_check = 1
    if 'henkoudo' in data[i]:
        check = 0
        data_adress.append([start_point,i])
# ------------------------------------------


# 3.最後グラフを作って保存する
# ------------------------------------------
print(data_adress)