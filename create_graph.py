# csvファイルからグラフを作るプログラムである
# 測定できなかった場合の対策も重要
# pandasを使うか？

import os

# import pandas as pd
# check the start
# 'sizen(LUX)'

# check the end
# 'main(LUX)' in

write_permission = False

file_path = 'C:/Users/zyxx/Desktop/'
file_data = '2022-10-26'
file_name = file_data+'-n.csv'
csv_file = file_path + file_name

csv_list = []

# csvファイルをリストとして保存する(行数が多すぎないように)
with open(csv_file, 'r') as f:
    for row in f:
        csv_list.append(row)

# len(csv_list)　リスト csv_list の要素数
print(csv_list.__len__())

for i in range(csv_list.__len__()):
    print(csv_list[i])
# データ記録できた場合

# データ記録できなかった場合

