# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 15:56:42 2015

@author: alexander
"""

import sys
import json
import pprint

with open("raw_output_file.txt", "r") as tweets:
    for f in tweets.readlines():
        l = json.loads(f)
        if "user" in l:
            print l["user"]
            print "{0}\t{1}".format(l["user"]["screen_name"], str(1))
        
        input("Waiting")