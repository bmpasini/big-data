#!/usr/bin/python
import sys

current_num_of_passengers = None
current_sum = 0

for line in sys.stdin:
    
    num_of_passengers, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if num_of_passengers == current_num_of_passengers:
        current_sum += count
    else:
        if current_num_of_passengers:
            print ("KEY: %s        VALUE: %d" % (current_num_of_passengers, current_sum))
        current_num_of_passengers = num_of_passengers
        current_sum = count

print ("KEY: %s        VALUE: %d" % (current_num_of_passengers, current_sum))