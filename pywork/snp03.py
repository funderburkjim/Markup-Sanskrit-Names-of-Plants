import re
import unicodedata
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
        l=re.sub(r' +</c>','</c>',l)
        #move a following period into segment
        l=re.sub(r'</c>\.','.</c>',l)
        #merge almost consecutive capitalized segments
        l=re.sub(r'</c> +<c>',' ',l)
        #change naked X. to <c>X.</>
        l=re.sub(r' [a-z]\. ',lambda pat:'<c>'+pat.group(0).upper()+'</c>',l)
    w.write(l)
    
