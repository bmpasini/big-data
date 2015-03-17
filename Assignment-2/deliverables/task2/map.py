#!/usr/bin/python
import sys
import string

stop_words = ["a", "able", "about", "across", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be", "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does", "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so", "some", "than", "that", "the", "their", "them", "then", "there", "these", "they", "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

def clean_word(word):
    for c in string.punctuation:
        word = word.replace(c,"")
    for c in numbers:
        word = word.replace(c,"")
    return word

def dont_stop(word):
    if word in stop_words or word == "":
        return False
    else:
        return True

for line in sys.stdin:
    
    l = line.strip().split()

    for word in l:

        # word = word.lower()
        word = clean_word(word)
        
        if dont_stop(word):

            initial = word[0].upper()
            
            print ("%s\t%d" % (initial, 1))
