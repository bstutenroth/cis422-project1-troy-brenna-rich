# cis422-project1-troy-brenna-rich

What we're doing:

    This project uses google maps api to reverse geocode.
    The user inputs a .gpxpy file on the web service (only files
    of this type will be allowed).  Then we take this file along
    with a file containing our api key, and run main() with those
    files as arguments.

    Main will then open the gpx file for reading and parse the file
    using gpxpy to get the coordinates.  Then using geopy and the
    Google maps API, we return a list of addresses

    These addresses are then parsed and posted to display.html for
    the user to view.

Installation:
How to use:

The Geocoding_API_Test folder contains the files needed
to test out reverse geocoding using the google maps API.

(Use Run Test.bat to run it. Make sure that you have a
file named apikey.txt with a valid api key)

Make sure you've installed gpxpy to your computer,
wherever you store your python modules.