import os
import rclone_method

upload_data_time = ['2022-10-11',
                    '2022-10-12',
                    '2022-10-13',
                    '2022-10-14',
                    '2022-10-15',
                    '2022-10-16',
                    '2022-10-17',
                    '2022-10-18'
                    ]
rd = rclone_method.raspberry_data_path + '/'
raspberry_source_path = [[rd + 'bw', '.csv'],
                         [rd + 'filetest', '.csv'],
                         [rd + 'unryo', '.jpg'],
                         [rd + 'tp', '.jpg'],
                         ]


def gdrive_once(source_path, suffix):
    for time in upload_data_time:
        for file in os.listdir(source_path):
            if time in file:
                if suffix == '.csv':
                    pass
                    break

                if file.endswith(suffix):
                    file_split = file.split('-')
                    print(file_split)
                    file_year = file_split[0]
                    file_month = file_split[1]
                    file_day = file_split[2]
                    target_path = "/偏光測定器\u3000データ/%s年/%s月/%s日" % (file_year, file_month, file_day)
                    rclone_method.update(source_path, target_path)


if __name__ == '__main__':
    for source in raspberry_source_path:
        gdrive_once(source[0], source[1])

# 雲量データをアップロードする
# 照度データをアップロードする
# 写真をアップロードする
# 二値化写真をアップロードする
