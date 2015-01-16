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

STATION_ID = "N06"

#####
# Get train departure JSON data from WMATA API
#####
def getTrainData():
	apiUrl = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/" + STATION_ID + "?api_key=" + os.environ.get("WMATA_API_KEY")
	r = requests.get(apiUrl)
	return r.json()

#####
# Get the time of the next train
#####
def getNextTrainTime(trainJSON):
	nextTrainTime = -1
	for train in trainJSON["Trains"]:
		# https://developer.wmata.com/docs/services/547636a6f9182302184cda78/operations/547636a6f918230da855363f

	return nextTrainTime

#####
# Entry Point
#####

if (not "WMATA_API_KEY" in os.environ):
	print "Please set environment variable WMATA_API_KEY with your API key."
	exit(1)
else:
	getNextTrainTime(getTrainData())


#schedule.every(30).seconds.do(updateDisplay)
#while True:
#	schedule.run_pending()
#	time.sleep(1)
