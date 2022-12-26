import os
import requests
import datetime

# ------------------自動アップデード機能-------------------
raspberry_code_path = '/home/pi/Documents/test/zyxx/'
gdrive_code_path = 'gdrive_taka:偏光測定器_コード/zyxx/'
raspberry_data_path = '/home/pi/Documents/test'
# パソコンにあるソースコードの場所
pc_code_path = 'D:/pythonProject/偏光測定器_コード/'
gdrive_code_name = []

# -------------------line通知機能-------------------------
token = "qsI16BJFqnoajg7ci1vxDlhxx84AKZp0r3C4b0YV5pO"
headers = {"Authorization": "Bearer " + token}
line_notify_url = "https://notify-api.line.me/api/notify"

# ----------------ダウンロード機能-------------------------
cloud_experimental_path = 'gdrive_taka:偏光測定器_実験データ'  # グーグルクラウドにある実験データのフォルダ
pc_experimental_path = 'C://Users/zyxx/Desktop/test_csv/experimental_data/'
# ------------------ gdrive_one.py と関係ある機能----------------------
# date_start と date_end　から　、この間の全ての日付を得られる
# --例　↓　--
# data = []
# date_time('2022-10-11','2022-10-15',data) と
# data = ['2022-10-11','2022-10-12','2022-10-13','2022-10-14','2022-10-15']　は同じ意味である
# --例　↑　--


def date_time(date_start, date_end, data):
    start = datetime.datetime.strptime(date_start, '%Y-%m-%d')
    end = datetime.datetime.strptime(date_end, '%Y-%m-%d')
    step = datetime.timedelta(days=1)

    while start <= end:
        data.append(start.date())
        start += step


for name in os.popen('rclone ls %s' % gdrive_code_path).read().split('\n'):
    if name != '':
        gdrive_code_name.append(name.strip().split(' ')[1])


# ファイルを更新する　メソッド
def update(source_path, target_path):
    os.system('rclone sync %s %s -P' % (source_path, target_path))


# ファイルをアップロードする　メソッド
def upload(source_path, target_path):
    os.system('rclone copy %s %s -P' % (source_path, target_path))


# ファイルを削除する　メソッド
def delete(source_path):
    os.system('rclone delete %s' % (source_path))


# -------------------line通知機能--------------------------
def line_send_message(message):
    data = {'message': message}
    requests.post(line_notify_url, headers=headers, data=data)


if __name__ == '__main__':
    for file in os.listdir(pc_code_path):
        if file.endswith('py'):
            update(file, gdrive_code_path)
