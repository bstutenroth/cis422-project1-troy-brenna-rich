
import numpy as np

def checkDirection(p1, p2, p3):
    """Helper function that will check the direction of a turn
    takes 3 points in np arrays and returns string of direction turned or 1 if no turn was made"""
    a = p2-p1
    b = p3-p2
    turn= a[0]*b[1]-a[1]*b[0]
    if turn > 0:
        return "right"
    elif turn < 0:
        return "left"
    else:
        uturn = a[0]*b[0]+a[1]*b[1]
        if uturn > 0:
            return "straight"
        elif uturn < 0:
            return "U-Turn"
        else:
            return "No Movement"

#def checkTurn(lat1, lon1, lat2, lon2): this only checks for roads that follow lat or lon and has been removed
    """helper function to determine if a turn has been made
    takes string or float of 2 points and returns 1 for turn, the lat or long that stayed the same if there is not turn
    0 for no movement"""
"""    if (float(lat1) == float(lat2)) or (float(lon1) == float(lon2)):
        if (float(lat1) == float(lat2)):
            return lat1
        elif (float(lon1) == float(lon2)):
            return lon1
        else:
            return 0
    else:
        return 1

#the following is points used for testing
lat1 = "44.5876"
lon1 = "-123.2566"
p1= np.array([44.5876, -123.2566])
lat2 = "44.5873"
lon2 = "-123.2617"
p3=np.array([44.5873, -123.2617])
turnlat="44.5876"
turnlon="-123.2617" 
p2=np.array([44.5876,-123.2617])

print (checkTurn(lat1, lon1, lat2, lon2))
print (checkDirection(p1, p2, p3))

lat1 = "44.5876"
lon1 = "-123.2566"
p1= np.array([44.5876, -123.2566])
lat2 = "44.5900"
lon2 = "-123.2617"
p3=np.array([44.5880, -123.2566])
turnlat="44.5890"
turnlon="-123.2556"
p2=np.array([44.5880, -123.2566])

#print (checkTurn(lat1, lon1, lat2, lon2))
print (checkDirection(p1, p2, p3))
"""
