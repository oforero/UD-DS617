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
# The goal is to output a list of thread_id - post lenght - AVG(answer lenght) 
#
# This can be achieved by doing conditional projection between the fields id and abs_parent_id in the mapper
# and the lenght of the body
#
# I decided to use a simple mapper that for each post returns: 
#    (node_type == question ? id : abs_parent_id) '\t' node_type '\t' len(body)  

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
   nt, b = val
   return (nt, len(b))

def print_output(key, val):
    print "{0}\t{1}\t{2}".format(key, *val)

####
# Main Body of the mapper
####

reader=csv.reader(sys.stdin, delimiter='\t')

# Set some constants to avoid magic numbers
id = 0
author_id = 3
body = 4
node_type = 5
abs_parent_id = 7

for line in reader:
    if len(line) == 19:
       key = post_process_key([line[id], line[node_type], line[abs_parent_id]])
       if is_not_header(key): # Skip the header line in case it exists
           val = post_process_value([line[node_type], line[body]])
	   print_output(key, val)
