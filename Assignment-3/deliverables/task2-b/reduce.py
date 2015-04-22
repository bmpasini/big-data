#!/usr/bin/python
import sys

cnt = 0

for line in sys.stdin:
    
    try:
        line = int(line)
    except ValueError:
        continue
    
    cnt += line

print ("%d" % (cnt))