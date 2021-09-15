import requests
import pandas as pd
import argparse
import numpy as np


parser = argparse.ArgumentParser()

parser.add_argument('csv_file', type=str,
                    help='location of a csv containing metadata')

args = parser.parse_args()

def single_request1(latitude, longitude, epoch, orientation):

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
        if not (type(latitude) is np.float64):
            raise ValueError()
        if not (type(longitude) is np.float64):
            raise ValueError()
        if not (type(epoch) is np.float64):
            raise ValueError()
        if not (type(orientation) is np.float64):
            raise ValueError()
    except ValueError:
        print("Data type must be 'float'")
        return

    base_url = 'http://localhost:5000/'
    url = base_url + str(latitude) + '/' + str(longitude) + '/' + str(epoch) + '/' + str(orientation)

    r = requests.post(url, allow_redirects=True)

    return r.json()


def multiple_requests(csv_file):

    request_df = pd.read_csv(csv_file)
    request_df.columns = ['latitude', 'longitude', 'epoch', 'orientation']
    responses = []
    for i in range(len(request_df)):

        response = single_request1(request_df['latitude'][i], request_df['longitude'][i], request_df['epoch'][i], request_df['orientation'][i])
        responses.append(response)

    request_df['responses'] = responses
    request_df.to_csv('data_with_responses.csv')

    return request_df


request1 = multiple_requests(str(args.csv_file))
print(request1)


request1 = multiple_requests('metadata.csv')
print(request1)

