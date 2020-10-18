# Troy Clendenen
# reverse_geocoding_test.py

# This is a test program to send a request to the google maps
# api in the form of a latitude, longitude pair, and recieve
# the address.

# Library Imports
import urllib
import geopy
from geopy import distance
import numpy as np
# Code Imports
from getLocation import *
from parse_gpx import *
from checkturn import *

quesheet = [[]] #list of lists containing, street, turn directio, distance

def main(input_file, api_key):
		with open(api_key, "r") as file:
			my_api_key = file.read().replace('\n', '')

		adresses = []
		LatitudeList = []
		LongitudeList = []
		listSize = 0
		listSize = getCoordinatesFromFile(LatitudeList, LongitudeList, listSize, input_file)
		print (listSize)
		j=1
		while j < listSize:
			if (LatitudeList[j] == LatitudeList[j - 1]) and (LongitudeList[j] == LongitudeList[j-1]):
				LatitudeList.pop(j)
				LongitudeList.pop(j)
				listSize -= 1
			else:
				j += 1
		print(listSize)
		start = getLocation(LatitudeList[0], LongitudeList[0], my_api_key)
		start = start.split(",")
		quesheet[0].append(start[0])
		quesheet[0].append("start")
		quesheet[0].append(distance.distance((LatitudeList[0], LongitudeList[0]), (LatitudeList[1], LongitudeList[1])).miles)
		count=0
		print(quesheet)
		queueplace = 0
		for i in range (2,listSize-1):
			test =checkDirection(np.array([LatitudeList[i-2], LongitudeList[i-2]]), np.array([LatitudeList[i], LongitudeList[i]]), np.array([LatitudeList[i+1], LongitudeList[i+1]]))
			#print(i)
			if test != 0:
				print(test)
				streetCheck= getLocation(LatitudeList[i+1], LongitudeList[i+1], my_api_key)
				streetCheck=streetCheck.split(",")
				streetCheck=streetCheck[0]
				print(streetCheck)
				if streetCheck == quesheet[queueplace][0]:
					quesheet[queueplace][2] += distance.distance((LatitudeList[i - 1], LongitudeList[i - 1]),
														(LatitudeList[i], LongitudeList[i])).miles
				else:
					print("new street")
					streetCheckNext = getLocation(LatitudeList[i], LongitudeList[i], my_api_key)
					streetCheckNext = streetCheck.split(",")
					streetCheckNext = streetCheckNext[0]
					if streetCheck == streetCheckNext:
						queueplace += 1
						print(queueplace)
						quesheet.append([])
						quesheet[queueplace].append(streetCheck)
						quesheet[queueplace].append(test)
						quesheet[queueplace].append(0)

			else:
				quesheet[queueplace][2] += distance.distance((LatitudeList[i-1], LongitudeList[i-1]), (LatitudeList[i], LongitudeList[i])).miles
				#print(getLocation(LatitudeList[i], LongitudeList[i], my_api_key))
				print (test)


		print (count)
		print(quesheet)
		"""
		for i in range(0, listSize):
			returnVal = getLocation(LatitudeList[i], LongitudeList[i], my_api_key)

			if (returnVal == 1):
				print("No location found")

			else:
				#append all locations to a list for easier flask access
				adresses.append(returnVal)
		#sent back to main_flask to display on display.html
		return adresses"""

if __name__ == '__main__':
	main("testfile.gpx" ,"apikey.txt")

