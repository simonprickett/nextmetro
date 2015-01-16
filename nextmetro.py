#####
#
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
#import unicornhat as UH

STATION_ID = "N06"
DESTINATION_STATION_ID = "G05"
DESTINATION_STATION_LINE = "SV"

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
# TODO description
#####
def updateDisplay():
	nextTime = getNextTrainTime(getTrainData())
	r = 0
	g = 0
	b = 0

	if (nextTime == -1):
		# API does not know
		b = 255
		print "Unknown"
	elif (nextTime == -99):
		# Network error
		r = 128
		b = 128
		print "Network error"
	elif (nextTime >= 10):
		# Plenty of time
		g = 255
		print "Lots of time - " + str(nextTime) + " mins"
	elif (nextTime < 10 and nextTime > 5):
		# Pushing it
		r = 255
		g = 255
		print "Not much time - " + str(nextTime) + " mins"
	elif (nextTime >= 0 and nextTime <= 5):
		# No chance
		r = 255
		print "Not enough time - " + str(nextTime) + " mins"

#	for y in range(8):
#		for x in range(8):
#			UH.set_pixel(x, y, r, g, b)
#
#	UH.show()

#####
# Entry Point
#####
if (not "WMATA_API_KEY" in os.environ):
	print "Please set environment variable WMATA_API_KEY with your API key."
	exit(1)
else:
	updateDisplay()
	schedule.every(60).seconds.do(updateDisplay)
	while True:
		schedule.run_pending()
		time.sleep(1)
