# すべてのcsvファイルをgoogle driveにアップロードする

import os
import rclone_method

raspberry_source_path = [['/home/pi/Documents/test/filetest', 'gdrive_taka:偏光測定器_照度データ'],
                         ['/home/pi/Documents/test/unryo', 'gdrive_taka:偏光測定器_雲量データ']
                         ]

if __name__ == '__main__':
    for raspberry_path in raspberry_source_path:
        for file in os.listdir(raspberry_path[0]):
            if file.endswith('.csv'):
                file_split = file.split('-')
                file_year = file_split[0]
                file_month = file_split[1]
                file_day = file_split[2].split('.')[0]
                target_path = raspberry_path[1]+'/%s年/%s月'%(file_year,file_month)
                print(target_path)
                rclone_method.update(raspberry_path[0]+'/'+file,target_path)