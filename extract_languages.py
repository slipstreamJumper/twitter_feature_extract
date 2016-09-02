import sys
import pprint
import json
import text_cleaner as textclean
import numpy

languages = {}

def extract_languages_from_tweets(tweets):
    print("Extracting Languages")

    errors = 0
    
    for t in tweets:
        try:
            tw = json.loads(t)
            if "lang" in tw:
              if tw["lang"] in languages:
                languages[tw["lang"]] += 1
              else:
                languages[tw["lang"]] = 1 
        except:
            errors = errors + 1
            continue
             
              
    print("Number of Language Errors: " + str(errors))
    return languages, errors

