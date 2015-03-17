#!/usr/bin/python
import sys

trip_k = ''
fare_k = ''

for line in sys.stdin:
    
    line = line.strip().split('\t')

    if len(line) == 14: # trip - 1st
        medallion, hack_license, vendor_id, pickup_datetime, rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude = line
        trip_k = ', '.join([medallion, hack_license, vendor_id, pickup_datetime])
        trip_v = ', '.join([rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude])

    elif len(line) == 11: # fare
        medallion, hack_license, vendor_id, pickup_datetime, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount = line
        fare_k = ', '.join([medallion, hack_license, vendor_id, pickup_datetime])
        fare_v = ', '.join([payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount])
    
    if trip_k == fare_k and trip_k != "medallion, hack_license, vendor_id, pickup_datetime":
        v = trip_v + ', ' + fare_v
        print ("KEY: %s        VALUE: %s" % (trip_k, v))
