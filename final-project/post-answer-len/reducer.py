#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import heapq
from itertools import takewhile

####
# Helper functions to improve readability
####

### Implement a monoid to accumulate the results

zero = [0, 0, 0] 
      
def clone(obj):
    return list(obj);

def add(acc, nt, val):
    if nt =='question':
        acc[0] = float(val)
    else:
        acc[1] += 1
        acc[2] += float(val)
    return acc 

def process_results(result):
    values = sorted(result, reverse=True)
    return values 

### Keep the 10 top elements using a minheap
topN = [(0, "")] * 10

### Print the results
def print_result(key, result):
    post_len, number_of_answers, answer_len = result
    if number_of_answers > 0:
        print key, "\t", post_len, "\t", answer_len / number_of_answers
    else:
        print key, "\t", post_len, "\t", 0 


#####
# Implementation of the reducer
#####

acc = clone(zero)
oldKey = None

# Loop around the data
# For this excercise it will return a row containing the author_id and the hour of maximum posts
# returning multiple lines for each author in case there is a tie 
#
# It will use a simple process to reduce the input, this reduce can't be used as a combiner 
# because it does not preserve the information about the number of posts for each author/time combination
#

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, nt, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print_result(oldKey, acc)
        oldKey = thisKey;
        acc = clone(zero)

    oldKey = thisKey
    acc = add(acc, nt, thisValue)

print_result(oldKey, acc);

