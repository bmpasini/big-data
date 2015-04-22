#!/usr/bin/python
import sys
 
for line in sys.stdin:

    line = line.strip().split(',')
    
    if len(line) == 11: # fare
        medallion = line[0] if len(line) > 0 else ''
        hack_license = line[1] if len(line) > 1 else ''
        vendor_id = line[2] if len(line) > 2 else ''
        pickup_datetime = line[3] if len(line) > 3 else ''
        payment_type = line[4] if len(line) > 4 else ''
        fare_amount = line[5] if len(line) > 5 else ''
        surcharge = line[6] if len(line) > 6 else ''
        mta_tax = line[7] if len(line) > 7 else ''
        tip_amount = line[8] if len(line) > 8 else ''
        tolls_amount = line[9] if len(line) > 9 else ''
        total_amount = line[10] if len(line) > 10 else ''
        
        print ('%s,%s,%s,%s|fare&%s,%s,%s,%s,%s,%s,%s' % (medallion, hack_license, vendor_id, pickup_datetime, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount))
    elif len(line) == 14: # trip
    	medallion = line[0] if len(line) > 0 else ''
    	hack_license = line[1] if len(line) > 1 else ''
    	vendor_id = line[2] if len(line) > 2 else ''
    	rate_code = line[3] if len(line) > 3 else ''
    	store_and_fwd_flag = line[4] if len(line) > 4 else ''
    	pickup_datetime = line[5] if len(line) > 5 else ''
    	dropoff_datetime = line[6] if len(line) > 6 else ''
    	passenger_count = line[7] if len(line) > 7 else ''
    	trip_time_in_secs = line[8] if len(line) > 8 else ''
    	trip_distance = line[9] if len(line) > 9 else ''
    	pickup_longitude = line[10] if len(line) > 10 else ''
    	pickup_latitude = line[11] if len(line) > 11 else ''
    	dropoff_longitude = line[12] if len(line) > 12 else ''
    	dropoff_latitude = line[13] if len(line) > 13 else ''

        print ('%s,%s,%s,%s|trip&%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (medallion, hack_license, vendor_id, pickup_datetime, rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude))
