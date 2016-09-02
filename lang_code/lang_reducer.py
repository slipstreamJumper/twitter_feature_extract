#!/usr/bin/python

import sys

langTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:

    lang= line.strip().split("\t")
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2: continue
    thisKey, thisLang = data_mapped

    thisKey = thisKey.strip()
    thisLang = thisLang.strip()
    
    #if oldKey and oldKey != thisKey:
    if oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, langTotal)

        langTotal = 1
    else: 
        langTotal += 1
        
    oldKey = thisKey
    
if oldKey != None:
    print oldKey, "\t", langTotal
