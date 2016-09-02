import sys
import json

end_line = ""
domain = ""
total = 0
langs={}
first = 1


with open("tweet_lang_data") as langus:
    for f in langus:
        if first == 1:
            first = 0
            continue        
        l = f.strip().split('\t')
        total = total+ int(l[1])+1

first = 1        
with open("tweet_lang_data") as langus:
    for f in langus:
        if first == 1:
            first = 0
            continue
        
        if f == "'": continue
        if f == "": continue
        line = f.strip()
        line = line.replace("'","")
        line = line.replace("\n","")
        line = line.replace("\r","")
        line = line.split("\t")
        p = "'" + line[0].strip() + "'"
        p = p.replace('"', "")
        langs[p.replace("'","")] = int(line[1])+1
        end_line = end_line + ((p+", ")*(int(line[1])+1))
        domain= domain + p+", " 
        

print("[" +end_line[:-2]+"]")   
print("domain")
print("[" + domain[:-2] + "]")     


for k in langs:
    i = float(langs[k])
    i = i / total
    langs[k]= str(("%.6f" % i))
    
with open("data_freq.tsv", "w") as tsv:
    for k in langs:
        tsv.write(k + "\t" + str(langs[k]) + "\n\r")
        
