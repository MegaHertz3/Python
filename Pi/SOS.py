#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#pin7=GPIO, pin9=GND
go = True
led = 17
GPIO.setup(led, GPIO.OUT)
def sos():
    for i in range(1,3):
        for I in range(3):
            GPIO.output(led, 1)
            time.sleep(i)
            GPIO.output(led, 0)
            time.sleep(i)
while go == True:
	sos()
