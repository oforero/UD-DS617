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
# This goal is to find the hour of maximum activity for each student 
#
# I decided to use a very simple mapper that for each student returns: author_id '\t' hour  

import sys
import csv 
from datetime import datetime

#####
# Declare some helper functions to improve readability
#####

# header detection
def is_not_header(x):
    return x != "author_id"

# For this excercise we simply need an id function
def post_process_key(key):
   return key

# Extract the time from the date field
def post_process_value(val):
   date_obj = datetime.strptime(val[:15], "%Y-%m-%d %H:%M")
   return date_obj.hour

####
# Main Body of the mapper
####

reader=csv.reader(sys.stdin, delimiter='\t')

# Set some constants to avoid magic numbers
author_id = 3
added_time = 8

for line in reader:
    if len(line) == 19:
       key = post_process_key(line[author_id])
       if is_not_header(key): # Skip the header line in case it exists
           val = post_process_value(line[added_time])
           print "{0}\t{1}".format(key, val)

