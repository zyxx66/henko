# 粒子実験用プログラム

import os
import sys
import RPi.GPIO as GPIO
import time
import smbus
from rclone import rclone_method

# ----------設定----------
check_times = 3
# -----------------------
def tcaselect(channel):
    data = 1 << channel
    i2c.write_byte_data(0x70, 0x00, data)


def initTSL2572():
    if (getTSL2572reg(TSL2572_ID) != [0x34]):
        # check TSL2572 ID
        return -1
    setTSL2572reg(TSL2572_COMMAND | TSL2572_TYPE_INC | TSL2572_CONTROL, 0x00)
    setTSL2572reg(TSL2572_COMMAND | TSL2572_TYPE_INC | TSL2572_CONFIG, 0x00)
    setTSL2572reg(TSL2572_COMMAND | TSL2572_TYPE_INC | TSL2572_ATIME, atime)
    setTSL2572reg(TSL2572_COMMAND | TSL2572_TYPE_INC | TSL2572_ENABLE, TSL2572_AEN | TSL2572_PON)
    return 0


def setTSL2572reg(reg, dat):
    i2c.write_byte_data(TSL2572_ADR, reg, dat)


def getTSL2572reg(reg):
    dat = i2c.read_i2c_block_data(TSL2572_ADR, TSL2572_COMMAND | TSL2572_TYPE_INC | reg, 1)
    return dat

def getTSL2572adc():
    dat = i2c.read_i2c_block_data(TSL2572_ADR, TSL2572_COMMAND | TSL2572_TYPE_INC | TSL2572_C0DATA, 4)
    adc0 = (dat[1] << 8) | dat[0]
    adc1 = (dat[3] << 8) | dat[2]
    return [adc0, adc1]


def angle(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    motor.ChangeDutyCycle(duty)
    time.sleep(0.1)

GPIO.setmode(GPIO.BCM)
gp_out = 18
GPIO.setup(gp_out, GPIO.OUT)
motor = GPIO.PWM(gp_out, 50)
motor.start(0.0)

i2c = smbus.SMBus(1)

# TSL2572 Register Set
TSL2572_ADR = 0x39
TSL2572_COMMAND = 0x80
TSL2572_TYPE_REP = 0x00
TSL2572_TYPE_INC = 0x20
TSL2572_ALSIFC = 0x66

TSL2572_SAI = 0x40
TSL2572_AIEN = 0x10
TSL2572_WEN = 0x80
TSL2572_AEN = 0x02
TSL2572_PON = 0x01

TSL2572_ENABLE = 0x00
TSL2572_ATIME = 0x01
TSL2572_WTIME = 0x03
TSL2572_AILTL = 0x04
TSL2572_AILTH = 0x05
TSL2572_AIHTL = 0x06
TSL2572_AIHTH = 0x07
TSL2572_PRES = 0x0C
TSL2572_CONFIG = 0x0D
TSL2572_CONTROL = 0x0F
TSL2572_ID = 0x12
TSL2572_STATUS = 0x13
TSL2572_C0DATA = 0x14
TSL2572_C0DATAH = 0x15
TSL2572_C1DATA = 0x16
TSL2572_C1DATAH = 0x17

# TSL2572 setings
atime = 0xC0
gain = 1.0

# 結果保存する場所
result_path = '/home/pi/henko/result/'

# こちらの順番はどうでもいい、番号が合ったらオーケー
number = {'6': '薄力小麦粉(20~50㎛)',
          '8': 'トマトパウダー(100~500㎛)',
          '5': '黒鉛粉末(5~11㎛)',
          '4': 'トルマリン(3㎛)',
          '3': 'トルマリン(1.8㎛)',
          '2': 'トルマリン(0.8㎛)',
          '1': 'RX_OX(40nm)',
          '7': 'スギ花粉(30㎛)',
          '9': '空き'
          }

# こちらの順番はどうでもいい
name = {'薄力小麦粉(20~50㎛)': 'komugiko',
        'トマトパウダー(100~500㎛)': 'tomato',
        '黒鉛粉末(5~11㎛)': 'kokuen',
        'トルマリン(3㎛)': 'torumarin_3',
        'トルマリン(1.8㎛)': 'torumarin_1.8',
        'トルマリン(0.8㎛)': 'torumarin_0.8',
        'RX_OX(40nm)': 'RX_OX',
        'スギ花粉(30㎛)': 'sugikafun',
        '空き': 'empty'}

# こちらの順番はどうでもいい
diameter = {'薄力小麦粉(20~50㎛)': '20~50um',
            'トマトパウダー(100~500㎛)': '100~500um',
            '黒鉛粉末(5~11㎛)': '5~11um',
            'トルマリン(3㎛)': '3um',
            'トルマリン(1.8㎛)': '1.8um',
            'トルマリン(0.8㎛)': '0.8um',
            'RX_OX(40nm)': '40nm',
            'スギ花粉(30㎛)': '30um',
            '空き': '--'}
k = 0
while True:
    # 測定目標リスト
    print('測定目標'.center(40, '-'), '\n',
          '\033[0;37;40m', '1:RX OX(40nm)'.center(40), '\033[0m'
                                                       '\n',
          '2:トルマリン(0.8㎛)'.center(40),
          '\n',
          '\033[0;37;40m', '3:トルマリン(1.8㎛)'.center(36), '\033[0m'
                                                       '\n',
          '4:トルマリン(3㎛)'.center(40),
          '\n',
          '\033[0;37;40m', '5:黒鉛粉末(5~11㎛)'.center(37), '\033[0m'
                                                       '\n',
          '6:薄力小麦粉(20~50㎛)'.center(40),
          '\n',
          '\033[0;37;40m', '7:スギ花粉(30㎛)'.center(37), '\033[0m'
                                                     '\n',
          '8:トマトパウダー(100~500㎛)'.center(40),
          '\n',
          '\033[0;37;40m', '9:空き'.center(39), '\033[0m'
          '\n',
          '10:本日の実験結果をアップロードする,実験終了'.center(36),
          '\n',
          ''.center(40, '-'))


    time_local = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    result_path += time_local
    if k == 0:
        if not os.path.exists(result_path):
            os.mkdir(result_path)
        result_path += '/'
        sumup_file_path = result_path+'sumup'
        if not os.path.exists(sumup_file_path):
            os.mkdir(sumup_file_path)
        sumup_file_path+='/'
        k+=1

    target_number = input('測定目標の番号を入力してください.\n')
    if target_number != '10':
        try:
            target_name = number[target_number]
        except:
            print('正しい番号を入力してください')
            sys.exit()

        target_name_short = name[target_name]
        target_diameter = diameter[target_name]

        csv_file = result_path + '%s-e-%s.csv' % (time_local,target_name_short)
        csv_sumup_file = sumup_file_path + '%s-e-%s-sumup.csv' % (time_local,target_name_short)
        file = open(csv_file, 'a')
        time_now = time.strftime('%H:%M:%S', time.localtime(
            time.time()))
        if not os.path.exists(csv_sumup_file):
            file_sumup = open(csv_sumup_file, 'a')
            file_sumup.write(time_local + ',,,' + time_now  + ',,,,' + target_name_short + ',' + target_diameter + '\n' + 'time,min,max,偏光度\n')
        else:
            file_sumup = open(csv_sumup_file,'a')


        # タイトルを入力する
        file.write(time_local + ',,,' + time_now  + ',,,,' + target_name_short + ',' + target_diameter + '\n' + 'angle,henko(LUX),CH0,CH1,LUX1,LUX2\n')

        # マルチプレクサーを利用する場合は、下の行の　＃　を削除する
        # tcaselect(0)

        # モーターを-90の所に戻す
        angle(-90)

        if (initTSL2572() != 0):
            print('Failed')
            sys.exit()

        measure_num = 3
        total = 0

        k = 0
        avg = 0
        sum = 0

        max_lux = 0
        min_lux = 9999
        max_s = 0
        min_s = 9999

        for i in range(61):
            angle((i - 30)*3)
            time.sleep(0.1)
            sum_adc0 = 0
            sum_adc1 = 0
            for k in range(check_times):
                adc = getTSL2572adc()
                sum_adc0 += adc[0]
                sum_adc1 += adc[1]
                time.sleep(0.05)
            adc[0] = sum_adc0/check_times
            adc[1] = sum_adc1/check_times
            print("sekigai + kasiko = %s" % adc[0])
            print("sekigai = %s" % adc[1])
            cpl = 0.0
            lux1 = 0.0
            lux2 = 0.0
            cpl = (2.73 * (256 - atime) * gain) / (60.0)
            lux1 = ((adc[0] * 1.00) - (adc[1] * 1.87)) / cpl
            lux2 = ((adc[0] * 0.63) - (adc[1] * 1.00)) / \
                   cpl
            time.sleep(0.01)
            if ((lux1 <= 0) and (lux2 <= 0)):
                print("0 Lx")
                file.write(str(3 * i) + ',' + str(lux1) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
                    lux2) + ',' + '\n')
                if 0 > max_lux:
                    max_lux = 0
                if 0 <= min_lux:
                    min_lux = 0
                if adc[1] > max_s:
                    max_s = adc[1]
                if adc[1] < min_s:
                    min_s = adc[1]
                print('max(s) = %f , min(s) = %f' % (max_s, min_s))
                print('max = %f , min = %f'%(max_lux,min_lux))

                print(time_now.center(40,'-'))
            elif (lux1 >= lux2):
                k += 1
                print(lux1)
                file.write(str(3 * i) + ',' + str(lux1) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
                    lux2) + ',' + '\n')
                if lux1 > max_lux:
                    max_lux = lux1
                if lux1 <= min_lux:
                    min_lux = lux1
                if adc[1] > max_s:
                    max_s = adc[1]
                if adc[1] < min_s:
                    min_s = adc[1]
                print('max(s) = %f , min(s) = %f' % (max_s, min_s))
                print('max = %f , min = %f'%(max_lux,min_lux))
                print(time_now.center(40,'-'))
            elif (lux1 < lux2):
                print(lux2)
                file.write(str(3 * i) + ',' + str(lux2) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
                    lux2) + ',' + '\n')
                if lux2 > max_lux:
                    max_lux = lux2
                if lux2 < min_lux:
                    min_lux = lux2
                if adc[1] > max_s:
                    max_s = adc[1]
                if adc[1] < min_s:
                    min_s = adc[1]
                print('max(s) = %f , min(s) = %f' % (max_s, min_s))
                print('max = %f , min = %f,' % (max_lux, min_lux))
                print(time_now.center(40,'-'))

        if i == 60:
            angle(-90)
            henkodo = (max_lux - min_lux) / (max_lux + min_lux)
            henkodo2 = (max_s-min_s)/(max_s+min_s)
            file_sumup.write('%s,%f,%f,%f\n'%(time_now,min_lux,max_lux,henkodo))
            print('偏光度1 = %f'%(henkodo))
            print('偏光度2 = %f'%(henkodo2))
            file.write('\n')
        file.close()
        file_sumup.close()

        # 実験ファイルを google drive　にアップロードする機能、要らなかったら Ture　を Falseにしてください

    elif target_number == '10':
        for file_name in os.listdir(result_path):
            if time_local in file_name:
                source_file = result_path+file_name
                time_local_split = time_local.split('-')
                target_path = "gdrive_taka:偏光測定器_実験データ/%s年/%s月/%s日" % (time_local_split[0], time_local_split[1],time_local_split[2])
                rclone_method.update(source_file, target_path)
        time.sleep(1)
        GPIO.cleanup()
        break