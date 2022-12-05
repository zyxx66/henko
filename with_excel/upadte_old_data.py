# 2022-11-02以前のデータを更新するためのプログラムである
import os
import rclone_method as rm

folder = 'C://Users/zyxx/Desktop/test_csv/daily_data/'
date_start = '2022-10-01'
date_end = '2022-11-05'

date_time = []
rm.date_time(date_start, date_end, date_time)


def download(date_time: []):
    for times in date_time:
        time_split = str(times).split('-')
        file_year = time_split[0]
        file_month = time_split[1]


        file_name = str(times)
        # 雲量ファイル(偏光度)
        source_path = "gdrive_taka:偏光測定器_雲量データ/%s年/%s月/"  % (file_year, file_month) + file_name + '.csv'
        # 照度ファイル(偏光度)
        source_path2 = "gdrive_taka:偏光測定器_照度データ/%s年/%s月/" % (file_year, file_month) + file_name + '-n.csv'
        target_path = folder

        rm.update(source_path, target_path)
        rm.update(source_path2,target_path)

        update(target_path+str(times)+'.csv',target_path+str(times)+'-n.csv')
        # 雲量ファイルを削除する
        os.remove(target_path+str(times)+'.csv')

def update(csv_file_unryo,csv_file_syoudo):
    csv_list_unryo = []
    csv_list_syoudo = []

    with open(csv_file_unryo) as f:
        for row in f:
            csv_list_unryo.append(row)

    with open(csv_file_syoudo) as f:
        for row in f:
            csv_list_syoudo.append(row)

    for i in range(csv_list_syoudo.__len__()):
        if 'max(LUX)' in csv_list_syoudo[i]:
            data_time = csv_list_syoudo[i-39].split('\n')[0].split(',')[3]
            for k in range(csv_list_unryo.__len__()):
                if data_time in csv_list_unryo[k]:
                    unryou = csv_list_unryo[k].split('\n')[0].split(',')[1]
                    break
            csv_list_syoudo_split = csv_list_syoudo[i+1].split('\n')[0].split(',')
            csv_list_syoudo[i+1] = csv_list_syoudo_split[0]+','+csv_list_syoudo_split[1]+','+csv_list_syoudo_split[2]+',,,'\
                                   +csv_list_syoudo_split[5]+','+unryou+'\n'

    with open(csv_file_syoudo,'w') as f:
        for i in range(csv_list_syoudo.__len__()):
            f.write(csv_list_syoudo[i])




if __name__ == '__main__':
    download(date_time)

