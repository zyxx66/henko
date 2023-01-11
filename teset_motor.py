import RPi.GPIO as GPIO
import time
import smbus

gp_out = 5
motor = GPIO.PWM(gp_out, 50)
motor.start(0.0)