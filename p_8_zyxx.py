import RPi.GPIO as GPIO
import time
import requests
import picamera
from datetime import datetime
import urllib.parse as parse
import smbus
from gpiozero import MCP3008
import csv
import os
import cv2
import numpy as np
import ts1
# ----2023/02/27追加----
# ライン通知機能使用かどうか
line_notice = False

GPIO.setmode(GPIO.BCM)
gp_out = 18
GPIO.setup(gp_out, GPIO.OUT)
motor = GPIO.PWM(gp_out, 50)
motor.start(0.0)

# ----2023/01/12追加----
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
# ----------------------

GPIO.setup(5, GPIO.OUT)
motor2 = GPIO.PWM(5, 50)

# ----2023/01/12追加----

# センサ―　や　マルチプレクサ　に電源入れ
GPIO.output(27, GPIO.HIGH)

# マルチプレクサーをリセットさせる(測定器の長く使用できるようになることに役に立てるかどうか知らない)
GPIO.output(17, GPIO.LOW)
time.sleep(0.5)
GPIO.output(17, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(17, GPIO.LOW)
time.sleep(0.5)
GPIO.setup(17, GPIO.IN)
time.sleep(5)
# -----------------------

unryou = 0
gege = datetime.now()
fdate_str = gege.strftime("%Y-%m-%d") + "-n.csv"
datestr = gege.strftime("%Y-%m-%d-%H:%M:%S") + ".jpg"
fdir = "/home/pi/Documents/test/filetest/"
fileName = fdir + fdate_str
bwdir = "/home/pi/Documents/test/bw/"
csvfile = "/home/pi/Documents/test/unryo/" + gege.strftime("%Y-%m-%d") + ".csv"
bwname = bwdir + datestr

with picamera.PiCamera() as camera:
    now_datetime = datetime.now()
    date_str = now_datetime.strftime("%Y-%m-%d-%H:%M") + ".jpg"
    dir = "/home/pi/Documents/test/tp/"
    filename = dir + date_str
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture(filename)


    def calc_black_whiteArea(bw_image):
        bwsize = bw_image.size
        whitePixels = cv2.countNonZero(bw_image)
        blackPixels = bw_image.size - whitePixels

        whiteAreaRatio = (whitePixels / bwsize) * 100  # [%]
        blackAreaRatio = (blackPixels / bwsize) * 100  # [%]

        print("White Area [%] : ", whiteAreaRatio)
        print("Black Area [%] : ", blackAreaRatio)
        f = open(csvfile, 'a')
        f.write(gege.strftime("%H%M") + ',' + str(blackAreaRatio) + '\n')
        global unryou
        unryou = blackAreaRatio


    if __name__ == "__main__":
        data = cv2.imread(filename, cv2.IMREAD_COLOR)
        hsvdata = cv2.cvtColor(data, cv2.COLOR_BGR2HSV)

        lower_hsv = np.array([90, 136, 102])
        upper_hsv = np.array([150, 255, 255])

        outimage = cv2.inRange(hsvdata, lower_hsv, upper_hsv)
        cv2.imwrite(bwname, outimage)
        calc_black_whiteArea(outimage)

url = "https://notify-api.line.me/api/notify"
# token = "hzTfA60slHsBBvS5J9GwgwMCWbrV6PdbXfLIM4TzyGD"
# token = "H5elt3vAYuitcjLoVNo0KoQdjDmeEhODrgK0agnexeV"

# f219030
# token = "qsI16BJFqnoajg7ci1vxDlhxx84AKZp0r3C4b0YV5pO"

image = filename


def angle(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    motor.ChangeDutyCycle(duty)
    time.sleep(1)


angle(-90)

hlist = []
slist = []

# ts1.init()

f = open(fileName, 'a')
f.write(gege.strftime("%Y-%m-%d-%H:%M:%S") + ',,,' + gege.strftime(
    "%H%M") + '\n' + 'sizen(LUX),henko(LUX),ch0,ch1,Lux1(LUX),Lux2(LUX)\n')

motor2.start(5)
time.sleep(1)
GPIO.setup(5, GPIO.IN)

ts1.tcaselect(0)
time.sleep(0.5)
ts1.tcaselect(1)
time.sleep(0.5)

for i in range(37):
    angle((i - 18) * 5)
    time.sleep(0.3)
    ts1.tcaselect(1)
    time.sleep(1)
    ts1.init()
    sizenko = ts1.lux_get()
    ts1.tcaselect(0)
    time.sleep(1)
    ts1.init()
    henko = ts1.lux_get()

    # 2023/01/12 upload
    #　こちらのコードは、偏光の値が0になってしまった場合があるので、0にならないように存在している
    if henko[0] == 0:
        continue
    else:
        print("偏光:" + str(round(henko[0], 2)) + "lux" + "   自然光:" + str(round(sizenko[0], 2)) + " lux")
        f.write(str(round(sizenko[0], 2)) + ',' + str(round(henko[0], 2)) + ',' + str(round(henko[1], 2)) + ',' + str(
            round(henko[2], 2)) + ',' + str(round(henko[3], 2)) + ',' + str(round(henko[4], 2)) + '\n')
        hlist.append(round(henko[0], 2))
        slist.append(round(sizenko[0], 2))

GPIO.setup(5, GPIO.OUT)
motor2.start(9.3)
time.sleep(0.3)
GPIO.setup(5, GPIO.IN)
max = max(hlist)
min = min(hlist)
s_ave = sum(slist) / len(slist)
henkoudo = ((max - min) / (max + min)) * 100
f.write('max(LUX),' + 'min(LUX),' + 'sizen(LUX),' + ',,' + 'henkoudo' + ',' + 'unryou' + '\n')
f.write(str(max) + ',' + str(min) + ',' + str(s_ave) + ',' + ' ,' + ' ,' + str(henkoudo) + ',' + str(unryou) + '\n' + '\n')
map1 = map(str, hlist)
lstr = ','.join(map1)
ms_data = '自然光(LUX)：' + str(round(s_ave, 2)) + '偏光(LUX)：' + lstr + "最大値:" + str(round(max, 2)) + "最小値:" + str(
    round(min, 2))
ms2 = '雲量（％）：' + str(unryou) + '偏光度（％）：' + str(henkoudo)

if line_notice:
    send_data = {'message': ms_data}
    send2 = {'message': ms2}
    headers = {'Authorization': 'Bearer ' + token}
    files = {'imageFile': open(image, 'rb')}
    file2 = {'imageFile': open(bwname, 'rb')}
    res = requests.post(url, data=send_data, headers=headers, files=files)
    res2 = requests.post(url, data=send2, headers=headers, files=file2)

print(henkoudo)

# 2022/11/24 追加
GPIO.cleanup()
