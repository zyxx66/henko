import os
import cv2
import numpy as np

for file in os.listdir('C:/Users/zyxx/Desktop/新しいフォルダー (2)/tp'):
    # print('C:/Users/zyxx/Desktop/新しいフォルダー (2)/tp'+file)
    print('1.start')
    pic_name = cv2.imread('C:/Users/zyxx/Desktop/新しいフォルダー (2)/tp/'+file)
    pic_gray = cv2.cvtColor(pic_name,cv2.COLOR_RGB2HSV)
    ret,pic_thresh = cv2.threshold(pic_gray,127,255,cv2.THRESH_BINARY)
    img_show = np.hstack([pic_name,pic_thresh])
    cv2.imshow('name',img_show)
    cv2.waitKey(0)
