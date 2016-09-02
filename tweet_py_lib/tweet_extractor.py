### Given a block of raw text from a twitter scrape this will
### return a list of string from the text field of the tweet
### json object as well as an integer representing the number
### of non-specific errors encountered when trying to load and 
### clean each of the tweet text objects.

import text_cleaner as textclean
import pprint
import json 

return_tweets = []
languages = {}

languages = {}
errors = 0
text = []
tweets = []
turls = []
geos = []
questions = []


def extract_all(text):
    ''' returns a list of strings from raw tweet block and an integer representing errors encountered while parsing'''
    ''' usage: tweets, errors = tweet_extractor.extract_tweets(raw_text) '''
    print("Extracting Tweets")
    
    errors = 0
    raw_tweets = text
    if isinstance(raw_tweets, list):
      input('list check wait wait')
      for i in raw_tweets:

        try:      
            extract_data(i)
        except Exception,e: 
            print str(e)
            input('first order error')
            errors = errors + 1
            continue
    else:
      for t in raw_tweets:
         
          t = textclean.killgremlins(t)
          #for dubugging
          #print(t)
          #input("wait")
          try:      
              tw = json.loads(t)
              
              #for dubugging
              #pprint.pprint(tw)
              #input("wait")
              extract_data(tw)
                    
          except:
              errors = errors + 1
              continue
                        
    print("Number of Tweet Errors: " + str(errors))      

    return tweets, text, questions, turls, tweets, languages, geos, errors


def extract_data(tw):
  pprint.pprint(tw)
  if "text" in tw:
    tweets.append(tw)
    
    text.append(tw["text"])
    url = findURLs(tw["text"])
    question = findQuestions(tw["text"])
    
    if(question != ""): questions.append(question)
    if(url != []): 
        for u in url:
            turls.append(u.replace('"',""))
  if "lang" in tw:
    if tw["lang"] in languages:
      languages[tw["lang"]] += 1
    else:
      languages[tw["lang"]] = 1 
      
  if "geo" in tw:
    if tw["geo"] != None: 
        geos.append(str(tw["geo"]["coordinates"][0]) + "," + str(tw["geo"]["coordinates"][1]))
            




def extract_tweets(text):
    ''' returns a list of strings from raw tweet block and an integer representing errors encountered while parsing'''
    ''' usage: tweets, errors = tweet_extractor.extract_tweets(raw_text) '''
    print("Extracting Tweets")

    errors = 0
    raw_tweets = text
   
    tweets = []
    for t in raw_tweets:
        twe = ""        
        
        try: twe = json.loads(t)
        except: twe = t
        input("wait inside")
        #t = textclean.killgremlins(t)
        try:      
            twe = json.loads(t)
            if "text" in twe.keys():
                tweets.append({'id':str(twe['id']), 'text':textclean.cleanTweet(twe['text'])})
        except:
            print("error")
            errors = errors + 1
            continue
                      
    print("Number of Tweet Errors: " + str(errors))      
    return tweets, errors



def extract_tweet_languages(text):
    languages = {}
    print("Extracting Languages")

    errors = 0
    raw_tweets = text
    for t in raw_tweets:
    
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

def extract_tweet_geos(text):
    geos=[]
    print("Extracting Geos")
    errors = 0
    raw_tweets = text
    for t in raw_tweets:
        try:
            tw = json.loads(t)
            if "geo" in tw:
              
              if tw["geo"] != None: 
                  geos.append(str(tw["geo"]["coordinates"][0]) + "," + str(tw["geo"]["coordinates"][1]))

        except:
            errors = errors + 1
            continue
             
              
    print("Number of Geo Errors: " + str(errors))
    return geos, errors

def extract_tweet_text(text):
    ''' returns a list of strings from raw tweet block and an integer representing errors encountered while parsing'''
    ''' usage: tweets, errors = tweet_extractor.extract_tweets(raw_text) '''
    print("Extracting Tweet Text")

    errors = 0
    raw_tweets = text
   
    tweets = []
    for t in raw_tweets:
        t = textclean.killgremlins(t)
        
        try:      
            tw = json.loads(t)
            if "text" in tw:
                tweets.append(tw["text"])
        except:
            errors = errors + 1
            continue
                      
    print("Number of Tweet Text Errors: " + str(errors))      
    return tweets, errors
    
def extract_tweet_URLs(text):
    ''' returns a list of strings from raw tweet block and an integer representing errors encountered while parsing'''
    ''' usage: tweets, errors = tweet_extractor.extract_tweets(raw_text) '''
    print("Extracting URLs")

    errors = 0
    raw_tweets = text
   
    tweets = []
    for t in raw_tweets:
        t = textclean.killgremlins(t)
        
        try:      
            tw = json.loads(t)
            if "text" in tw:
              url = findURLs(tw["text"])
              
              if(url != []): 
                  for u in url:
                      tweets.append(u.replace('"',""))
        except:
            # print(sys.exc_info()[0])
            
            errors = errors + 1
            continue
                      
    print("Number of URL Errors: " + str(errors))      
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
    if "?" in string:
      return string
    else:
      return ""     