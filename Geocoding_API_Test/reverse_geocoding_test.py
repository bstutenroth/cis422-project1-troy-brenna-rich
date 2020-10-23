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
from printroute import *

def main(input_file):
	
		'''
		with open(api_key, "r") as file:
			my_api_key = file.read().replace('\n', '')
		'''
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
		turns=getdirections(LatitudeList, LongitudeList, listSize)
		#print (turns)
		routelist = PrintRoute(turns)
		return routelist

