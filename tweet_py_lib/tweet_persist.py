import sys
import json

return_tweets = []
languages = {}

#folder = sys.argv[1]
#save_file = sys.arv[2]
#file_type = sys.arv[3]

#save_file = folder + "/" + save_file + "." + file_type
def output_raw_tweets(location, tweets, tdata):
    print("Persisting " + str(tdata))
    errors = 0
 
    # "tweet_data/raw_output_file.txt" 
    output_file = open(location, "w")    
    for t in tweets:
        json.dump(t, output_file)
        output_file.write("\n")
        
    output_file.close()
