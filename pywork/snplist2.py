import re
import sys
import codecs
from collections import Counter
filein=sys.argv[1]
fileout=sys.argv[2]
f=codecs.open(filein,encoding="utf-8")
w=codecs.open(fileout,encoding="utf-8",mode='w')
#read whole input file(snp04_list1.txt) in a string
x=f.read()

#make list of all c-tags
l=re.findall(r'<c>.*?</c>',x)
# initialize empty counter
c=Counter()
for i in l:
    #add i to counter 
    c.update([i])
#sort the counter according to occurrence of c-tags
d=c.most_common()
for i in d:
    #write the number of occurrence and c-tag
    w.write("%d %s\n" %(i[1],i[0]))

    
