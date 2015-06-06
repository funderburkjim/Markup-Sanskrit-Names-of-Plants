import re
import unicodedata
import sys
import codecs

filein=sys.argv[1]
fileout=sys.argv[2]
f=codecs.open(filein,encoding="utf-8")
w=codecs.open(fileout,encoding="utf-8",mode='w')

lines = [l.rstrip('\r\n') for l in f]
lineno = 0
for i in xrange(0,len(lines)):
    lineno+=1
    if (lineno>=81 and lineno<3313):
        l1=lines[i]
        l2=lines[i+1]
        m = re.search(r'</c>-* *$',l1)
        n = re.search(r'^<> *<c>',l2)
        if (m and n):
            l1=re.sub(r'</c>(-* *)$',r'\1',l1)
            l2=re.sub(r'^(<> *)<c>',r'\1',l2)
            lines[i]=l1
            lines[i+1]=l2
for l in lines:
    w.write(l)
    w.write('\n')

        

