from geopy.geocoders import GoogleV3
#from geopy.geocoders import Noninatim

def getLocation(lat, lon):
    """helper function to get address from lat and lon"""
    # geolocator = Nominatim(user_agent="project1") #remove comment for Nominatim
    location = str(lat) + "," + " "+str(lon)
    geolocator = GoogleV3(api_key="AIzaSyDbc-uvarJSL3JSaNkyO1lCDQoawBpRdhM") #assigns key for search
    location = geolocator.reverse(location)

    if (location != None):
    	print(location.address)
    	return location.address
    else:
    	print("No location found...")
    	return 1