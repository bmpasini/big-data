#!/usr/bin/python
# key is the medallion, and the value is the number of trips.
import sys

for line in sys.stdin:

    key, value = line.strip().split('        ')
    key = key.replace('KEY: ', '')

    medallion = key.split(',')[0]

    print ("%s\t%d" % (medallion, 1))
