# Sensor <-> RasPiHeader
# Vin    <-> 01
# 3V3    <-> 01
# GND    <-> 09
# SCL    <-> 05
# SDA    <-> 03

# Python 2.7.16

# 修正
# ----------------------------------------
# 2022-10-26

# ----------------------------------------
import RPi.GPIO as GPIO
from time import time
import smbus

GPIO.setmode(GPIO.BCM)
gp_out = 18
GPIO.setup(gp_out, GPIO.OUT)
motor = GPIO.PWM(gp_out, 50)
motor.start(0.0)

# 結果保存する場所
result_path = '/home/pi/henko/result/'

time_local = time.strftime('%Y-%m-%d', time.localtime(time.time()))
csv_file = result_path + '%s.csv' % time_local
file = open(csv_file, 'a')
file.write(time_local + ',,,' + time.strftime('%H:%M:%S', time.localtime(
    time.time())) + '\n' + 'angle,henko(LUX),CH0,CH1,LUX1,LUX2\n')

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


def tcaselect(channel):
    data = 1 << channel
    i2c.write_byte_data(0x70, 0x00, data)


def angle(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    motor.ChangeDutyCycle(duty)
    time.sleep(0.3)


# TCA9548Aに関する設定
# tcaselect(0)の意味は：SD0はSDAと繋ぐ、SC0はSCAと繋ぐ
tcaselect(0)
# モーターを-90の所に戻す
angle(-90)

if (initTSL2572() != 0):
    print('Failed')
    sys.exit()

measure_num = 3
total = 0

Note = open('1.txt', mode='w')

k = 0
avg = 0
sum = 0

for i in range(37):
    angle((i - 18) * 5)
    time.sleep(0.1)
    adc = getTSL2572adc()
    print("sekigai + kasiko = %s" % adc[0])
    print("sekigai = %s" % adc[1])
    cpl = 0.0
    lux1 = 0.0
    lux2 = 0.0
    cpl = (2.73 * (256 - atime) * gain) / (60.0)
    lux1 = ((adc[0] * 1.00) - (adc[1] * 1.87)) / cpl
    lux2 = ((adc[0] * 0.63) - (adc[1] * 1.00)) / cpl
    time.sleep(0.01)
    if ((lux1 <= 0) and (lux2 <= 0)):
        print("0 Lx")
    elif (lux1 > lux2):
        k += 1
        print(lux1)
        file.write(str(5 * i) + ',' + str(lux1) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
            lux2) + ',' + '\n')
        print('--------------------------')
    elif (lux1 < lux2):
        print(lux2)
        file.write(str(5 * i) + ',' + str(lux2) + ',' + str(adc[0]) + ',' + str(adc[1]) + ',' + str(lux1) + ',' + str(
            lux2) + ',' + '\n')
        print('--------------------------')
    time.sleep(0.2)
    if i == 36:
        angle(-90)
        file.write('\n')
        GPIO.cleanup()
file.close()
