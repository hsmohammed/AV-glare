import numpy as np
import pandas as pd
from pysolar.solar import *
import datetime
import pytz
import json


def is_glare_request(request):

    data = list(request.items())
    data_array = np.array(data)


    
    time = datetime.datetime.fromtimestamp(float(data_array[2][1]), pytz.utc)
    sun_altitude = get_altitude(float(data_array[0][1]), float(data_array[1][1]), time)
    sun_azimuth = get_azimuth(float(data_array[0][1]), float(data_array[1][1]), time)

    azimuth_diff = sun_azimuth-float(data_array[3][1])

    if azimuth_diff < 30 and sun_altitude < 45:
        return {'glare': True}
    else:
        return {'glare': False}     


def is_glare_ui(request):
    data = request
    data_array = data

    try:
        if  float(data_array[0][0]) <= -90:
            raise ValueError()
        if  float(data_array[0][0]) >= 90:
            raise ValueError()
        if  float(data_array[0][1]) <= -180:
            raise ValueError()
        if  float(data_array[0][1]) >= 180:
            raise ValueError()
        if  float(data_array[0][2]) <= -2208960000:
            raise ValueError()
        if  float(data_array[0][2]) >= 1609401600:
            raise ValueError()
        if  float(data_array[0][3]) <= -180:
            raise ValueError()
        if  float(data_array[0][3]) >= 180:
            raise ValueError()
    except ValueError:
        return "Invalid data ranges, check data ranges in the readme"
         


         

    
    time = datetime.datetime.fromtimestamp(float(data_array[0][2]), pytz.utc)
    sun_altitude = get_altitude(float(data_array[0][0]), float(data_array[0][1]), time)
    sun_azimuth = get_azimuth(float(data_array[0][0]), float(data_array[0][1]), time)
    
    

    azimuth_diff = sun_azimuth-float(data_array[0][3])
    
    
    if azimuth_diff < 30 and sun_altitude < 45:
        return {'glare': True}
    else:
        return {'glare': False}       


    
    