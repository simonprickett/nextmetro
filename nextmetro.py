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
DESTINATION_STATION_ID = "G05"
DESTINATION_STATION_LINE = "SV"

#####
# Get train departure JSON data from WMATA API
#####
def getTrainData():
	# TODO Handle network error display error and
	# return empty Trains JSON object
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
				return train["Min"]
	else:
		if ("Error" in trainJSON):
			nextTrainTime = -99

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
	updateDisplay()
	schedule.every(60).seconds.do(updateDisplay)
	while True:
		schedule.run_pending()
		time.sleep(1)
