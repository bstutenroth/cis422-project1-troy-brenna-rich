# parse_gpx.py
# Brenna Stutenroth

import gpxpy
import gpxpy.gpx
import sys
#https://pypi.org/project/gpxpy/00


def getCoordinatesFromFile(LatitudeList,LongitudeList,listSize, input_file):

	''' 
		getCoordinatesFromFile()
		Authors: Brenna Stutenroth, Troy Clendenen

		Helper function to parse through a gpx file and
		add latitude, longitude pairs to a list

		inputs: 2 empty lists, 0
		outputs: list of latitude values, list of longitude
		values, list size of both (should be the same)

	'''

	try:
		with open(input_file, "r") as file:
			gpx_file = gpxpy.parse(file.read()) # parse the gpx file using gpxpy

		for trk in gpx_file.tracks:
			for trkseg in trk.segments:
				count = 0 # counter for when to append lat/lon pairs
				for trkpt in trkseg.points:
					count += 1
					lat = trkpt.latitude
					lon = trkpt.longitude
					#time = trkpt.time

					LatitudeList.append(round(lat, 4)) # round the coords to a measurement
					LongitudeList.append(round(lon, 4)) # that's reasonable
					listSize += 1

	except IndexError: # an old exception when we were using command line stuff
		noFile = 1

	return listSize
