# printroute.py

def PrintRoute(routelist):

	# routelist = []
	# routelist.append(('Quai du Marechal Foch', 'start', 0.04113949999759449))
	# routelist.append(("Quai d'Aiguillon", 'right', 0))
	# routelist.append(('Kermaria', 'right', 0))
	# routelist.append(("Quai d'Aiguillon", 'right', 0))
	# routelist.append(('Pont Sainte-Anne', 'right', 0))
	# routelist.append(('Quai du Maréchal Foch', 'right', 0))
	# routelist.append(('Avenue du Général de Gaulle', 'left', 0.024855294706737124))

	currentRoad = None # this will store our current road we are travelling on

	for entry in routelist:

		if (entry[2] != 0):
			if (currentRoad != None):
				if (currentRoad[0] == entry[0]):
					currentRoad[2] += entry[2] # add the distance continued on this road

				else:
					print(currentRoad[1] + " on " + currentRoad[0] + " for " + str(round(currentRoad[2],2)) + " miles.")
					currentRoad = entry

			else:
				currentRoad = entry

	print(currentRoad[1] + " on " + currentRoad[0] + " for " + str(round(currentRoad[2],2)) + " miles.")

#PrintRoute()