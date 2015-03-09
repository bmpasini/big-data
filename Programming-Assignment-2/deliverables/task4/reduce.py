#!/usr/bin/python
import sys
import operator

# It takes 30 minutes to run, but it works

# Input: List from map
# Output: Unique list of words that came from map
def get_words(word_list):
    words = []
    for key in word_list:
        word = key.split("    ", 1)[0]
        words.append(word)
    uniq_words = []
    for word in words:
       if word not in uniq_words:
          uniq_words.append(word)
    return uniq_words

# Input: List from map
# Output: Unorganized { "word" => { "0000" => count, "0001" => count, ... } }
def put_same_together(word_list):
    reorganized_list = {}
    uniq_words = get_words(word_list)
    for uniq_word in uniq_words:
        doc_and_count = {}
        for key in word_list:
            word, doc = key.strip().split("    ", 1)
            count = word_list[key]
            if word == uniq_word:
                doc_and_count[doc] = count
        reorganized_list[uniq_word] = doc_and_count
    return reorganized_list

# Input: List from map
# Output: Organized { "word" => { "0000" => count, "0001" => count, ... } }
def sort_correctly(word_list):
    unorganized_list = put_same_together(word_list)
    organized_list = {}
    for word in unorganized_list:
        sorted_doc_list = sorted(unorganized_list[word].items(), key=operator.itemgetter(1))
        max_value_doc_list = 1
        for doc_count_pair in sorted_doc_list:
            if doc_count_pair[1] > max_value_doc_list:
                max_value_doc_list = doc_count_pair[1] # get max value from sorted_doc_list
        sub_sorted_doc_list = []
        for i in range(1, max_value_doc_list+1):
            j_value_items = []
            for j in sorted_doc_list:
                if j[1] == i:
                    j_value_items.append(j)
            j_value_items = sorted(j_value_items, key=operator.itemgetter(0))
            for item in j_value_items:
                sub_sorted_doc_list.append(item)
        organized_list[word] = sub_sorted_doc_list
    return organized_list

# Input: List from map
# Output: word    0063 35, 0000 50, 0010 50 (Organized and ready to print to stdout)
def printable_list(word_list):
    organized_list = sort_correctly(word_list)
    printable_list = []
    for key in organized_list:
        kv_pair_str = ""
        kv_pair_str += key
        kv_pair_str += "\t"
        for doc_count_pair in organized_list[key]:
            kv_pair_str += doc_count_pair[0]
            kv_pair_str += " "
            kv_pair_str += str(doc_count_pair[1])
            kv_pair_str += ", "
        kv_pair_str = kv_pair_str[:-2]
        printable_list.append(kv_pair_str)
    return printable_list

word_list = {}

for line in sys.stdin:
    
    word_and_file, count = line.strip().split("\t", 1)
    word_and_file = word_and_file.replace("&","    ")

    try:
        count = int(count)
    except ValueError:
        continue
    
    if word_and_file not in word_list:
        word_list[word_and_file] = count
    else:
        word_list[word_and_file] += count

word_list = printable_list(word_list)

for line in word_list:
    print ("%s" % (line))

