#!/usr/bin/python
import sys
import csv
import StringIO
 
for line in sys.stdin:
    key, value = line.strip().split('        ')
    values = value.replace('VALUE: ', '')

    csv_file = StringIO.StringIO(values)
    csv_reader = csv.reader(csv_file)
    for values in csv_reader:
        
        agent_name = values[29] if len(values) > 29 else ''

        try:
            fare_amount = float(values[14]) if len(values) > 14 else ''
            surcharge = float(values[15]) if len(values) > 15 else ''
            tip_amount = float(values[17]) if len(values) > 17 else ''
            tolls_amount = float(values[18]) if len(values) > 18 else ''
        except ValueError:
            continue

        revenue = fare_amount + surcharge + tip_amount + tolls_amount

        print ('%s&%f' % (agent_name, revenue))
    



