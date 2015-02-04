#####
 
# Name:    nextmetro.py
#
# Purpose: Determine when next DC Metro leaves Wiehle-Reston East station.
#          May need modification to work with non terminal station.
#
# Author:  Simon Prickett
#
#####

import os
import requests
import schedule
import time
import unicornhat as UH

API_POLL_INTERVAL = 30
MAX_CONSECUTIVE_NETWORK_ERRORS = 5
STATION_ID = "N06"
DESTINATION_STATION_ID = "G05"
DESTINATION_STATION_LINE = "SV"

consecutiveNetworkErrors = 0

#####
# Log something with a timestamp
#####
def log(logMessage):
	print time.strftime("%c") + ": " + logMessage

#####
# Get train departure JSON data from WMATA API
#####
def getTrainData():
	apiUrl = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/" + STATION_ID + "?api_key=" + os.environ.get("WMATA_API_KEY")
	try:
		r = requests.get(apiUrl)
		return r.json()
	except:
		# TODO Indicate a network error on the display
		return { "Error": "" }

#####
# Get the time of the next train arrival, could be:
#
# -99 Network error
# -1  Unknown
# ARR Arriving
# BRD Boarding 
# >0  Minutes until it arrives
#####
def getNextTrainTime(trainJSON):
	nextTrainTime = -1
	if ("Trains" in trainJSON):
		for train in trainJSON["Trains"]:
			if (train["DestinationCode"] == DESTINATION_STATION_ID and train["Line"] == DESTINATION_STATION_LINE):
				try:
					nextTrainTime = int(train["Min"])
				except:
					# Train is arriving or boarding
					nextTrainTime = 0

				return nextTrainTime
	elif ("Error" in trainJSON):
		nextTrainTime = -99

	return int(nextTrainTime)

#####
# Reboot the device as the network is down
# Displays a red X during reboot
#####
def reboot():
	log("Rebooting as network is not working...")

	ledMatrix = [[1, 0, 0, 0, 0, 0, 0, 1], 
		     	 [0, 1, 0, 0, 0, 0, 1, 0], 
	      	     [0, 0, 1, 0, 0, 1, 0, 0], 
	             [0, 0, 0, 1, 1, 0, 0, 0], 
 		     	 [0, 0, 0, 1, 1, 0, 0, 0], 
		     	 [0, 0, 1, 0, 0, 1, 0, 0], 
		     	 [0, 1, 0, 0, 0, 0, 1, 0], 
		     	 [1, 0, 0, 0, 0, 0, 0, 1]
		    	]

	for y in range(8):
		for x in range(8):
			UH.set_pixel(x, y, 255 * ledMatrix[y][x], 0, 0)

	UH.show()

	os.system("reboot")

#####
# Clear the display
#####
def clearDisplay():
	for x in range(8):
		for y in range(8):
			UH.set_pixel(x, y, 0, 0, 0)
		
		UH.show()
		time.sleep(0.2)

#####
# TODO description
#####
def updateDisplay():
	global consecutiveNetworkErrors
	nextTime = getNextTrainTime(getTrainData())
	r = 0
	g = 0
	b = 0

	if (nextTime == -1):
		# API does not know
		b = 255
		log("Unknown")
	elif (nextTime == -99):
		# Network error
		r = 128
		b = 128
		log("Network error")
		consecutiveNetworkErrors += 1

		if (consecutiveNetworkErrors == MAX_CONSECUTIVE_NETWORK_ERRORS):
			reboot()
	elif (nextTime >= 10):
		# Plenty of time
		g = 255
		log("Lots of time - " + str(nextTime) + " mins")
	elif (nextTime < 10 and nextTime > 5):
		# Pushing it
		r = 238
		g = 238
		log("Not much time - " + str(nextTime) + " mins")
	elif (nextTime >= 0 and nextTime <= 5):
		# No chance
		r = 255
		log("Not enough time - " + str(nextTime) + " mins")
	if (nextTime != -99):
		consecutiveNetworkErrors = 0

	clearDisplay()
	for y in range(8):
		for x in range(8):
			UH.set_pixel(x, y, r, g, b)
		 	time.sleep(0.05)
			UH.show()

#####
# Entry Point
#####

if (not "WMATA_API_KEY" in os.environ):
	log("Please set environment variable WMATA_API_KEY with your API key.")
	exit(1)
else:
	UH.brightness(0.3)
	updateDisplay()
	schedule.every(API_POLL_INTERVAL).seconds.do(updateDisplay)
	while True:
		schedule.run_pending()
		time.sleep(1)
