from geopy.geocoders import GoogleV3

def getLocation(lat, lon):
    location=str(lat) + "," + " "+lon
    geolocator = GoogleV3(api_key="AIzaSyDbc-uvarJSL3JSaNkyO1lCDQoawBpRdhM") #assigns key for search
    location = geolocator.reverse((location))
    return location.address

