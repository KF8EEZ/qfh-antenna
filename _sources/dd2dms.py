import numpy as np

def dd2dms(dd):
    """
    convert decimal degrees to degrees minutes seconds
    """

    deg = float(int(dd))
    dmin = (dd-deg)*60
    min = float(int(dmin))
    dsec = (dmin-min)*60
    #sec = float(int(dsec))
    
    return np.array([deg,min,dsec])


def dms2dd(dms):
    """
    convert degrees minutes seconds to decimal degrees
    """

    deg,min,sec = dms
    dd = deg + min/60.0 + sec/3600.0
    
    return dd
