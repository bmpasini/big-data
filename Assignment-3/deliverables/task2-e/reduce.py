#!/usr/bin/python
import sys

current_medallion = None
current_sum = 0

for line in sys.stdin:
    
    medallion, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if medallion == current_medallion:
        current_sum += count
    else:
        if current_medallion:
            print ("KEY: %s        VALUE: %d" % (current_medallion, current_sum))
        current_medallion = medallion
        current_sum = count

print ("KEY: %s        VALUE: %d" % (current_medallion, current_sum))





