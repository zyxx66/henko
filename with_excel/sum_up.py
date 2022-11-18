def sumup(folder):
    file = folder + 'sumup.csv'

    data_time = {'0600': 1, '0630': 2, '0700': 3, '0730': 4, '0800': 5, '0830': 6, '0900': 7, '0930': 8, '1000': 9,'1030': 10,
                 '1100': 11,'1130': 12, '1200': 13, '1230': 14, '1300': 15, '1330': 16, '1400': 17, '1430': 18, '1500': 19,
                 '1530': 20,'1600': 21,'1630': 22, '1700': 23, '1730': 24, '1800': 25, '1830': 26}

    # ある日入力したら１、入力してない(空欄の場合)0
    input_check = []

    for i in range(26):
        input_check.append(0)

    data_csv = ['\n']

    for i in range(13):
        for k in range(2):
            if i < 4:
                data_csv.append('0'+str(i+6)+str(k*3)+'0,\n')
            else:
                data_csv.append(str(i+6)+str(k*3)+'0,\n')

    print(data_csv)

    data = []



    with open(file) as f:
        for i in f:
            data.append(i)

    start_point_list = []
    row_number = 0

    for i in range(data.__len__()):
        if 'time' in data[i]:
            start_point_list.append(i)
        if 'end' in data[i]:
            start_point_list.append(i)

    for i in range(len(start_point_list)):
        data_csv[0] = data_csv[0].split('\n')[0] + data[start_point_list[i]-1]
        if i == 0:
            data_csv[0] = data_csv[0].split('\n')[0] +','

        if i == len(start_point_list) - 1:
            break
        for i in range(start_point_list[i] + 1, start_point_list[i + 1] - 1):
            data_split = data[i].split(',')
            if data_split[0] in data_time:
                row = data_time[data_split[0]]
                data_csv[row] = data_csv[row].split('\n')[0] + data_split[1]+','+data_split[2]+',,\n'
                input_check[row-1] = 1
        for i in range(input_check.__len__()):
            if input_check[i] == 0:
                data_csv[i+1] = data_csv[i+1].split('\n')[0]+',,,\n'
            elif input_check[i] == 1:
                input_check[i] = 0
            # data_time[data[i+1]]
    print(start_point_list)
    for k in data:
        print(k)
    with open(folder+'sumup_2.csv','a') as f:
        for i in range(27):
            f.write(data_csv[i])