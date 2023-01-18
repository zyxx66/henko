# 光センサー不具合の有無を確認するプログラムである
# 動作：0.1秒間隔でセンサの結果を読み取る

import sys
import RPi.GPIO as GPIO
import time
import smbus

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
GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.HIGH)

def lux_get():
  adc = getTSL2572adc()
  cpl = 0.0
  lux1 = 0.0
  lux2 = 0.0
  cpl = (2.73 * (256 - atime) * gain)/(60.0)
  lux1 = ((adc[0] * 1.00) - (adc[1] * 1.87)) / cpl
  lux2 = ((adc[0] * 0.63) - (adc[1] * 1.00)) / cpl
  if ((lux1 <= 0) and (lux2 <= 0)) :
    return [0,adc[0],adc[1],lux1,lux2]
  elif (lux1 > lux2) :
    return [lux1,adc[0],adc[1],lux1,lux2]
  elif (lux1 < lux2) :
    return [lux2,adc[0],adc[1],lux1,lux2]

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

i = 1

print('測定目標'.center(40, '-'), '\n',
      '\033[0;37;40m', '1:tca(0)のセンサ'.center(40), '\033[0m'
                                                   '\n',
      '2:tca(1)のセンサ'.center(40),
      '\n',
      '\033[0;37;40m', '3:tca(0)とtca(1)のセンサ'.center(36), '\033[0m'
                                                   '\n',
      '4:直接繋いでるセンサ'.center(40),
      '\n',
      ''.center(40, '-'))

target_number = input('チェックしたい番号を入力して、エンターキーを押してください。\n')

if target_number == 1:
    while True:
        tcaselect(0)
        initTSL2572()
        henko = lux_get()
        print(henko)
        i += 1
        print('---------------------%d-----------' % i)

elif target_number == 2:
    while True:
        tcaselect(1)
        initTSL2572()
        henko = lux_get()
        print(henko)
        i += 1
        print('---------------------%d-----------' % i)

elif target_number == 3:
    while True:
        tcaselect(0)
        initTSL2572()
        henko = lux_get()
        print(henko)
        tcaselect(1)
        initTSL2572()
        henko = lux_get()
        print(henko)
        i += 1
        print('---------------------%d-----------' % i)

elif target_number == 4:
    while True:
        initTSL2572()
        henko = lux_get()
        print(henko)
        i += 1
        print('---------------------%d-----------' % i)
