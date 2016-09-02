### Given a block of raw text from a twitter scrape this will
### return a list of string from the text field of the tweet
### json object as well as an integer representing the number
### of non-specific errors encountered when trying to load and 
### clean each of the tweet text objects.




import sys
import pprint
import json
import text_cleaner as textclean
import numpy

return_tweets = []
languages = {}

def extract_tweets(text):
    ''' returns a list of strings from raw tweet block and an integer representing errors encountered while parsing'''
    ''' usage: tweets, errors = tweet_extractor.extract_tweets(raw_text) '''
    print("Extracting Tweets")

    errors = 0
    raw_tweets = text
   
    tweets = []
    for t in raw_tweets.readlines():
        t = textclean.killgremlins(t)
        
        try:      
            tw = json.loads(t)
            if "text" in tw:
                tweets.append(tw["text"])
        except:
            errors = errors + 1
            continue
                      
    print("Number of Tweet Errors: " + str(errors))      
    return tweets, errors

