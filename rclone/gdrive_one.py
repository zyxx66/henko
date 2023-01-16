import os
from rclone import rclone_method

# 開始日付と終了日付を入力してください
# 半角で入力　と　[''],[-]を忘れないように
# 例　　date_start = '2022-10-11'
# 　　　date_end = '2022-10-15'

date_start = '2022-04-01'
date_end = '2022-10-27'
upload_date = []

rclone_method.date_time(date_start, date_end, upload_date)
rd = rclone_method.raspberry_data_path + '/'
# raspberry_source_path = [[rd + 'bw', '.jpg'],
#                          [rd + 'filetest', '.csv'],
#                          [rd + 'unryo', '.csv'],
#                          [rd + 'tp', '.jpg'],
#                          ]

raspberry_source_path = [[rd + 'unryo', '.csv']]

def gdrive_once(source_path, suffix):
    for time in upload_date:
        for file in os.listdir(source_path):
            if str(time) in file:
                if suffix == '.csv':
                    pass

                if file.endswith(suffix):
                    file_split = file.split('-')
                    file_year = file_split[0]
                    file_month = file_split[1]
                    file_day = file_split[2].split('.')[0]
                    #target_path = "gdrive_taka:偏光測定器\u3000データ/%s年/%s月/%s日" % (file_year, file_month, file_day)
                    target_path = "gdrive_taka:偏光測定器_雲量データ/%s年/%s月/" % (file_year, file_month)
                    rclone_method.update(source_path + '/' + file, target_path)


if __name__ == '__main__':
    for source in raspberry_source_path:
        gdrive_once(source[0], source[1])
