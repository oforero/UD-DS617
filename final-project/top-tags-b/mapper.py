#!/usr/bin/python
# -*- coding: utf-8 -*-

# The project has two files.
# One containing posts in the forums, the format of each line is:
# "id" "title" "tagnames" "author_id" "body" "node_type" "parent_id" "abs_parent_id"
# "added_at" "score" "state_string" "last_edited_id" "last_activity_by_id" 
# "last_activity_at" "active_revision_id" "extra" "extra_ref_id" "extra_count" "marked"
#
# Another containing the reputation of the authors, the format of each line is
# "user_ptr_id" "reputation" "gold" "silver" "bronze"
#
# In both cases the fields are sorrounded by quotes and separated by '\t'
#
# This goal is to find the top 10 most used tags, weighted by lenght of the title
#
# I decided to use a simple mapper that for each post returns: tag '\t' len(title)  

import sys
import csv 
from datetime import datetime

#####
# Declare some helper functions to improve readability
#####

# header detection
def is_not_header(x):
    return x != "id"

# For this excercise we simply need an id function
def post_process_key(key):
   return key

# Extract the time from the date field
def post_process_value(val):
   return val.split(" ")

def print_output(key, vals, weight):
    for v in vals:
        print "{0}\t{1}".format(v.upper(), weight)
####
# Main Body of the mapper
####

reader=csv.reader(sys.stdin, delimiter='\t')

# Set some constants to avoid magic numbers
id = 0  
tittle = 1
tagnames = 2

for line in reader:
    if len(line) == 19:
       key = post_process_key(line[id])
       if is_not_header(key): # Skip the header line in case it exists
           tags = post_process_value(line[tagnames])
	   print_output(key, tags, len(line[tittle]))
