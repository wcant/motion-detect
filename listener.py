#!/usr/bin/python

import RPi.GPIO as GPIO
import picamera
import gps
import time
import sqlite3
import os.path

dbcon = sqlite3.connect('motion.db',check_same_thread=False)
cursor = dbcon.cursor()

camera = picamera.PiCamera()

#--------------- GPIO Setup ------------------------------#

GPIO.setmode(GPIO.BCM)

#listen on pin 4 for PIR
PIR_PIN = 22

# Logically Low by default
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#--------------- GPS -------------------------------------#

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

#--------------- Event Callback --------------------------#

def eventTrigger(channel):

	print("Motion Detected")

	#Get time string and remove unfriendly characters
	time_str = time.ctime()
	time_str = time_str.replace(" ", "")
	time_str = time_str.replace(":", "")
	img_path = '/usr/share/nginx/www/images/'+time_str+'.jpg'

	camera.capture(img_path)

	#get image ready for insert
	
	day = time_str[0:3]
	mon = time_str[3:6]
	dayn = time_str[6:8]
	hour = time_str[8:10]
	minu = time_str[10:12]
	sec = time_str[12:14]
	year = time_str[14:19]
	print(time_str)

#	list_to_write = [day,dayn,mon,year,hour,minu,sec]	
	cursor.execute("INSERT INTO log VALUES (NULL, "+day+","+dayn+","+mon+","+year+","+hour+","+minu+","+sec+","+"NULL"+","+img_path+");")	
	cursor.commit()
	cursor.close()
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
