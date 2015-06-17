import re
import sys
import codecs

filein=sys.argv[1]
filein1=sys.argv[2]
fileout=sys.argv[3]


f=codecs.open(filein,encoding="utf-8")
f1=codecs.open(filein1,encoding="utf-8")
w=codecs.open(fileout,encoding="utf-8",mode='w')

nobot = {}

for l in f1:
    #Read snp04_one_noperiod_nobot into a dict (nobot)
    #The keys of nobot are the lines of the file, after stripping the line-ending character(s)) 
    l = l.rstrip('\r\n')
    nobot[l] = True

for l in f:
    #find c-tags from snp04.txt
    caps=re.findall(r'<c>.*?</c>',l)
    for x in caps:
        #if x in caps
        if x in nobot:
            #if x is in dict(nobot) remove c-tags
            l=re.sub(r'<c>(.*?)</c>',r'\1',l)
    w.write(l)
            
