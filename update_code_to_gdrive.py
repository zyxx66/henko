# ***********************************************************************
# ラズベリーパイ　　にある　「ソースコード」　を　google drive　にアップロードする
# update the source code in google drive
# ***********************************************************************
import os

file_path = '/home/pi/Documents/test/zyxx/'
file_name = os.listdir(file_path)
gdrive_path = 'gdrive_taka:偏光測定器_コード/zyxx'

if __name__ == '__main__':
    for fn in file_name:
        if fn.endswith('.py'):
            os.system('rclone sync %s %s -P' % (file_path + str(fn), gdrive_path))
