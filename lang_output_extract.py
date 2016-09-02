with open("part-00000", "r") as f:
    langs = {}    
    lang_var = []
    total = 0
    for line in f:
        l = line.split('\t')
        langs[l[0]] = l[1]

for l in langs.keys():
    lang_var.append(l * int(langs[l]))
    total = total + int(langs[l])

print lang_var
print str(total)