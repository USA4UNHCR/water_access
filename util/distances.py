"""

Utility of functions for calculating and filtering based on distances.

"""

from haversine import haversine

def distance_filter(coord1,coord2,max_distance):
    """
    filter function that returns True or False depending on whether the cood1 and coord2 
    coordinates are within max_distance miles from each other.

    Example: 
    >> coord1 = (0,90) # north pole
    >> coord2 = (0,0) # somewhere in africa
    >> distance_filter(coord1,coord2,max_distance=12) 
    False

    """

    if haversine(coord1,coord2,miles = True) > max_distance:
        return False
    else:
        return True


