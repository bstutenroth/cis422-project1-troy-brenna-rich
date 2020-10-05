# Troy Clendenen
# reverse_geocoding_test.py

# This is a test program to send a request to the google maps
# api in the form of a latitude, longitude pair, and recieve
# the address.

# Library Imports
import urllib.request

# Code Imports
from getLocation import *

def oldGetLocation(coordinates):

	''' getLocation(coordinates)
	
		Takes a latitude/longitude pair, separated by a
		comma, and sends a request to the google map API
		to get the location in street form
	
		inputs: coordinates (string)
		outputs: tbd
		used by: main()
	'''
	
	apiURL = urllib.request.urlopen("https://maps.googleapis.com/maps/api/geocode/xml?latlng="+coordinates+"&key=AIzaSyDbc-uvarJSL3JSaNkyO1lCDQoawBpRdhM").read()
	#print(apiURL)

def main():

	''' main()

		The main method. Will take latitude, longitude inputs
		from the user and output an address. No input
		will close the program
	'''

	done = False
	while not done:
		# print("Enter latitude and longitude, separated by a comma.")
		# print("Like so: 40.714224,-73.961452")
		latitude = input("Enter latitude: ")
		if (latitude==""):
			done = True
		else:
			longitude = input("Enter longitude:")
			if (longitude==""):
		 		done = True
			else:
				print("Looking up location at: " + latitude + "," + longitude + " ...")
				getLocation(latitude,longitude)

main()
