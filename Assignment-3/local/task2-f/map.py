#!/usr/bin/python
# key is the medallion, and the value is the number of trips.
import sys

for line in sys.stdin:

    key, value = line.strip().split('        ')
    keys = key.replace('KEY: ', '').split(',')

    medallion = keys[0]
    license = keys[1]

    print ("%s&%s" % (license, medallion))