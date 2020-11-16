# routing_main.py
# Troy Clendenen

# This is the main program for the routing and geocoding
# application.

from geopy.geocoders import Nominatim
from api_keys import *
from routing_config import *

import urllib.request
import openrouteservice
import json

def getWeather(coords):

	'''
	getweather()

	Takes in coordinates and outputs a dictionary from
	a json taken from the web which shows weather info
	of a place(s).

	inputs: tuple of coordinate pairs
	outputs: dictionary

	'''

	if weather_use_boundary_box == True:
		# boundary box for finding all cities within a square on the map.
		# [lon-left,lat-bottom,lon-right,lat-top,zoom]
		
		bbox = [0,0,0,0,weather_zoom]

		# compare coordinates so we can get our boundary box.

		if (coords[0][1] <= coords[1][1]):
			bbox[0] = coords[0][1]
			bbox[2] = coords[1][1]

			if (coords[0][0] <= coords[1][0]):
				bbox[1] = coords[0][0]
				bbox[3] = coords[1][0]

			else:
				bbox[1] = coords[1][0]
				bbox[3] = coords[0][0]

		else:
			bbox[0] = coords[1][1]
			bbox[2] = coords[0][1]

			if (coords[0][0] <= coords[1][0]):
				bbox[1] = coords[0][0]
				bbox[3] = coords[1][0]

			else:
				bbox[1] = coords[1][0]
				bbox[3] = coords[0][0]

		# boundary box url
		weather_url = "https://api.openweathermap.org/data/2.5/box/city?bbox=" + str(bbox[1]) + "," + str(bbox[0]) + "," + str(bbox[3]) + "," + str(bbox[2]) + "," + str(bbox[4]) + "&units=" + units + "&appid=" + weather_api_key
		#print(weather_url)
		weather_api_obj = eval(urllib.request.urlopen(weather_url).read())

	else:
		# single-point url
		weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(coords[0][1]) + "&lon=" + str(coords[0][0]) + "&units=" + units + "&appid=" + weather_api_key
		#print(weather_url)
		weather_api_obj = eval(urllib.request.urlopen(weather_url).read())

	return weather_api_obj

def printWeather(forecast):

	'''
		printWeather()

		Prints out various weather information from the
		data returned from getWeather()

		inputs: forecast dictionary
		outputs: none

	'''

	print("### Weather Start ###")

	city = forecast["name"]
	precipitation = forecast["weather"][0]["main"]
	detailed_precipitation = forecast["weather"][0]["description"]
	temperature = forecast["main"]["temp"]
	humidity = forecast["main"]["humidity"]
	wind_speed = forecast["wind"]["speed"]
	wind_direction = forecast["wind"]["deg"]

	print("Weather in " + city + ":")
	print("Precipitation: " + precipitation + " (" + detailed_precipitation + ")")
	print("Temperature is " + str(temperature) + " degrees")
	print("Humidity is " + str(humidity) + " percent")
	print("Wind " + str(wind_speed) + " mph at " + str(wind_direction) + " degrees")

	print("### Weather End ###")
	print()

def getAQI(coords):

	'''
		getAQI()

		Takes in coordinates and outputs a dictionary from
		a json taken from the web which shows air quality info
		of a place(s).

		input: tuple of coordinate pairs
		outputs: tuple of dictionaries (start, destination)

	'''

	origin_url = "https://api.waqi.info/feed/geo:" + str(coords[0][1]) + ";" + str(coords[0][0]) + "/?token=" + aqi_api_key
	origin_aqi_obj = eval(urllib.request.urlopen(origin_url).read())

	destination_url = "https://api.waqi.info/feed/geo:" + str(coords[1][1]) + ";" + str(coords[1][0]) + "/?token=" + aqi_api_key
	destination_aqi_obj = eval(urllib.request.urlopen(destination_url).read())

	# access various parts of the json.
	# feel free to change/add whatever you feel like needs to be added.

	aqi_data = (origin_aqi_obj,destination_aqi_obj)

	return aqi_data

def printAQI(aqi_pair):

	'''
		printAQI()

		Prints out the average air quality between 2 places in the
		data returned from getAQI()

		inputs: tuple of dictionaries
		outputs: none

	'''
	print("### Air Quality Index Start ###")

	origin_aqi = aqi_pair[0]["data"]["aqi"]
	destination_aqi = aqi_pair[1]["data"]["aqi"]

	average_aqi = (origin_aqi + destination_aqi) // 2

	print("Air quality index value: " + str(average_aqi))

	if average_aqi <= 50:
		print("Good")
	elif average_aqi <= 100:
		print("Moderate")
	elif average_aqi <= 150:
		print("Unhealthy for Sensitive Groups")
	elif average_aqi <= 200:
		print("Unhealthy")
	elif average_aqi <= 300:
		print("Very Unhealthy")
	elif average_aqi <= 500:
		print("Hazardous")
	else:
		print("Extremely Hazardous")

	print("### Air Quality Index End ###")
	print()

def getRoute(coords):

	'''
		getroute()

		Get a route between 2 points using OpenRouteService
		in the form of a json dictionary

		inputs: tuple of coordinate pairs
		outputs: dictionary
	'''

	try:
		client = openrouteservice.Client(key=maps_api_key)
		routes = client.directions(coords)

	except openrouteservice.exceptions.ApiError:
		routes = 1 # could not find route

	return routes

def printRoute(route):

	'''
		printroute()

		Prints a route based on the input json file.

		input: json file of the route
		outputs: none
	'''

	print("### Direcion Start ###")

	if type(route) == dict:
		directions = (route["routes"][0]["segments"][0]["steps"])

		for element in directions:
			print(element['instruction'] + " for " + str(element['distance']) + " meters.")
	
	else:
		if route == 1:
			print("Could not find route")

		else:
			print("Something went wrong.")

	print("### Direcion End ###")
	print()

def main():

	'''
		Have the user enter 2 addresses via name,
		and return the route between them.

		Extras: Have it return information about
		air quality in the area, choose between 
		car/bike/walk/transit, 
	'''

	geolocator = Nominatim(user_agent="project1")
	queryList = []

	done = False
	while not done:

		# origin entry
		found = False
		while not found:
			entry = input("Enter start point: ")

			if entry != "":
				entry.replace(" ","")
				queryList = entry.split(",")

				location = geolocator.geocode(queryList)

				if location != None:
					origin = (location.longitude,location.latitude)
					found = True
				else:
					print("Could not find location. Did you enter it in correctly?")

			else:
				break

		if (found == False):
			done = True
			break

		# destination entry
		found = False
		while not found:
			entry = input("Enter destination: ")

			if entry != "":
				entry.replace(" ","")
				queryList = entry.split(",")

				location = geolocator.geocode(queryList)
				if location != None:
					destination = (location.longitude,location.latitude)
					found = True
				else:
					print("Could not find location. Did you enter it in correctly?")

			else:
				break

		if (found == False):
			done = True
			break
			
		coords = (origin,destination) #coordinates for our route

		'''
			This is where you can expand what data is
			retrieved with our program.

			route:
				format: json dictionary
				source: OpenRouteService

			aqi:
				format: tuple (origin json, destination json)
				source: Air Quality Open Data Platform

			weather:
				format: json dictionary
				source: OpenWeatherMap

		'''

		route = getRoute(coords)
		aqi = getAQI(coords)
		weather = getWeather(coords)

		# end_data
		###
		# print data

		printRoute(route)
		printAQI(aqi)
		printWeather(weather)

		# end printing

		#cont = input("continue? (y/n): ")
		#if cont == 'n':
			#done = True

if __name__ == "__main__":
	main()