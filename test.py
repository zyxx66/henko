import os
import requests
import time

# 今日の日時を取得する
time_local = time.strftime('%Y-%m-%d', time.localtime(time.time()))
time_local_year = time_local[0:4]
time_local_mounth = time_local[5:7]
time_local_day = time_local[8:10]

file_amount = 0


def upload_to_gdrive(source_path, suffix, target_path):
    global file_amount
    for file_name in os.listdir(source_path):
        file_name_split = file_name.split('-')
        if file_name.split(".")[1] == suffix:
            if file_name_split[0] == time_local_year:
                if file_name_split[1] == time_local_mounth:
                    print(file_name_split[2].split('.')[0])
                    if file_name_split[2].split('.')[0] == time_local_day:
                        file_amount += 1
                        os.system("rclone copy %s gdrive_taka:%s " % (source_path + "/" + file_name, target_path))


upload_to_gdrive("/home/pi/Documents/test/tp", "jpg",
                 "/偏光測定器　データ/%s年/%s月/%s日/" % (time_local_year, time_local_mounth, time_local_day))
