import numpy as np
import logging
from geopy import distance
#from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from functools import partial



def getLocation(lat, lon):
    """ helper function to get address from lat and lon

        inputs: list of latitude numbers, list of longitude numbers,
        an api key
    """

    geolocator = Nominatim(user_agent="project1")  # remove comment for Nominatim
    location = (lat, lon)
    reverse = RateLimiter(partial(geolocator.reverse, addressdetails=False, zoom=17), max_retries=5, min_delay_seconds=1)
    # geolocator = GoogleV3(my_api_key) #assigns key for search
    location=reverse(location)
    # geolocator = GoogleV3(my_api_key) #assigns key for search
    #try:
        #except (GeocoderUnavailable, GeocoderTimedOut):
    #print("geocoder is not accepting requests,please try again later")

    if (location != None):
        return location.address

    else:
        # no location found
        return 1


def checkDirection(p1, p2, p3):
    """Helper function that will check the direction of a turn
    takes 3 points in np arrays and returns string of direction turned or 1 if no turn was made"""
    #print(p1)
    #print(p2)
    #print(p3)
    a = p2-p1
    b = p3-p2
    #print (a)
    #print (b)
    turn= a[0]*b[1]-a[1]*b[0]
    if turn > 0:
        return "right"
    elif turn < 0:
        return "left"
    else:
        return 0
        """uturn = a[0]*b[0]+a[1]*b[1]
        if uturn > 0:
            return "straight"
        elif uturn < 0:
            return "U-Turn"
        else:
            return "No Movement"""

def getdirections(LatitudeList, LongitudeList, listSize):
    """
    Takes a list of latitudes, longitudes, thesizeof the list and a given api key.
    Creates a list of streets, direction turned on to street and distance traveled on street
    """
    logging.basicConfig()
    logger = logging.getLogger("geopy")
    quesheet = [[]]  # list of lists containing, street, turn direction, distance
    start = getLocation(LatitudeList[0], LongitudeList[0])
    start = start.split(",")
    quesheet[0].append(start[0])
    quesheet[0].append("start")
    quesheet[0].append(
        distance.distance((LatitudeList[0], LongitudeList[0]), (LatitudeList[1], LongitudeList[1])).miles)
    queueplace = 0
    oldPercentage = 0
    for i in range(2, listSize - 2):
        percentage = (i/listSize) * 100
        if (percentage != oldPercentage):
            print("{} percent complete.".format(str(round(percentage, 2))), end='\r')
            oldPercentage = percentage

        if i % 10 == 0:
            percentage = i/listSize
            print("Calculating "+str(i)+ " records") #str(round(percentage)))
        test = checkDirection(np.array([LatitudeList[i - 1], LongitudeList[i - 1]]),
                              np.array([LatitudeList[i], LongitudeList[i]]),
                              np.array([LatitudeList[i + 1], LongitudeList[i + 1]]))
        # print(i)
        if test != 0:
            # print(test)
            streetCheck = getLocation(LatitudeList[i + 1], LongitudeList[i + 1])
            streetCheck = streetCheck.split(",")
            streetCheck = streetCheck[0]
            # print(streetCheck)
            if streetCheck == quesheet[queueplace][0]:
                quesheet[queueplace][2] += distance.distance((LatitudeList[i - 1], LongitudeList[i - 1]),
                                                             (LatitudeList[i], LongitudeList[i])).miles
            else:
                # print("new street")
                streetCheckNext = getLocation(LatitudeList[i], LongitudeList[i])
                streetCheckNext = streetCheck.split(",")
                streetCheckNext = streetCheckNext[0]
                if streetCheck == streetCheckNext:
                    queueplace += 1
                    # print(queueplace)
                    quesheet.append([])
                    quesheet[queueplace].append(streetCheck)
                    quesheet[queueplace].append(test)
                    quesheet[queueplace].append(0)

        else:
            quesheet[queueplace][2] += distance.distance((LatitudeList[i - 1], LongitudeList[i - 1]),
                                                         (LatitudeList[i], LongitudeList[i])).miles
        # print(getLocation(LatitudeList[i], LongitudeList[i], my_api_key))
        # print (test)

    return quesheet
