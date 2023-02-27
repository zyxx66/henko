import os

sum_up_csv = 'C:/Users/zyxx/Desktop/test_csv/daily_data/result/sumup.csv'
unryo_folder = 'C:/Users/zyxx/Desktop/test_csv/daily_data/unryo'

sumup = open(sum_up_csv, 'r')
sumup_list = []
start_list = []

# まずは'0'を追加

for i in sumup:
    sumup_list.append(i)

for i in range(sumup_list.__len__()):
    if '/' in sumup_list[i]:
        start_list.append(i + 2)
    if 'end' in sumup_list[i]:
        start_list.append(i + 2)

for i in range(start_list.__len__() ):
    csv_list = []
    # 時間を読み取る
    time_split = sumup_list[start_list[i] - 2].split(',')[0].split('/')
    csv_file = time_split[0] + '-' + time_split[1] + '-' + time_split[2] + '.csv'
    print(csv_file)
    # 雲量csvファイルを開く
    csv_file_reader = open(unryo_folder + '/' + csv_file, 'r')
    for k in csv_file_reader:
        csv_list.append(k)
    for l in csv_list:
        l_split = l.split('\n')[0].split(',')
        time = l_split[0]
        unryo = l_split[1]
        print(time)
    for j in range(start_list[i], start_list[i+1] - 2):
        pass
print(csv_list)