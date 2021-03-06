# checkturn.py
# Rich Hastings

import numpy as np
import math
import logging
from geopy import distance
#from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from functools import partial



def getLocation(lat, lon):

    """ helper function to get address from lat and lon

        inputs: list of latitude numbers, list of longitude numbers returns string for address
        returns string with the address
    """

    geolocator = Nominatim(user_agent="project1")  # assign nominating as your geolocator
    location = (lat, lon)
    reverse = RateLimiter(partial(geolocator.reverse, addressdetails=False, zoom=17), max_retries=5, min_delay_seconds=1)
    
    location = reverse(location)
    
    if (location != None):
        street = location.address
        street = street.split(",")
        street = street[0]
        return street
        return location.address

    else:
        # no location found
        return 1



def checkDirection(p1, p2, p3):

    """ WARNING this will not test for uturns
    Helper function that will check the direction of a turn using array cross multiplication
    takes 3 points in np arrays and returns string of direction turned or 0 if no turn was made


    future version will have a turn tolerence to detect uturn and reduce calls to service and test for uturns
    """

    a = p2-p1
    b = p3-p2

    turn = a[0]*b[1]-a[1]*b[0]
    turn = np.math.atan2(np.linalg.det([a, b]), np.dot(a, b))
    turn = (np.degrees(turn))
    if abs(turn) <15:#(turn > 0 and turn<15) or (turn<0 and turn>-15):
        #print ("no turn")
        return 0
    else:
        return turn
    """elif turn > 0:
        print ("right")
        return "right"
    elif turn < 0:
        print ("left")
        return "left"""



def getdirections(LatitudeList, LongitudeList, listSize, quesheet):

    """
    Takes a list of latitudes, longitudes, thesizeof the list and blank list of list.
    Creates a list of streets, direction turned on to street and distance traveled on street
    Returns total distance traveled
    """
    
    logging.basicConfig()
    logger = logging.getLogger("geopy")
    dist=0
    #quesheet = [[]]  # list of lists containing, street, turn direction, distance, then initialize with first location
    start = getLocation(LatitudeList[0], LongitudeList[0])
    start = start.split(",")  # will be inserted in to get location for modularity
    quesheet[0].append(start[0])
    quesheet[0].append("start")
    quesheet[0].append(
        distance.distance((LatitudeList[0], LongitudeList[0]), (LatitudeList[1], LongitudeList[1])).miles)
    queueplace = 0  # location in list that most recent turn was made
    oldPercentage = 0
    for i in range(2, listSize - 2): # iterate through list and find turns, then check if they are valid
        percentage = (i/listSize) * 100

        if (percentage != oldPercentage):
            print("{} percent complete.".format(str(round(percentage, 2))), end='\r')
            oldPercentage = percentage

        test = checkDirection(np.array([LatitudeList[i - 1], LongitudeList[i - 1]]),
                              np.array([LatitudeList[i], LongitudeList[i]]),
                              np.array([LatitudeList[i + 1], LongitudeList[i + 1]]))

        if test: # if a turn was detected check
            streetCheck = getLocation(LatitudeList[i + 1], LongitudeList[i + 1])
            streetCheck = streetCheck.split(",")
            streetCheck = streetCheck[0]

            if (streetCheck == quesheet[queueplace][0]):  # check if there was a turn or winding street. if not update distance
                if abs(test) < 130:
                    tdist = distance.distance((LatitudeList[i - 1], LongitudeList[i - 1]),
                                              (LatitudeList[i], LongitudeList[i])).miles
                    quesheet[queueplace][2] += tdist
                    dist += tdist
                else:
                    queueplace += 1
                    quesheet.append([])
                    quesheet[queueplace].append(streetCheck)
                    quesheet[queueplace].append("Uturn")
                    quesheet[queueplace].append(0)
            else: # check against next street to determine if this is a an actual turn or cross road
                streetCheckNext = getLocation(LatitudeList[i], LongitudeList[i])
                streetCheckNext = streetCheck.split(",")
                streetCheckNext = streetCheckNext[0]
                #print (streetCheckNext)
                if streetCheck == streetCheckNext:
                    queueplace += 1
                    quesheet.append([])
                    quesheet[queueplace].append(streetCheck)
                    if test>0:
                        quesheet[queueplace].append("Right")
                    else:
                        quesheet[queueplace].append("left")
                    quesheet[queueplace].append(0)


        else:
            tdist=distance.distance((LatitudeList[i - 1], LongitudeList[i - 1]),
                                                         (LatitudeList[i], LongitudeList[i])).miles
            quesheet[queueplace][2] += tdist
            dist += tdist
    #print (quesheet)
    return dist


'''
help(getLocation)
help(checkDirection)
help(getdirections)
'''