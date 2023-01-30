# 粒子が本当に飛んでるかどうかについて調べる実験である
# 光センサー不具合の有無を確認するプログラムである
# 動作：1秒間隔でセンサの結果を読み取る
import os.path
import sys
import RPi.GPIO as GPIO
import time
import smbus

# -----------測定設定----------
# 測定回数(秒)
time_of_measurements = 300
# 間隔時間(秒)
delay_of_measurements = 0.2
# 毎回測定中取るデータ数
check_times = 5
# -----------------------------

# 測定回数
number_of_measurements = int(time_of_measurements/delay_of_measurements)

GPIO.setmode(GPIO.BCM)

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


def lux_get():
    adc = getTSL2572adc()
    cpl = 0.0
    lux1 = 0.0
    lux2 = 0.0
    cpl = (2.73 * (256 - atime) * gain) / (60.0)
    lux1 = ((adc[0] * 1.00) - (adc[1] * 1.87)) / cpl
    lux2 = ((adc[0] * 0.63) - (adc[1] * 1.00)) / cpl
    if ((lux1 <= 0) and (lux2 <= 0)):
        return [0, adc[0], adc[1], lux1, lux2]
    elif (lux1 > lux2):
        return [lux1, adc[0], adc[1], lux1, lux2]
    elif (lux1 < lux2):
        return [lux2, adc[0], adc[1], lux1, lux2]


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


print('1:可視光の偏光\n'
      '2:赤外線の偏光')

max_lux = 0
min_lux = 9999
max_s = 0
min_s = 9999

target_number = input('測定したい部分の番号を入力してください：')

file_number = 1

if (initTSL2572() != 0):
    print('Failed')
    sys.exit()

if target_number == '1':
    while True:
        file_name = '/home/pi/henko/result/granule/granule_kasi_' + str(file_number) + '.csv'
        if os.path.exists(file_name):
            file_number += 1
        else:
            file = open(file_name, 'a')
            break

    for i in range(number_of_measurements):
        time_now = time.strftime('%H:%M:%S', time.localtime(
            time.time()))
        time.sleep(0.1)
        sum_adc0 = 0
        sum_adc1 = 0
        for k in range(check_times):
            adc = getTSL2572adc()
            sum_adc0 += adc[0]
            sum_adc1 += adc[1]
            time.sleep(0.05)
        adc[0] = sum_adc0 / check_times
        adc[1] = sum_adc1 / check_times
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
            file.write(
                str(i*delay_of_measurements) + ',' + str(lux1) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
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
            print('max = %f , min = %f' % (max_lux, min_lux))

            print(time_now.center(40, '-'))
        elif (lux1 >= lux2):
            print(lux1)
            file.write(
                str(i*delay_of_measurements) + ',' + str(lux1) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
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
            print('max = %f , min = %f' % (max_lux, min_lux))
        elif (lux1 < lux2):
            print(lux2)
            file.write(
                str(i*delay_of_measurements) + ',' + str(lux2) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
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
        print(time_now.center(40, '-'))
        time.sleep(delay_of_measurements)

if target_number == '2':
    while True:
        file_name = '/home/pi/henko/result/granule/granule_sekigai_' + str(file_number) + '.csv'
        if os.path.exists(file_name):
            file_number += 1
        else:
            file = open(file_name, 'a')
            break

    for i in range(number_of_measurements):
        time_now = time.strftime('%H:%M:%S', time.localtime(
            time.time()))
        time.sleep(0.1)
        adc = getTSL2572adc()
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
            file.write(
                str(i*delay_of_measurements) + ',' + str(lux1) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
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
            print('max = %f , min = %f' % (max_lux, min_lux))

            print(time_now.center(40, '-'))
        elif (lux1 >= lux2):
            print(lux1)
            file.write(
                str(i*delay_of_measurements) + ',' + str(lux1) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
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
            print('max = %f , min = %f' % (max_lux, min_lux))
        elif (lux1 < lux2):
            print(lux2)
            file.write(
                str(i*delay_of_measurements) + ',' + str(lux2) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
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
            print(time_now.center(40, '-'))
        time.sleep(delay_of_measurements)
print('file name : %s'%file_number)
file.close()
