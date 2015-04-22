#!/usr/bin/python
import sys

current_medallion = None
current_license = None
current_sum = 0

for line in sys.stdin:
    
    license, medallion = line.strip().split("&", 1)

    if license == current_license:
        if medallion != current_medallion:
            current_sum += 1
    else:
        if current_license:
            print ("KEY: %s        VALUE: %d" % (current_license, current_sum))
        current_sum = 1

    current_license = license
    current_medallion = medallion

print ("KEY: %s        VALUE: %d" % (current_license, current_sum))