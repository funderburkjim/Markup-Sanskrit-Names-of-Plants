import re
import unicodedata
import sys
import codecs

filein=sys.argv[1]
fileout=sys.argv[2]
f=codecs.open(filein,encoding="utf-8")
w=codecs.open(fileout,encoding="utf-8",mode='w')

x=f.read()

l=re.findall(r'<c>.*?</c>',x,flags=re.DOTALL)
for i in xrange(0,len(l)):
    l[i]=re.sub(r'\r\n',' ',l[i])
    l[i]=re.sub(r'<>','',l[i])
    if l[i].endswith("</c>"):
        w.write(l[i])
        w.write("\n")
    else :
        l[i+1]=l[i].rstrip('\n')+l[i+1]
       
        
    
    
        
