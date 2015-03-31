#!/usr/bin/python

import RPi.GPIO as GPIO
import time

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

PIR_PIN = 22
GPIO.setup(PIR_PIN, GPIO.IN)

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

count = 0

while True:
	
	if GPIO.input(PIR_PIN):
		print "Motion Detected"
		time.sleep(1)	
		print count
		count=count + 1
	else : 
		count=0

GPIO.cleanup()
