import requests
import pandas as pd
import argparse



parser = argparse.ArgumentParser()


parser.add_argument('latitude', type=float,
                    help='a float between -90 to 90 that shows the latitude in which the image was taken')
parser.add_argument('longitude', type=float,
                    help='a float between -180 to 180 that shows the longitude in which the image was taken')
parser.add_argument('epoch', type=float,
                    help='Linux epoch in second')
parser.add_argument('orientation', type=float,
                    help='a float between -180 to 180 the east-ward orientation of car travel from true north. 0 means north. 90 is east and -90 is west')
                

args = parser.parse_args()



def single_request(latitude, longitude, epoch, orientation):
    try:
        if  float(latitude) <= -90:
            raise ValueError()
        if  float(latitude) >= 90:
            raise ValueError()
        if  float(longitude) <= -180:
            raise ValueError()
        if  float(longitude) >= 180:
            raise ValueError()
        if  float(epoch) <= -2208960000:
            raise ValueError()
        if  float(epoch) >= 1609401600:
            raise ValueError()
        if  float(orientation) <= -180:
            raise ValueError()
        if  float(orientation) >= 180:
            raise ValueError()
    except ValueError:
        print("Invalid data ranges, check data ranges in the readme")
        return


    try:
        if not type(latitude) is float:
            raise ValueError()
        if not type(longitude) is float:
            raise ValueError()
        if not type(epoch) is float:
            raise ValueError()
        if not type(orientation) is float:
            raise ValueError()
    except ValueError:
        print("Data type must be 'float'")
        return

    base_url = 'http://localhost:5000/'
    url = base_url + str(latitude) + '/' + str(longitude) + '/' + str(epoch) + '/' + str(orientation)

    r = requests.post(url, allow_redirects=True)

    return r.json()


request1 = single_request(args.latitude, args.longitude, args.epoch, args.orientation)
print(request1)


