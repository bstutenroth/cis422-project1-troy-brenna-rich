import math

def checkDirection(lat1, lon1, lat2, lon2):
    """Helper function that will check the direction of a turn
    takes string or float of 2 points and returns string of direction turned of 1 if no turn was made"""
    turn = abs(float(lat1))*abs(float(lon2))-abs(float(lon1))*abs(float(lat2))
    print(turn)
    if turn < 0:
        return "right"
    elif turn > 0:
        return "left"
    else:
        return 1

def checkTurn(lat1, lon1, lat2, lon2):
    """helper function to determine if a turn has been made
    takes string or float of 2 points and returns 1 for turn and 0 for no turn"""
    if (float(lat1) == float(lat2)) or (float(lon1) == float(lon2)):
        return 0
    else:
        return 1


lat1 = "44.5876"
lon1 = "-123.2566"
lat2 =  "44.5880" 
lon2 = "-123.2617"

print (checkTurn(lat1, lon1, lat2, lon2))
print (checkDirection(lat1, lon1, lat2, lon2))