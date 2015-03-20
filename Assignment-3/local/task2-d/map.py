#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:

    key, value = line.strip().split('        ')
    key = key.replace('KEY: ', '')
    value = value.replace('VALUE: ', '')

    medallion, hack_license, vendor_id, pickup_datetime = key.split(', ')
    rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount = value.split(', ')

    pickup_date = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

    print ("%s&%s\t%s\t%s\t%s" % (pickup_date, fare_amount, surcharge, tip_amount, tolls_amount))
