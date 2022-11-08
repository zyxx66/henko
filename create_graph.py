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

file_path = 'C:/Users/zyxx/Desktop/11月/'
file_data = '2022-11-06'
file_name = file_data + '-n.csv'
csv_file = file_path + file_name

csv_list = []

# csvファイルをリストとして保存する(行数が多すぎないように)
with open(csv_file, 'r') as f:
    for row in f:
        csv_list.append(row)

# len(csv_list)　リスト csv_list の要素数
# print(csv_list.__len__())

for i in range(csv_list.__len__()):
    if ':' in csv_list[i]:
        print(csv_list[i]) # 2022-11-05-06:00:02,,,0600\n
        time = csv_list[i].split(',')[0].split('-')[3].split('\n')[0] # 06:00:02
        time_s = csv_list[i].split(',')[3].split('\n')[0] # 0600
        time_split = time.split(':')
        print(int(time.split(':')[1]))
        # 30分の時
        if int(time_split[1]) == 30:
            pass
            csv_list[i] = csv_list[i].replace('30','00')
            time_hour = int(time_split[0]) + 3
            csv_list[i] = csv_list[i].replace(time_split[0], str(time_hour))
        # 00分の時
        elif int(time_split[1]) == 0:

            pass
            csv_list[i] = csv_list[i].replace('00','30')
            time_hour = int(time_split[0]) + 2
            csv_list[i] = csv_list[i].replace(time_split[0],str(time_hour))
        # csv_list[i] = csv_list[i].replace()

with open('C:/Users/zyxx/Desktop/11月/new.csv', 'a') as nf:
    for k in csv_list:
        nf.write(k)
# データ記録できた場合

# データ記録できなかった場合
