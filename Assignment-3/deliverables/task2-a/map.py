#!/usr/bin/python
import sys

for line in sys.stdin:

    key, value = line.strip().split('        ')
    value = value.replace('VALUE: ', '')
    fare_amount = value.split(',')[11]

    print ("%s&%d" % (fare_amount, 1))