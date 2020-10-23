# cis422-project1-troy-brenna-rich

Troy Clendenen
Brenna Stutenroth
Rich Hastings

What we're doing:

    Important note about Nominatim:
    In this project we are using the Nominatim server for all tests. Using the remote server slows down the project and has the potential of connection errors.
    In a production enviroment Nominatim would be placed on the server with commincation though appache.
    The production approach would allow for almost instant ppcoessing, no sever timeouts and multi-threading.
    This would allow us to change a route that takes us 20-30 minutes to process to be completed in under a minute.
    The process to complete the production build can be found at https://nominatim.org/release-docs/latest/admin/Installation/
    The choice to use the slower less stable service was due to Nominatim taking 800gb of data. It is our belief that the one time user would rather have a wait time of 2-30 minutes depending upon route than a several day installation.

    We have designed an algorithm which charts the route and only checks for street changes at the turns. This is done to reduce external calls which:
    1. reduces chances of external error.
    2. Allows for the user to use a paid service such as google. Reduced calls means reduced payments to the service provider.

    The user inputs a .gpx file on the web service (only files
    of this type will be allowed).  Then we take this file and run main() with that
    file as an argument.

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

    (Alternatively, on Windows, if you have all of the modules installed, we haven't streamlined this way of using, but in "reverse_geocoding_test.py", if you change the name of the gpx file at the bottom when it calls main(<gpxfilename>) to a gpx
    file in the current folder, press Run Test.bat, and it will find the route
    in the command line. A bash version of this same script is planned for future testing.)

Known Issues:

    Riding on unmark street or bikepath will default to closest known street. This can cause impossible routes.
    May not detect change in road name. Will show where you turned and how long you travel on said road.
    Will not detect U-turns, This can cause extended milage on road or turn direction other than expected.
    Possibility of time out from Nominatim causing incorrect routing.
        - We have error handling for this mostly working. While the screen
          may be filled with error messages (Depending on the terminal),
          the program will continue to retry (as long as you see the progess
          bar updating, all should be working)

Future possible upgrades:

    Store routes and:
    Allow the user to compare routes with friends. This way they can see who does the route is the fastest time.
    Give approximate burned calorie.
    Compare route to air quality so that a user can determine if they want to take a known route before setting out.

    Show interesting locations close to route so that user can plan next route accordingly.
    Suggest future route that is easier/more difficult based upon elevation.
    Compare route with typical car traffic and suggest the safest time to take the route.

    Overall make installation easier, such as easier module install, cleaner looking
    website, flexibility in where the program is run, etc.
