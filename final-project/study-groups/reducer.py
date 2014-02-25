#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import heapq
from itertools import takewhile

####
# Helper functions to improve readability
####

### Implement a monoid to accumulate the results

zero = 0 
      
def clone(obj):
    return 0 #obj.copy();

def add(acc, key, val):
    return acc + float(val)

def process_results(result):
    values = sorted(result, reverse=True)
    return values 

### Keep the 10 top elements using a minheap
topN = [(0, "")] * 10

### Print the results
def print_result(result):
    for (val, key) in process_results(result):
        print key, "\t", val 


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

# This can just passthrough the output of the mapper
for line in sys.stdin:
    print line

