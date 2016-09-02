from __future__ import division

import os
from os import listdir
import text_cleaner as tc
import math
import re
import pprint 
import operator 


words = {}
docs = {}
top = {}

def getFiles():
    currentDir = str(os.getcwd()) + "/bible/"
    files = []    
    for f in listdir(currentDir):
        files.append(currentDir+str(f))
        docs[f] = {}
    return(files)
    

def getWords(files):
    for f in files:

        with open(f, "r") as oFile:
            longString = ""
            for segment in oFile.readlines():
                segment = segment.replace("\n", " ")            
                segment = segment.replace("\r", " ")   
                segment = segment.replace("\n\r", " ")   
                segment = segment.replace("\r\n", " ")   
                segment = segment.replace("'", "")
                segment = segment.replace(":", "")
                segment = segment.replace("!", "")
                segment = segment.replace("?", "")
                segment = segment.replace(".", "")
                segment = segment.replace(",", "")
                segment = segment.replace(";", "")
                segment = segment.replace("-", " ")
                segment = segment.replace('"', " ")
                segment = segment.replace('(', "")
                segment = segment.replace(')', "")
                segment = segment.replace('_', "")
                segment = segment.replace('[', "")
                segment = segment.replace(']', "")
                segment = segment.replace('*', "")
                segment = segment.replace('&', "")            
                longString = longString + segment
                
            longString = tc.killgremlins(longString)
            longString = longString.lower()         
            longString = longString.split(" ")
            a =f.replace(os.getcwd() + '/bible/', "")
            total = 0
            for b in longString:
                if b.strip() != "":
                    total += 1
                    if re.sub("[\d]+", "", b) == "": continue    
                    if b not in words.keys():
                        words[b] = {}
                        words[b]["docs"] = []
                    if a not in words[b]["docs"]: 
                        words[b]["docs"].append(a)                        
                    if b not in docs[a].keys():
                        docs[a][b] = {}
                        docs[a][b]["ct"]=1
                    elif b in docs[a].keys():
                        docs[a][b]["ct"] = docs[a][b]["ct"]+1
            docs[a]['total'] = total
            for keys in docs[a].keys():
                if keys != "total":
                    
                    num = int(docs[a][keys]["ct"])
                    demon = int(docs[a]['total'])
                    x = num/demon
                    #print("Doc: " + str(docs[a][keys]) + " -- " + str(x))
                    #print("Total: " + str(docs[a]['total']))
                    docs[a][keys]["freq"] = round(x,20)
            
            #for w in words.keys(): w['docs'] = set(w['docs'])
 

def getIDF(corpusCount):
    for w in words.keys():
        #print("corpus: " + str(corpusCount))
        #pprint.pprint(words[w])
        f = float(corpusCount/len(words[w]["docs"]))
        #print("F: " + str(f))
        #print("word: "+ w) 
        words[w]["idf"] = math.log(f,math.e)
        #print("IDF: " + str(words[w]["idf"]))
              
    
def calcTFIDF():
    top = {}    
    for d in docs.keys():
        for w in words.keys():
            if w in docs[d].keys():            
                try:
                    #print("doc: " + d)
                    #print("word: " + w)            
                    idf = float(words[w.encode('utf-8')]["idf"]) 
                    freq = float(docs[d.encode('utf-8')][w.encode('utf-8')]['freq'])
                    #print("freq: " + str(freq))
                    tfidf = idf*freq
                    #print("tfidf: " + str(tfidf))
                    docs[d][w]["TFIDF"] = float(tfidf)
                    if top == {}:
                        top[w] = tfidf
                    else:
                        if tfidf > top[top.keys()[0]]: 
                            top[w] = tfidf
                except:
                    print("d: " + d.encode('utf-8') + " :: w: " + w.encode('utf-8'))
    return top

    
files = getFiles()
getWords(files)
getIDF(len(files))
t = calcTFIDF()

word = max(t.iteritems(), key=operator.itemgetter(1))[0]
tdidf = t[word]

print("word: " + word.encode('utf-8') + ' Score: ' + str(tdidf))


