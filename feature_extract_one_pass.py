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

def extract_features(text):
    ''' returns a list of strings from raw tweet block and an integer representing errors encountered while parsing'''
    ''' usage: tweets, errors = tweet_extractor.extract_tweets(raw_text) '''
    print("Extracting Tweets")
    languages = {}
    errors = 0
    raw_tweets = text
    text = []
    tweets = []
    turls = []
    for t in raw_tweets:
        t = textclean.killgremlins(t)
        
        try:      
            tw = json.loads(t)
            if "text" in tw:
              tweets.append(tw)
              text.append(tw["text"])
              url = findURLs(tw["text"])
              if(url != []): 
                  for u in url:
                      turls.append(u.replace('"',""))
            if "lang" in tw:
              if tw["lang"] in languages:
                languages[tw["lang"]] += 1
              else:
                languages[tw["lang"]] = 1 
        except:
            errors = errors + 1
            continue
                      
    print("Number of Tweet Errors: " + str(errors))      
    return tweets, errors

def findURLs(string):
    urls = []
    string = string.replace("\n", " ")
    string = string.replace(u"\u201d", " ")  
    string = string.replace(u"\u201di", " ")  
    string = string.replace("\\", " ")
    string = string.replace('"'," ")
    string = string.split(" ")
    for s in string:
        if "http" in s: urls.append(s)
    return urls        
    
def findQuestions(string):
    if "?" in string or "¿" in string:
      return string
    else:
      return ""