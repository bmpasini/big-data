#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:

    key, value = line.strip().split('        ')
    key = key.replace('KEY: ', '')
    value = value.replace('VALUE: ', '')

    pickup_datetime = key.split(',')[3]
    values = value.split(',')

    if len(values) == 17:
	    fare_amount = values[11]
	    surcharge = values[12]
	    tip_amount = values[14]
	    tolls_amount = values[15]

    pickup_date = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

    print ("%s&%s\t%s\t%s\t%s" % (pickup_date, fare_amount, surcharge, tip_amount, tolls_amount))