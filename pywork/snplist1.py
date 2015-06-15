import re
import sys
import codecs

filein=sys.argv[1]
fileout=sys.argv[2]
f=codecs.open(filein,encoding="utf-8")
w=codecs.open(fileout,encoding="utf-8",mode='w')
#read whole input file(snp04.txt) in a string
x=f.read()
# find all c-tags (plus contents) in this string
#including c-tags wich extend in more than one line
l=re.findall(r'<c>.*?</c>',x,flags=re.DOTALL)
for i in xrange(0,len(l)):
    #replace end of line characters (r'\r\n') with a space
    l[i]=re.sub(r'\r\n',' ',l[i])
    #replace end of line characters (r'\n') with a space,
    l[i]=re.sub(r'\n',' ',l[i])
    #remove "<>"
    l[i]=re.sub(r'<>','',l[i])
    #write c-tag in output file
    w.write("%s\n" %l[i])
       
        
    
    
        
