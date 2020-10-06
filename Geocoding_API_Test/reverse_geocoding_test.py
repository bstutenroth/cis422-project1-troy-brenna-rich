# Troy Clendenen
# reverse_geocoding_test.py

# This is a test program to send a request to the google maps
# api in the form of a latitude, longitude pair, and recieve
# the address.

# Library Imports
import urllib.request

# Code Imports
from getLocation import *
from parse_gpx import *

def main():

	''' main()

		The main method. Will take latitude, longitude inputs
		from the user and output an address. No input
		will close the program
	'''

	# This is the coordinate list that holds a string
	# 'latitude,longitude' at each entry.

	if len(sys.argv) > 1:

		# basic error handling
		if (len(sys.argv) == 2):
			print("Incorrect number of arguments")

		elif (len(sys.argv) > 3):
			print("Incorrect number of arguments")

		else:
			with open(sys.argv[2], "r") as file:
				my_api_key=file.read().replace('\n','')

			LatitudeList = []
			LongitudeList = []
			listSize = 0
			listSize = getCoordinatesFromFile(LatitudeList,LongitudeList,listSize)

			for i in range(0,listSize):
				returnVal = getLocation(LatitudeList[i],LongitudeList[i],my_api_key)

				if (returnVal == 1):
					print("No location found")

				else:
					print(returnVal)

	# this else statement shouldn't be used
	# use the .bat file to run the program instead
	
	else:

		done = False	
		while not done:

			my_api_key = input("Enter a valid api key: ")
			if (my_api_key==""):
				done = True
				break

			latitude = input("Enter latitude: ")
			if (latitude==""):
				done = True

			else:
				longitude = input("Enter longitude:")
				if (longitude==""):
			 		done = True

				else:
					print("Looking up location at: " + latitude + "," + longitude + " ...")
					returnVal = getLocation(latitude,longitude)
					if (returnVal == 1):
						print("No Location Found")

					elif (returnVal == 2):
						print("Invalid API key")

					else:
						print(returnVal)
main()
