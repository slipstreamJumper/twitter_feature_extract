#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import json

for line in sys.stdin:   
    try:    
        l = json.loads(line.strip().replace("\n", ""))
        if "lang" in l:
            print "{0}\t{1}".format(l["lang"], str(1))
    except Exception, e:
        print (str(e))
        print("ERROR")
        continue
        

