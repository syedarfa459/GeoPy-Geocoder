from django.contrib.gis.geoip2 import GeoIP2


#creating my project helper functions here


def get_center_coordinates(latA, longA, latB=None, longB=None):
    cord = (latA, longA)
    if latB:
        cord = [(latA+latB)/2, (longA+longB)/2]
    return cord

def get_zoom(distance):

    if distance <= 100:
        return 9
    elif distance > 100 and distance <= 2500:
        return 5
    elif distance > 2501 and distance <= 3000:
        return 3
    else:
        return 2

