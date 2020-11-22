# routing_config.py
# Troy Clendenen

units = "imperial" #imperial by default, because we're Americans

# weather config
weather_language = "english" #for possible expansion to other languages
weather_use_boundary_box = False #determines if we use boundary box
weather_zoom = "50" #if using boundary box, zoom radius for finding cities within the rectangle zone
# routing config
#profile = "driving-car"
# profile can be the following:
   # driving-car (default)
   # driving-hgv
   # foot-walking
   # foot-hiking
   # cycling-regular
   # cycling-road
   # cycling-mountain
   # cycling-electric
