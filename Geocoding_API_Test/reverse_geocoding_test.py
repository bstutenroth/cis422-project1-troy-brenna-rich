# Troy Clendenen
# reverse_geocoding_test.py

# This is a test program to send a request to a geocoding
# api in the form of a latitude, longitude pair, and recieve
# the address(es).

# Library Imports
import urllib
import geopy
from geopy import distance
import numpy as np
from datetime import timedelta

# Code Imports
from getLocation import *
from parse_gpx import *
from checkturn import *
from printroute import *


def main(input_file):
	
	'''
		main()
		Authors: Troy Clendenen, Rich Hastings

		The main method for our reverse geocoding program.
		It creates a list of coordinates from a gpx file,
		and then uses a geocoding api to find the locations
		that were travelled to and puts them in a list as
		a tuple.

		inputs: a string of the gpx file that will be read.
		outputs: a list of tuples that have all of the places
		gone on the route.
	'''

		# leftover from when we were using an api key from a text file
		# with open(api_key, "r") as file:
		# my_api_key = file.read().replace('\n', '')

	LatitudeList = [] # list to store latitude values
	LongitudeList = [] # list to store longitude values
	turns = [[]]
	listSize = 0
	calcount = ""
	time = getCoordinatesFromFile(LatitudeList, LongitudeList, listSize, input_file)
	listSize = len(LatitudeList)
	print(time.total_seconds()//3600)
	j=1
	while j < listSize:
		if (LatitudeList[j] == LatitudeList[j - 1]) and (LongitudeList[j] == LongitudeList[j-1]):
			LatitudeList.pop(j)
			LongitudeList.pop(j)
			listSize -= 1

		else:
			j += 1

	dist=getdirections(LatitudeList, LongitudeList, listSize, turns) # construct the route as a list
	print(dist)
	routelist = PrintRoute(turns) # print the route
	if time == None:
		calcount += "Time not tracked in this GPX file we couldn't find your average speed or calorie count"
	else:
		hrs=time.total_seconds()/3600
		avespeed= dist/hrs
		calburn = time.total_seconds() // 3600 * 240
		calcount="On this trip you traveled at an average speed of "\
			+ str(round(avespeed, 2)) + " miles per hour\n" \
			"You burned aproxinately " + str(calburn) + " calories"



	routelist.append(calcount)
	for entry in routelist: # print the route to the console, comment out if needed
		print(entry)

	return routelist

if __name__ == "__main__":
	main("testfile.gpx")
