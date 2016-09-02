import sys
import json



for o in sys.stdin:
    
    print("Working on a", type(o))

#return_tweets = []
#languages = {}
#
#location = sys.argv[2]  
#ext = sys.argv[3]
#feature = sys.argv[4]
#
#def main():
#    print("Running Py Lib Tweets")
#    errors = 0
#   
#    raw_tweets = open(sys.argv[1])
#     
#    
#    rtweets = raw_tweets.readlines()    
#    raw_tweets.close()
#    
#    if(feature=="all"): 
#      tweets, text, questions, turls, tweets, languages, geos, errors = textract.extract_all(rtweets)
#      tpersist.output_raw_tweets(location+"_tweets."+ext, tweets, "full tweets")
#      tpersist.output_raw_tweets(location+"_questions."+ext, questions, "questions")
#      tpersist.output_raw_tweets(location+"_text."+ext, text, "tweet text")
#      tpersist.output_raw_tweets(location+"_URLs."+ext, turls, "urls")      
#      tpersist.output_raw_tweets(location+"_languages."+ext, languages, "tweet language")
#      tpersist.output_raw_tweets(location+"_geo."+ext, geos, "tweet geo")
#    elif(feature=="tweet"):  
#      tweets, errors  = textract.extract_tweets(rtweets)
#      tpersist.output_raw_tweets(location+"_tweets."+ext, tweets, "full tweets")
#      print("Number of Errors: " + str(errors))
#    elif(feature=="url"):    
#      tweets,errors = textract.extract_tweet_URLs(rtweets)
#      tpersist.output_raw_tweets(location+"_urls."+ext, tweets, "urls")
#      print("Number of Errors: " + str(errors))
#    elif(feature=="text"):
#      tweets, errors = textract.extract_tweet_text(rtweets)
#      tpersist.output_raw_tweets(location+"_text."+ext, tweets, "tweet text")
#      print("Number of Errors: " + str(errors))
#    elif(feature=="lang"):
#      tweets, errors = textract.extract_tweet_languages(rtweets)
#      tpersist.output_raw_tweets(location+"_languages."+ext, tweets, "tweet language")
#      print("Number of Errors: " + str(errors))
#    elif(feature=="geo"):
#      tweets, errors = textract.extract_tweet_geos(rtweets)
#      tpersist.output_raw_tweets(location+"_geo."+ext, tweets, "tweet geo")
#      print("Number of Errors: " + str(errors))
#     
#if __name__ == '__main__':
#    main()