import re
import unicodedata
import sys
import codecs

filein1=sys.argv[1]
filein2=sys.argv[2]
fileout=sys.argv[3]


f1=codecs.open(filein1,encoding="utf-8")
f2=codecs.open(filein2,encoding="utf-8")
w=codecs.open(fileout,encoding="utf-8",mode='w')

x1=f1.read()
x2=f2.read()
x1=re.sub(r'<c>([A-Z]*)</c>',lambda y:y.group(1)if re.search(y.group(0),x2) else y.group(0), x1)
x1=re.sub(r'</c>( *\( *)<c>(.*)</c>( *\) *)<c>',lambda y:y.group(1)+y.group(2)+y.group(3) ,x1)
x1=re.sub(r'</c>( *\[ *)<c>(.*)</c>( *\] *)<c>',lambda y:y.group(1)+y.group(2)+y.group(3) ,x1)

w.write(x1)

