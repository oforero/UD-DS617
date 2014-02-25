#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from itertools import takewhile

####
# Helper functions to improve readability
####

### Implement a monoid to accumulate the results

zero = []

def clone(obj):
    return list(obj);

def add(acc, val):
    acc.append(val)

def results(acc):
    return acc

### Print the results
def print_result(key, values):
    if key != None:
        print key, "\t", values 


#####
# Implementation of the reducer
#####

acc = clone(zero)
oldKey = None

# Loop around the data
# For this excercise it will return a row containing the author_id and the hour of maximum posts
# returning multiple lines for each author in case there is a tie 
#
# This reducer will accumulate the author occurrances in a list for each thread id and print the thread id and list  
# when finishing a thread id 
#

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
	print_result(oldKey, acc);
        oldKey = thisKey;
        acc = clone(zero)

    oldKey = thisKey
    add(acc, thisValue)

print_result(oldKey, acc);

