#!/usr/bin/python
import sys
import csv
import StringIO
 
for line in sys.stdin:
    key, value = line.strip().split('        ')
    key = key.replace('KEY: ', '')
    value = value.replace('VALUE: ', '')
    values = value.split(', ')

    medallion = key
    hack_license = values[0] if len(values) > 0 else ''
    vendor_id = values[1] if len(values) > 1 else ''
    pickup_datetime = values[2] if len(values) > 2 else ''
    rate_code = values[3] if len(values) > 3 else ''
    store_and_fwd_flag = values[4] if len(values) > 4 else ''
    dropoff_datetime = values[5] if len(values) > 5 else ''
    passenger_count = values[6] if len(values) > 6 else ''
    trip_time_in_secs = values[7] if len(values) > 7 else ''
    trip_distance = values[8] if len(values) > 8 else ''
    pickup_longitude = values[9] if len(values) > 9 else ''
    pickup_latitude = values[10] if len(values) > 10 else ''
    dropoff_longitude = values[11] if len(values) > 11 else ''
    dropoff_latitude = values[12] if len(values) > 12 else ''
    payment_type = values[13] if len(values) > 13 else ''
    fare_amount = values[14] if len(values) > 14 else ''
    surcharge = values[15] if len(values) > 15 else ''
    mta_tax = values[16] if len(values) > 16 else ''
    tip_amount = values[17] if len(values) > 17 else ''
    tolls_amount = values[18] if len(values) > 18 else ''
    total_amount = values[19] if len(values) > 19 else ''
    name = license[20] if len(license) > 20 else ''
    type = license[21] if len(license) > 21 else ''
    current_status = license[22] if len(license) > 22 else ''
    DMV_license_plate = license[23] if len(license) > 23 else ''
    vehicle_VIN_number = license[24] if len(license) > 24 else ''
    vehicle_type = license[25] if len(license) > 25 else ''
    model_year = license[26] if len(license) > 26 else ''
    medallion_type = license[27] if len(license) > 27 else ''
    agent_number = license[28] if len(license) > 28 else ''
    agent_name = license[29] if len(license) > 29 else ''
    agent_telephone_number = license[30] if len(license) > 30 else ''
    agent_website = license[31] if len(license) > 31 else ''
    agent_address = license[32] if len(license) > 32 else ''
    last_updated_date = license[33] if len(license) > 33 else ''
    last_updated_time = license[34] if len(license) > 34 else ''

    print ('%s&%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (medallion, hack_license, vendor_id, pickup_datetime, rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount, name, type, current_status, DMV_license_plate, vehicle_VIN_number, vehicle_type, model_year, medallion_type, agent_number, agent_name, agent_telephone_number, agent_website, agent_address, last_updated_date, last_updated_time))
    


revenue = fare_amount + surcharge + tip_amount + tolls_amount                

