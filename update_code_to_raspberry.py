import os
import rclone_method as rc

for code_name in rc.gdrive_code_name:

    rc.refresh(rc.gdrive_code_path + code_name, rc.raspberry_code_path)
