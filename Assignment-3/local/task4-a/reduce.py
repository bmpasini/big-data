#!/usr/bin/python
import sys

current_vehicle_type = None
current_revenue = 0
current_tip_amount = 0
current_count = 0

for line in sys.stdin:
    
    vehicle_type, values = line.strip().split("&", 1)
    revenue, tip_amount, count = values.strip().split(",", 2)
    
    try:
        revenue = float(revenue)
        tip_amount = float(tip_amount)
        count = int(count)
    except ValueError:
        continue
    
    if vehicle_type == current_vehicle_type:
        current_revenue += revenue
        current_tip_amount += tip_amount
        current_count += count
    else:
        if current_vehicle_type:
            print ("KEY: %s        VALUE: %d,%.2f,%.2f%%" % (current_vehicle_type, current_count, current_revenue, (100*current_tip_amount/current_revenue)))
        current_vehicle_type = vehicle_type
        current_revenue = revenue
        current_tip_amount = tip_amount
        current_count = count

print ("KEY: %s        VALUE: %d,%.2f,%.2f%%" % (current_vehicle_type, current_count, current_revenue, (100*current_tip_amount/current_revenue)))