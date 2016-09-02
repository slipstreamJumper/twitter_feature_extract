import urllib
import json
import urllib.request
import pprint

def get_top_ten(debug):
    r = urllib.request.urlopen('https://api.twitter.com/1/trends/1.json')
    twit_j = r.read()
    if(debug == 1): j_string = twit_j.decode('latin9')
    else: j_string = twit_j.decode('utf-8')

    twit_json = json.loads(j_string)
    pprint.pprint(twit_json)
    return j_string
