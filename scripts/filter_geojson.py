"""

This script will generate a new geojson file that only includes tents that are located within `max_distance` miles from a given set of coordinates.

Usage: 

    >> python filter_geojson.py <path/to/geojson_data.geojson> <output_filename> <latitude> <longitude> <max_distance>

"""

from json import loads
import sys
sys.path.append('../')

from util.distances import distance_filter

INPUT_PATH, OUTPUT_FILE, LATITUDE, LONGITUDE, MAX_DISTANCE = sys.argv[1:]


def ingest_geojson(input_path):
    """
    loads input geojson into memory
    """
    with open(input_path,'r') as file: 
        return loads(file.read())


