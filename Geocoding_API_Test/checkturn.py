import numpy as np


def checkDirection(p1, p2, p3):
    """Helper function that will check the direction of a turn
    takes 3 points in np arrays and returns string of direction turned or 1 if no turn was made"""
    #print(p1)
    #print(p2)
    #print(p3)
    a = p2-p1
    b = p3-p2
    #print (a)
    #print (b)
    turn= a[0]*b[1]-a[1]*b[0]
    if turn > 0:
        return "right"
    elif turn < 0:
        return "left"
    else:
        return 0
        """uturn = a[0]*b[0]+a[1]*b[1]
        if uturn > 0:
            return "straight"
        elif uturn < 0:
            return "U-Turn"
        else:
            return "No Movement"""""