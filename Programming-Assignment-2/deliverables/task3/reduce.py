#!/usr/bin/python
import sys
import os

word_list = {}

def inv_word_list(word_list):
    inv_word_list = []
    for key, value in word_list.items():
        inv_word_list.append((value, key))
    return sorted(inv_word_list, reverse = True)

for line in sys.stdin:
    
    word, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if word not in word_list:
        word_list[word] = count
    else:
        word_list[word] += count

inv_word_list = inv_word_list(word_list)

for word in inv_word_list[:100]:
    print ("%s\t%d" % (word[1], word[0]))