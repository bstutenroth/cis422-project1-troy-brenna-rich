import gpxpy
import gpxpy.gpx
import sys
#https://pypi.org/project/gpxpy/00


def getCoordinatesFromFile(LatitudeList,LongitudeList,listSize, input_file):

	''' Helper function to parse through a gpx file and
		add latitude, longitude pairs to a list

		inputs: 2 empty lists, 0
		outputs: list of latitude values, list of longitude
		values, list size of both (should be the same)

	'''

	try:
		with open(input_file, "r") as file:
			gpx_file = gpxpy.parse(file.read())

		for trk in gpx_file.tracks:
			for trkseg in trk.segments:
				count = 0 # counter for when to append lat/lon pairs
				for trkpt in trkseg.points:
					count += 1
					lat = trkpt.latitude
					lon = trkpt.longitude
					#time = trkpt.time
					#print('Latitude: {0}, Longitude: {1}, Time: {2}'.format(trkpt.latitude, trkpt.longitude, trkpt.time))
					
					'''
					This if statement ensures that we aren't going over the
					alloted calls to google maps API. I don't wanna spend
					200 bucks accidentally lol
					'''
					
					#if (count == 2000):
						#break
					LatitudeList.append(round(lat, 4))
					LongitudeList.append(round(lon, 4))
					listSize += 1
					#count = 0
						#print('{0},{1}'.format(trkpt.latitude, trkpt.longitude))

	except IndexError:
		noFile = 1
	return listSize
