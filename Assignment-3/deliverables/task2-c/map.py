#!/usr/bin/python
import sys

for line in sys.stdin:

    key, value = line.strip().split('        ')
    value = value.replace('VALUE: ', '')
    passenger_count = value.split(',')[3]

    print ("%s\t%d" % (passenger_count, 1))

