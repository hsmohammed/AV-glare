# from model import is_glare_request
# import requests

# base_url = 'http://localhost:5000/'
# url = base_url + str(-200) + '/' + str(1) + '/' + str(1) + '/' + str(1)

# r = requests.post(url, allow_redirects=True)

# print(r.json())






# def is_glare_request(request):

#     data = list(request.items())
#     data_array = np.array(data)

    try:
        if not float(data_array[0][1]) >= -90:
            raise ValueError()
        if not float(data_array[0][1]) <= 90:
            raise ValueError()
        if not float(data_array[1][1]) >= -180:
            raise ValueError()
        if not float(data_array[1][1]) <= 180:
            raise ValueError()
        if not float(data_array[2][1]) >= -2208960000:
            raise ValueError()
        if not float(data_array[2][1]) <= 1609401600:
            raise ValueError()
        if not float(data_array[3][1]) >= -180:
            raise ValueError()
        if not float(data_array[3][1]) >= 180:
            raise ValueError()
    except ValueError:
        print("Invalid data ranges, check data ranges in the readme")

#     # try:
#     #     type(data_array[0][1]) = '<class 'float'>'
#     #     type(data_array[0][1]) = '<class 'float'>''
#     #     type(data_array[1][1]) = '<class 'float'>'
#     #     type(data_array[1][1]) = '<class 'float'>'
#     #     type(data_array[2][1]) = '<class 'float'>'
#     #     type(data_array[2][1]) = '<class 'float'>'
#     #     type(data_array[3][1]) = '<class 'float'>'
#     #     type(data_array[3][1]) = '<class 'float'>'
#     # except:
#     #     print("Data type must be 'float'")
    
#     time = datetime.datetime.fromtimestamp(float(data_array[2][1]), pytz.utc)
#     sun_altitude = get_altitude(float(data_array[0][1]), float(data_array[1][1]), time)
#     sun_azimuth = get_azimuth(float(data_array[0][1]), float(data_array[1][1]), time)

#     azimuth_diff = sun_azimuth-float(data_array[3][1])

#     if azimuth_diff < 30 and sun_altitude < 45:
#         return {'glare': True}
#     else:
#         return {'glare': False}     




a = -200
try:
    if not float(a) >= -90:
        raise ValueError()
    if not float(a) <= 90:
        raise ValueError()
except ValueError:
    print("Invalid data ranges, check data ranges in the readme")

