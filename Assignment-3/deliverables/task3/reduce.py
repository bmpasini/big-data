#!/usr/bin/python
import sys

current_medallion = None
vehicle_data = False
trip_fares = []

for line in sys.stdin:
    
    tag_medallion, values = line.strip().split('&', 1)
    medallion, tag = tag_medallion.strip().split(',', 1)

    if medallion != current_medallion:
        for trip_fare in trip_fares:
            if vehicle_data:
                print ("KEY: %s        VALUE: %s" % (current_medallion, trip_fare + ',' + vehicle_data))
                trip_fares = []
                vehicle_data = False
    
    if tag == 'trip_fare': # task1 - 1st in output
        trip_fares.append(values)
    elif tag == 'license': # license
        vehicle_data = values
    
    current_medallion = medallion