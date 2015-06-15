import re
import sys
import codecs

filein=sys.argv[1]
fileout=sys.argv[2]
f=codecs.open(filein,encoding="utf-8")
w=codecs.open(fileout,encoding="utf-8",mode='w')
#read whole input file(snp03.txt) as array of string ,each string ending with (\r\n) new line
lines = [l.rstrip('\r\n') for l in f]
lineno = 0
for i in xrange(0,len(lines)):
    lineno+=1
    if (lineno>=81 and lineno<3313):
        #first line l1 and second line l2 
        l1=lines[i]
        l2=lines[i+1]
        #find if the l1 line end with "</c>" or "</c>-"
        m = re.search(r'</c>-* *$',l1)
        #find if the l2 line start with "<>" 0 or more space and "<c>"
        n = re.search(r'^<> *<c>',l2)
        #if both condition
        # then  (a) remove that last </c> in l1 and that first <c> in l2 and
        # (b) set lines[i] to the modified l1, and similarly for lines[i+1]
        if (m and n):
            l1=re.sub(r'</c>(-* *)$',r'\1',l1)
            l2=re.sub(r'^(<> *)<c>',r'\1',l2)
            lines[i]=l1
            lines[i+1]=l2
for l in lines:
    # write l with a newline character \n
    w.write(l)
    w.write('\n')

        

