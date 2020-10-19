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



def main(input_file, api_key):
		with open(api_key, "r") as file:
			my_api_key = file.read().replace('\n', '')

		adresses = []
		LatitudeList = []
		LongitudeList = []
		listSize = 0
		listSize = getCoordinatesFromFile(LatitudeList, LongitudeList, listSize, input_file)
		#print (listSize)
		j=1
		while j < listSize:
			if (LatitudeList[j] == LatitudeList[j - 1]) and (LongitudeList[j] == LongitudeList[j-1]):
				LatitudeList.pop(j)
				LongitudeList.pop(j)
				listSize -= 1
			else:
				j += 1
		#print(listSize)
		turns=getdirections(LatitudeList, LongitudeList, listSize, my_api_key)
		print (turns)
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

