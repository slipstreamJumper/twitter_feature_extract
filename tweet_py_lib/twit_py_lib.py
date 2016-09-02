import sys
import pprint
import json
import text_cleaner as textclean
import numpy
import tweet_extractor as textract
import tweet_persist as tpersist
from StringIO import StringIO
import tweet_tdidf as ttdidf

return_tweets = []
languages = {}

location = sys.argv[2]  
ext = sys.argv[3]
feature = sys.argv[4]
search = sys.argv[5]

def main():
    print("Running Py Lib Tweets")
    errors = 0
   
    raw_tweets = open(sys.argv[1])
     
    
    rtweets = raw_tweets.readlines()
    if search == 'search':
      temp = []
      rtweets = json.loads(rtweets[0])['statuses']
      for i in rtweets:
        
        
        temp.append(i)
      rtweets = temp
    raw_tweets.close()
    
    if(feature=="all"): 
      tweets, text, questions, turls, tweets, languages, geos, errors = textract.extract_all(rtweets)
      tdidf = ttdidf.ididfEngine()
      tdidf.processTweetIDIDF(tweets)
      tpersist.output_raw_tweets(location+"_tweets."+ext, tweets, "full tweets")
      tpersist.output_raw_tweets(location+"_questions."+ext, questions, "questions")
      tpersist.output_raw_tweets(location+"_text."+ext, text, "tweet text")
      tpersist.output_raw_tweets(location+"_URLs."+ext, turls, "urls")      
      tpersist.output_raw_tweets(location+"_languages."+ext, languages, "tweet language")
      tpersist.output_raw_tweets(location+"_geo."+ext, geos, "tweet geo")
    elif(feature=="tweet"):  
      print("Extracting Tweets!")
      tweets, errors  = textract.extract_tweets(rtweets)
      tpersist.output_raw_tweets(location+"_tweets."+ext, tweets, "full tweets")
      tdidf = ttdidf.ididfEngine()
      tdidf.processTweetIDIDF(tweets)
      print("Number of Errors: " + str(errors))
    elif(feature=="url"):    
      tweets,errors = textract.extract_tweet_URLs(rtweets)
      tpersist.output_raw_tweets(location+"_urls."+ext, tweets, "urls")
      print("Number of Errors: " + str(errors))
    elif(feature=="text"):
      tweets, errors = textract.extract_tweet_text(rtweets)
      tpersist.output_raw_tweets(location+"_text."+ext, tweets, "tweet text")
      print("Number of Errors: " + str(errors))
    elif(feature=="lang"):
      tweets, errors = textract.extract_tweet_languages(rtweets)
      tpersist.output_raw_tweets(location+"_languages."+ext, tweets, "tweet language")
      print("Number of Errors: " + str(errors))
    elif(feature=="geo"):
      tweets, errors = textract.extract_tweet_geos(rtweets)
      tpersist.output_raw_tweets(location+"_geo."+ext, tweets, "tweet geo")
      print("Number of Errors: " + str(errors))
     
if __name__ == '__main__':
    main()