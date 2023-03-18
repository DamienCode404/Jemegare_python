#!/usr/bin/env python3

from math import radians, cos, sin, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    """
    Retourne la distance en kilomètres entre deux points.

    On utilise la [formule de Haversine](https://fr.wikipedia.org/wiki/Formule_de_haversine)
    pour déterminer la distance orthodromique entre les points de coordonnées 
    (`lat1`,`lon1`) et (`lat2`, `lon2`), où `lat1` et `lat2` sont les latitudes et `lon1` 
    et `lon2` les longitudes. Latitudes et longitudes sont exprimées en degrés.

    Source du code: https://www.geeksforgeeks.org/program-distance-two-points-earth/ 
    """
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
    # calculate the result
    return(c * r)


if __name__ == "__main__":
    print(f"La distance entre les parkings 'Tour Bretagne' et 'Hôtel Dieu' est de {distance(-1.5582500169999776,47.21784288800001,-1.5519831099999806,47.21105707999999)} km.")
