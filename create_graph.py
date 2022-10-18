import os

for file_path in os.popen('rclone ls gdrive_taka:').read().split('\n'):
    if '-n' in file_path and file_path.endswith('.csv'):
        # print('偏光測定器 データ'+file_path.split('データ')[1])
        gdrive_path = 'gdrive_taka:偏光測定器\u3000データ' + file_path.split('データ')[1]
        os.system('rclone copy %s /home/pi/Documents/test/filetest/ -P' % (gdrive_path))

