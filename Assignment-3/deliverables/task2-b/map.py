#!/usr/bin/python
import sys

for line in sys.stdin:

    key, value = line.strip().split('        ')
    value = value.replace('VALUE: ', '')

    try:
        fare_amount = float(value.split(',')[11])
    except ValueError:
        continue

    if fare_amount <= 10:
    	print (1);