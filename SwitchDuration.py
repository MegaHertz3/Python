#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#pin7=GPIO, pin9=GND
go = True

led = 17
GPIO.setup(led, GPIO.OUT)
long = int(input('How long do u want the switch on for?\n'))
long *= 60
while go == True:
    GPIO.output(led, 1)
    time.sleep(long)
    GPIO.output(led, 0)
    go = False
