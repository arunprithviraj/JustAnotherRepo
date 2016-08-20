adict = {"1":"Arun","2":"Seethu","3":"Advaith","4":"DesertStorm"}
#print adict.values()
#print adict.keys()

#print adict

for i in adict.keys():
    print i
    print adict[i]

for i in adict.values():
    print i

print(adict.items())

for k,v in adict.items():
    print k, v

l,m = adict.keys(), adict.values()
print l
print m
