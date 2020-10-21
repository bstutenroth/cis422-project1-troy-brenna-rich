# cis422-project1-troy-brenna-rich

What we're doing:

    This project uses google maps api to reverse geocode.
    The user inputs a .gpxpy file on the web service (only files
    of this type will be allowed).  Then we take this file along
    with a file containing our api key, and run main() with those
    files as arguments.

    Main will then open the gpx file for reading and parse the file
    using gpxpy to get the coordinates.  Then using geopy and the
    Nominatim API, we return a list of street names and the turns made.

    These directions are then parsed and posted to display.html for
    the user to view.

Installation: 

    Before running the code, make sure to have the following installed in the
    same directory as your python modules:
    (if you have pip installed, go ahead and use the below commands to install)
    geopy : pip install geopy
    gpxpy : pip install gpxpy
    flask : pip install flask
    numpy : pip install numpy
    You will also need an apikey.  This must be placed into a file within the folder "Geocoding_API_Test"
    named "apikey.txt"


How to Use:

    First, follow the installation instructions above.  Once that has been
    completed, go into the Geocoding_API_Test file and run the following in your terminal:
    if you're using Unix Bash(Linux, Mac, etc.):
        $ export FLASK_APP=main_flask.py
        $ flask run
    If you're using Windows CMD:
        > set FLASK_APP=main_flask
        > flask run
    If you're using Windows Powershell:
        > $env:FLASK_APP = "main_flask"
        > flask run
    Then follow the provided link to the webpage.  Here, you can upload your gpx file
    and get the route for your bike ride returned to you.



