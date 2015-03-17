#!/usr/bin/python

import sys

current_word = None
current_sum = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    word, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if word == current_word:
        current_sum += count
    else:
        if current_word:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d" %( current_word, current_sum )
        current_word = word
        current_sum = count