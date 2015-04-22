#!/usr/bin/python
import sys
import csv
import StringIO
 
for line in sys.stdin:
    if '        ' in line:
        key, value = line.strip().split('        ')
        key = key.replace('KEY: ', '')
        value = value.replace('VALUE: ', '')

        keys = key.split(',')
        values = value.split(',')

        medallion, hack_license, vendor_id, pickup_datetime = keys
        rate_code = values[0] if len(values) > 0 else ''
        store_and_fwd_flag = values[1] if len(values) > 1 else ''
        dropoff_datetime = values[2] if len(values) > 2 else ''
        passenger_count = values[3] if len(values) > 3 else ''
        trip_time_in_secs = values[4] if len(values) > 4 else ''
        trip_distance = values[5] if len(values) > 5 else ''
        pickup_longitude = values[6] if len(values) > 6 else ''
        pickup_latitude = values[7] if len(values) > 7 else ''
        dropoff_longitude = values[8] if len(values) > 8 else ''
        dropoff_latitude = values[9] if len(values) > 9 else ''
        payment_type = values[10] if len(values) > 10 else ''
        fare_amount = values[11] if len(values) > 11 else ''
        surcharge = values[12] if len(values) > 12 else ''
        mta_tax = values[13] if len(values) > 13 else ''
        tip_amount = values[14] if len(values) > 14 else ''
        tolls_amount = values[15] if len(values) > 15 else ''
        total_amount = values[16] if len(values) > 16 else ''

        print ('%s,trip_fare&%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (medallion, hack_license, vendor_id, pickup_datetime, rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount))

    else: # licenses
        csv_file = StringIO.StringIO(line)
        csv_reader = csv.reader(csv_file)
        for values in csv_reader:
            license = []
            for v in values:
                if ',' in v:
                    license.append('"' + v + '"')
                else:
                    license.append(v)
            medallion = license[0] if len(license) > 0 else ''
            name = license[1] if len(license) > 0 else ''
            type = license[2] if len(license) > 1 else ''
            current_status = license[3] if len(license) > 2 else ''
            DMV_license_plate = license[4] if len(license) > 3 else ''
            vehicle_VIN_number = license[5] if len(license) > 4 else ''
            vehicle_type = license[6] if len(license) > 5 else ''
            model_year = license[7] if len(license) > 6 else ''
            medallion_type = license[8] if len(license) > 7 else ''
            agent_number = license[9] if len(license) > 8 else ''
            agent_name = license[10] if len(license) > 9 else ''
            agent_telephone_number = license[11] if len(license) > 10 else ''
            agent_website = license[12] if len(license) > 11 else ''
            agent_address = license[13] if len(license) > 12 else ''
            last_updated_date = license[14] if len(license) > 13 else ''
            last_updated_time = license[15] if len(license) > 14 else ''

            if medallion != "medallion":
                print ('%s,license&%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (medallion, name, type, current_status, DMV_license_plate, vehicle_VIN_number, vehicle_type, model_year, medallion_type, agent_number, agent_name, agent_telephone_number, agent_website, agent_address, last_updated_date, last_updated_time))

