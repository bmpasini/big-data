#!/usr/bin/python
import sys
import string

f = open("stop-word-list.csv", "r")
stop_words = f.read().split(",")
f.close()

exclude = set(string.punctuation + "0123456789")

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    line = line.strip()
    line = ''.join(ch for ch in line if ch not in exclude)
    
    l = line.split()
    
    for word in l:
        
        if word.lower() not in stop_words:
        
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d" %( word, 1 )
    print "%s\t%d" %( word, 1 )