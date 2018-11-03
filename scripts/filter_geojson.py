"""

This script will generate a new geojson file that only includes tents that are located within `max_distance` miles from a given set of coordinates.

Usage: 

    >> python filter_geojson.py <path/to/geojson_data.geojson> <output_filename> <latitude> <longitude> <max_distance>

"""

import sys
sys.path.append('../')

from json import loads, dumps
from util.distances import distance_filter

def get_geojson_data(PATH):
    with open(PATH,'r') as file:
        return loads(file.read())


def get_filtered_geojson(input_paths,center_location,max_distance):
    """
    Returns filtered geojson
    
    center_location (latitude, longitude)
    input_paths
    max_distance (in miles)
    
    """
    if type(input_paths) != list:
        input_paths = [input_paths]
        
    feature_count = 0
    print("features within range: %i" % feature_count,end='\r')
    for input_path in input_paths:
        input_geojson = get_geojson_data(input_path)
        filtered_geojson = get_geojson_data(input_path)
        filtered_geojson['features'] = []

        for feature in input_geojson['features']:
            coordinates = feature['geometry']['coordinates'][::-1]
            if distance_filter(coordinates,center_location,max_distance):
                filtered_geojson['features'] += [feature]
                feature_count += 1
                print("features within range: %i" % feature_count,end='\r')

        return filtered_geojson

    
if __name__ == '__main__':
    INPUT_PATH = 'data/original/africa1.geojson'
    CENTER_LOCATION = (3.734,18.761778)
    MAX_DISTANCE = 25
    OUTPUT_PATH = "LAT%1.5f_LON%1.5f_RANGE%1.3f" % (CENTER_LOCATION[0],CENTER_LOCATION[1],MAX_DISTANCE)
    OUTPUT_PATH = '../' + OUTPUT_PATH.replace('.','D') + '.json'
    
    fg = get_filtered_geojson(INPUT_PATH,CENTER_LOCATION,MAX_DISTANCE)
    with open(OUTPUT_PATH,'w') as file:
        file.write(dumps(fg))
        print("\nWritten to: %s" % OUTPUT_PATH)
