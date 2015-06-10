import re
import unicodedata
import sys
import codecs

filein=sys.argv[1]
fileout=sys.argv[2]
#fileout2=sys.argv[3]
f=codecs.open(filein,encoding="utf-8")
#j=codecs.open(fileout1,encoding="utf-8",mode='w')
w=codecs.open(fileout,encoding="utf-8",mode='w')

x=f.read()

#j=re.findall(r'<c>[A-Z]*</c>',x)
#j=list(set(l))
#for i in xrange(0,len(j)):
#   w.write(j[i])
#    w.write("\n")

l=re.findall(r'</c> *\( *<c>.*</c> *\) *<c>',x)
k=re.findall(r'</c> *\[ *<c>.*</c> *\] *<c>',x)
l=list(set(l))
k=list(set(k))
for i in xrange(0,len(l)):
    w.write(l[i])
    w.write("\n")
for i in xrange(0,len(k)):
    w.write(k[i])
    w.write("\n")
    
    
        
