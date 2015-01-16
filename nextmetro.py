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

STATION_ID = "N04"
DESTINATION_STATION_ID = "G05"
DESTINATION_STATION_LINE = "SV"

#####
# Get train departure JSON data from WMATA API
#####
def getTrainData():
	apiUrl = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/" + STATION_ID + "?api_key=" + os.environ.get("WMATA_API_KEY")
	r = requests.get(apiUrl)
	return r.json()

#####
# Get the time of the next train arrival, could be:
#
# -1 Unknown
# ARR Arriving
# BRD Boarding 
# >0  Minutes until it arrives
#####
def getNextTrainTime(trainJSON):
	nextTrainTime = -1
	for train in trainJSON["Trains"]:
		if (train["DestinationCode"] == DESTINATION_STATION_ID and train["Line"] == DESTINATION_STATION_LINE):
			return train["Min"]

	return nextTrainTime

def updateDisplay():
	print getNextTrainTime(getTrainData())

#####
# Entry Point
#####
if (not "WMATA_API_KEY" in os.environ):
	print "Please set environment variable WMATA_API_KEY with your API key."
	exit(1)
else:
	schedule.every(60).seconds.do(updateDisplay)
	while True:
		schedule.run_pending()
		time.sleep(1)
