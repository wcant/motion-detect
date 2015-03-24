#!/usr/bin/python

import RPi.GPIO as GPIO
import picamera
import gps
import time

camera = picamera.PiCamera()

#--------------- GPIO Setup ------------------------------#

GPIO.setmode(GPIO.BCM)

#listen on pin 4 for PIR
PIR_PIN = 4

# Logically Low by default
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#--------------- GPS -------------------------------------#

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

#--------------- Event Callback --------------------------#

def eventTrigger(channel):

	print("Motion Detected")
	time_str = time.ctime()
	img_path = 'images/'+time_str.replace(" ", "_")+'.jpg'
	camera.capture(img_path)
	
	#maybe call logger.py here and add to database

#--------------- Event Listener --------------------------#
try:
	
	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=eventTrigger)

	while True:
	
		print(time.ctime())
		time.sleep(5)	
		

except KeyboardInterrupt:

	print("\n Program terminated.")

finally:

	GPIO.cleanup()
