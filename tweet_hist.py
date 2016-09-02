#!/usr/bin/python

import sys
import numpy
import pprint
import matplotlib.pyplot as plt

langs = {}

data = open("part-00000", "r")

for line in data:
    l = line.split("\t")
    langs[l[0].strip()] = int(l[1])
    
plt.bar(range(len(langs)), langs.values(), align='center')
plt.xticks(range(len(langs)), langs.keys(), rotation=205)
