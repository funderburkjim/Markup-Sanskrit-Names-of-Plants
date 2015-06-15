import re
import sys
import codecs

filein=sys.argv[1]
fileout=sys.argv[2]
f=codecs.open(filein,encoding="utf-8")
w=codecs.open(fileout,encoding="utf-8",mode='w')
lineno=0
for l in f:
    lineno+=1
    if lineno>=81 and lineno<=3313:
        #move ending space out of segment
        l=re.sub(r'( +)</c>',lambda t:'</c>'+t.group(1),l)
        #move a following period into segment
        l=re.sub(r'</c>\.','.</c>',l)
        #merge almost consecutive capitalized segments
        l=re.sub(r'</c>( +)<c>',lambda t:t.group(1),l)
    w.write(l)
    
