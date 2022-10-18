# **********************************************************
# 実行すると当日の測定データと写真をgoogle driveにアップロードする
# **********************************************************
import os
import requests
import time

# 今日の日時を取得する
time_local = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# --------------------------
# debug用,削除しても構いません
# debugをする前に、各フォルダに 9999-99-99.csv　見たいなファイルを作成してください
# time_local = '9999-99-99'
# ---------------------------

time_local_year = time_local[0:4]
time_local_mounth = time_local[5:7]
time_local_day = time_local[8:10]

# LINE notift機能に関する情報
# f219030
# token = "qsI16BJFqnoajg7ci1vxDlhxx84AKZp0r3C4b0YV5pO"

# ファイルの数を数えるため
file_amount = 0

token = "qsI16BJFqnoajg7ci1vxDlhxx84AKZp0r3C4b0YV5pO"

headers = {"Authorization": "Bearer " + token}
line_notify_url = "https://notify-api.line.me/api/notify"


# LINEに通知する機能
def line_send_message(message):
    data = {'message': message}
    requests.post(line_notify_url, headers=headers, data=data)


def upload_to_gdrive(source_path, suffix, target_path):
    global file_amount
    for file_name in os.listdir(source_path):
        file_name_split = file_name.split('-')
        if file_name.split(".")[1] == suffix:
            if file_name_split[0] == time_local_year:
                if file_name_split[1] == time_local_mounth:
                    if file_name_split[2].split('.')[0] == time_local_day:
                        file_amount += 1
                        os.system("rclone copy %s gdrive_taka:%s -P" % (source_path + "/" + file_name, target_path))


def update_to_gdrive(source_path, suffix, target_path):
    global file_amount
    for file_name in os.listdir(source_path):
        file_name_split = file_name.split('-')
        if file_name.split(".")[1] == suffix:
            if file_name_split[0] == time_local_year:
                if file_name_split[1] == time_local_mounth:
                    if file_name_split[2].split('.')[0] == time_local_day:
                        file_amount += 1
                        os.system("rclone sync %s gdrive_taka:%s -P" % (source_path + "/" + file_name, target_path))


if __name__ == '__main__':
    # 本日の写真をアップロードする
    upload_to_gdrive("/home/pi/Documents/test/tp", "jpg",
                     "/偏光測定器\u3000データ/%s年/%s月/%s日/" % (time_local_year, time_local_mounth, time_local_day))

    # 本日の二値化図をアップロードする
    upload_to_gdrive("/home/pi/Documents/test/bw", "jpg",
                     "/偏光測定器\u3000データ/%s年/%s月/%s日" % (time_local_year, time_local_mounth, time_local_day))

    # 本日の照度データをアップロードする
    upload_to_gdrive("/home/pi/Documents/test/filetest", "csv",
                     "/偏光測定器_照度データ/%s年/%s月" % (time_local_year, time_local_mounth))
    upload_to_gdrive("/home/pi/Documents/test/filetest", "csv",
                     "/偏光測定器\u3000データ/%s年/%s月/%s日" % (time_local_year, time_local_mounth, time_local_day))

    # 本日の雲量データをアップロードする
    upload_to_gdrive("/home/pi/Documents/test/unryo", "csv",
                     "/偏光測定器_雲量データ/%s年/%s月" % (time_local_year, time_local_mounth))
    upload_to_gdrive("/home/pi/Documents/test/unryo", "csv",
                     "/偏光測定器\u3000データ/%s年/%s月/%s日" % (time_local_year, time_local_mounth, time_local_day))

    line_send_message("本日( %s )\n %s個 \n のファイルをアップロードしました。" % (time_local, file_amount))
