# printroute.py

def PrintRoute(routelist):

	currentRoad = None # this will store our current road we are travelling on
	route = []
	for entry in routelist:

		if (entry[2] != 0):
			if (currentRoad != None):
				if (currentRoad[0] == entry[0]):
					currentRoad[2] += entry[2] # add the distance continued on this road

				else:
					route.append(currentRoad[1] + " on " + currentRoad[0] + " for " + str(round(currentRoad[2],2)) + " miles.")
					currentRoad = entry

			else:
				currentRoad = entry

	route.append(currentRoad[1] + " on " + currentRoad[0] + " for " + str(round(currentRoad[2],2)) + " miles.")
	return route

#PrintRoute()