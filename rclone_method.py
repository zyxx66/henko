import os

raspberry_code_path = '/home/pi/Documents/test/zyxx/'
gdrive_code_path = 'gdrive_taka:偏光測定器_コード/zyxx/'

# パソコンにあるソースコードの居場所
pc_code_path = 'D:/pythonProject/偏光測定器_コード/'

gdrive_code_name = []

for name in os.popen('rclone ls %s' % gdrive_code_path).read().split('\n'):
    if name != '':
        gdrive_code_name.append(name.strip().split(' ')[1])


# ファイルを更新する　メソッド
def refresh(source_path, target_path):
    os.system('rclone sync %s %s -P' % (source_path, target_path))


# ファイルをアップロードする　メソッド
def upload(source_path, target_path):
    os.system('rclone copy %s %s -P' % (source_path, target_path))


# ファイルを削除する　メソッド
def delete(source_path):
    os.system('rclone delete %s' % (source_path))


if __name__ == '__main__':
    for file in os.listdir(pc_code_path):
        if file.endswith('py'):
            refresh(file, gdrive_code_path)
