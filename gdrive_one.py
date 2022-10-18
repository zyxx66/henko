import os

for file_name in os.listdir("/home/pi/Documents/test/unryo"):
    file_name_split = file_name.split('-')
    file_name_year = file_name_split[0]
    file_name_mounth = file_name_split[1]
    file_name_day = file_name_split[2].split('.')[0]
    os.system("rclone copy %s gdrive_taka:%s -P" % ("/home/pi/Documents/test/unryo/" + file_name,
                                                    "/偏光測定器_雲量データ/%s年/%s月/%s日/" % (
                                                    file_name_year, file_name_mounth, file_name_day)))

for file_name in os.listdir("/home/pi/Documents/test/filetest"):
    file_name_split = file_name.split('-')
    file_name_year = file_name_split[0]
    file_name_mounth = file_name_split[1]
    file_name_day = file_name_split[2].split('.')[0]
    os.system("rclone copy %s gdrive_taka:%s -P" % ("/home/pi/Documents/test/filetest/" + file_name,
                                                    "/偏光測定器_照度データ/%s年/%s月/%s日/" % (
                                                    file_name_year, file_name_mounth, file_name_day)))
