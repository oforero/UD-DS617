#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from itertools import takewhile

####
# Helper functions to improve readability
####

### Implement a monoid to accumulate the results

zero = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0,
        "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0 }

def clone(obj):
    return obj.copy();

def add(acc, val):
    acc[val] += 1

def results(acc):
    values = sorted(acc.items(), key=lambda tup: tup[1], reverse=True)
    maxVal = values[0][1]
    return takewhile(lambda tup: tup[1]==maxVal, values)

### Print the results
def print_result(key, values):
    if key != None:
        for x,y in results(values):
            print key, "\t", x


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

