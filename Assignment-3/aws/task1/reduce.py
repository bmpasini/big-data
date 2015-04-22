#!/usr/bin/python
import sys

current_key = None
trip_data = False
fare_data = False

for line in sys.stdin:
    
    key_tag, values = line.strip().split('&', 1)
    key, tag = key_tag.strip().split('|', 1)

    if key != current_key:    
        if trip_data and fare_data:
            print ("KEY: %s        VALUE: %s" % (current_key, trip_data + ',' + fare_data))
            trip_data = False
            fare_data = False
    
    if tag == 'trip': # trip
        trip_data = values
    elif tag == 'fare': # fare
        fare_data = values
    
    current_key = key
