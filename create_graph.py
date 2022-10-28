# csvファイルからグラフを作るプログラムである
import os

# import pandas as pd
# check the start
# 'sizen(LUX)'

# check the end
# 'main(LUX)' in

write_permission = False

with open('C:/Users/zyxx/Desktop/2022-10-16-n.csv', 'r') as f:
    for words in f:
        if 'henkoudo' in words:
            write_permission = True
        if '2022-10-16' in words:
            time_date = words.split('-')[3].split(',')[0]
            write_permission = False
        if write_permission:
            print(words.split(','))
            if words.split(',')[5] != '\n':
                print(time_date)
                print(words.split(',')[5])
