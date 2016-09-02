from __future__ import division

import text_cleaner as tc
import math
import re
import pprint
import json

import operator 


class ididfEngine():
    
    
    def __init__(self):    
        self.words = {}
        self.docs = {}
        self.top = {}
        self.gtotal = 0 
    
    def getWordsFromTweets(self, listoftweets):
        for segment in listoftweets:
            
                #pprint.pprint(segment)
                #input("wait")
                #t = json.loads(segment)
                a = segment["id"]
                
                if(a not in self.docs.keys()): 
                    self.docs[a] = {}                                
                
                longString = segment["text"]

                #longString = longString.replace("\n", " ")            
                #longString = longString.replace("\r", " ")   
                #longString = longString.replace("\n\r", " ")   
                #longString = longString.replace("\r\n", " ")   
                #longString = longString.replace("'", "")
                longString = longString.replace(":", "")
                #longString = longString.replace("!", "")
                longString = longString.replace("?", "")
                #longString = longString.replace(".", "")
                #longString = longString.replace(",", "")
                #longString = longString.replace(";", "")
                #longString = longString.replace("-", " ")
                #longString = longString.replace('"', " ")
                #longString = longString.replace('(', "")
                #longString = longString.replace(')', "")
                #longString = longString.replace('_', "")
                #longString = longString.replace('[', "")
                #longString = longString.replace(']', "")
                #longString = longString.replace('*', "")
                longString = longString.replace('&', "")                        
                longString = tc.cleanTweet(longString)
                longString = longString.lower()         
                longString = longString.split(" ")
                
                self.gtotal = 0
                for b in longString:
                    #total_words.append(b)
                    if b.strip() != "":
                        self.gtotal = self.gtotal + 1
                        if re.sub("[\d]+", "", b) == "": continue    
                        if b not in self.words.keys():
                            self.words[b] = {}
                            self.words[b]["docs"] = []
                        if a not in self.words[b]["docs"]: 
                            self.words[b]["docs"].append(a)                        
                        if b not in self.docs[a].keys():
                            self.docs[a][b] = {}
                            self.docs[a][b]["ct"]=1
                        elif b in self.docs[a].keys():
                            self.docs[a][b]["ct"] = self.docs[a][b]["ct"]+1
                self.docs[a]['global_total'] = self.gtotal
                for keys in self.docs[a].keys():
                    if keys != "global_total":
                        
                        num = int(self.docs[a][keys]["ct"])
                        demon = int(self.docs[a]['global_total'])
                        x = num/demon
                        #print("Doc: " + str(docs[a][keys]) + " -- " + str(x))
                        #print("Total: " + str(docs[a]['total']))
                        self.docs[a][keys]["freq"] = round(x,20)
                
                #for w in words.keys(): w['docs'] = set(w['docs'])
     

     
    
    def getIDF(self, corpusCount):
        for w in self.words.keys():
            #print("corpus: " + str(corpusCount))
            #pprint.pprint(words[w])
            f = float(corpusCount/len(self.words[w]["docs"]))
            #print("F: " + str(f))
            #print("word: "+ w) 
            self.words[w]["idf"] = math.log(f,math.e)
            #print("IDF: " + str(words[w]["idf"]))
                  
        
    def calcTFIDF(self):
        top = {}    
        for d in self.docs.keys():
            for w in self.words.keys():
                if w in self.docs[d].keys():            
                    try:
                        #print("doc: " + d)
                        #print("word: " + w)            
                        idf = float(self.words[w.encode('utf-8')]["idf"]) 
                        freq = float(self.docs[d.encode('utf-8')][w.encode('utf-8')]['freq'])
                        #print("freq: " + str(freq))
                        tfidf = idf*freq
                        #print("tfidf: " + str(tfidf))
                        self.docs[d][w]["TFIDF"] = float(tfidf)
                        if top == {}:
                            top[w] = tfidf
                        else:
                            if tfidf > top[top.keys()[0]]: 
                                top[w] = tfidf
                    except:
                        print("d: " + d.encode('utf-8') + " :: w: " + w.encode('utf-8'))
        return top
    
    def processTweetIDIDF(self, listofTweets):
        #print(listofTweets)
        #input("wait")
        self.getWordsFromTweets(listofTweets)
        self.getIDF(len(listofTweets))
        t = self.calcTFIDF()
    
        word = max(t.iteritems(), key=operator.itemgetter(1))[0]
        tdidf = t[word]
    
        print("word: " + word.encode('utf-8') + ' Score: ' + str(tdidf))