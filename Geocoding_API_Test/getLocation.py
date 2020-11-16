#from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim

def getLocation(lat, lon):

   """ 
	getLocation()

   helper function to get address from lat and lon. Uses
   a geocoding service (currently Nominatim).
        
   inputs: list of latitude numbers, list of longitude numbers
   outputs: returns a string if an address was found, 1 if not
   """

   geolocator = Nominatim(user_agent="project1") #remove comment for Nominatim
   #geolocator = GoogleV3(my_api_key) # remove comment for Google Maps

   location = str(lat) + ", " +str(lon) # properly format our lat/lon input

   try:
      location = geolocator.reverse(location, addressdetails=False, zoom=16)
   except (GeocoderUnavailable, GeocoderTimedOut):
      print("geocoder is not accepting requests,please try again later")

   if (location != None):
    	# location found
      return location.address

   else:
      # no location found
    	return 1