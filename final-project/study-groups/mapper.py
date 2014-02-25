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
# The goal is to output a list of thread_id - user_id
# Because the operation required is a conditional projection between the fields id and abs_parent_id
# this can be achieved in the mapper only, leaving the reducer to be a passthrough function
#
# I decided to use a simple mapper that for each post returns: (node_type == question ? id : abs_parent_id) '\t' author_id  

import sys
import csv 
from datetime import datetime

#####
# Declare some helper functions to improve readability
#####

# header detection
def is_not_header(x):
    return x != "abs_parent_id"

# For this excercise we simply need an id function
def post_process_key(key):
   pid, nt, apid = key
   if nt == 'question':
       return pid
   else:
       return apid

# Extract the time from the date field
def post_process_value(val):
   return val 

def print_output(key, val):
    print "{0}\t{1}".format(key, val)

####
# Main Body of the mapper
####

reader=csv.reader(sys.stdin, delimiter='\t')

# Set some constants to avoid magic numbers
id = 0
author_id = 3
node_type = 5
abs_parent_id = 7

for line in reader:
    if len(line) == 19:
       key = post_process_key([line[id], line[node_type], line[abs_parent_id]])
       if is_not_header(key): # Skip the header line in case it exists
           val = post_process_value(line[author_id])
	   print_output(key, val)
