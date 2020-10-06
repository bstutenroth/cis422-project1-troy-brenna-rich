from geopy.geocoders import GoogleV3
#from geopy.geocoders import Noninatim

def getLocation(lat, lon, my_api_key):

    """ helper function to get address from lat and lon
        
        inputs: list of latitude numbers, list of longitude numbers,
        an api key
    """

    # geolocator = Nominatim(user_agent="project1") #remove comment for Nominatim

    location = str(lat) + "," + " "+str(lon)
    geolocator = GoogleV3(api_key=my_api_key) #assigns key for search
    location = geolocator.reverse(location)

    if (location != None):
    	return location.address

    else:
        # no location found
    	return 1