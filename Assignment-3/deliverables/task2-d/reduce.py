#!/usr/bin/python
import sys

current_pickup_date = None
current_fare_amount = 0
current_surcharge = 0
current_tip_amount = 0
current_tolls_amount = 0

for line in sys.stdin:
    
    pickup_date, revenue = line.strip().split("&", 1)
    fare_amount, surcharge, tip_amount, tolls_amount = revenue.strip().split("\t", 3)
    
    try:
        fare_amount = float(fare_amount)
        surcharge = float(surcharge)
        tip_amount = float(tip_amount)
        tolls_amount = float(tolls_amount)
    except ValueError:
        continue
    
    if pickup_date == current_pickup_date:
        current_fare_amount += fare_amount
        current_surcharge += surcharge
        current_tip_amount += tip_amount
        current_tolls_amount += tolls_amount
    else:
        if current_pickup_date:
            print ("KEY: %s        VALUE: %.2f,%.2f,%.2f,%.2f" % (current_pickup_date, current_fare_amount, current_surcharge, current_tip_amount, current_tolls_amount))
        current_pickup_date = pickup_date
        current_fare_amount = fare_amount
        current_surcharge = surcharge
        current_tip_amount = tip_amount
        current_tolls_amount = tolls_amount

print ("KEY: %s        VALUE: %.2f,%.2f,%.2f,%.2f" % (current_pickup_date, current_fare_amount, current_surcharge, current_tip_amount, current_tolls_amount))