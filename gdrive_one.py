import os
import rclone_method


def pass_2(source_path, suffix):
    for file in os.listdir(source_path):
        if file.endswith(suffix):
            file_split = file.split('-')
            print(file_split)
            file_year = file_split[0]
            file_month = file_split[1]
            file_day = file_split[2]
            print('year = %s mounth = %s day = %s' % (file_year, file_month, file_day))

        if suffix == '.csv':
            pass


# 雲量データをアップロードする
path_unryo = rclone_method.raspberry_data_path + '/unryo'
pass_2(path_unryo, '.csv')

# 照度データをアップロードする
path_syodo = rclone_method.raspberry_data_path + '/filetest'
pass_2(path_syodo, '.csv')

# 写真をアップロードする
path_photo = rclone_method.raspberry_data_path + '/tp'
pass_2(path_photo, '.jpg')

# 二値化写真をアップロードする
path_photo_2 = rclone_method.raspberry_data_path + '/bw'
pass_2(path_photo_2, 'jpg')
