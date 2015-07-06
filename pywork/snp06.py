import re
import sys
import codecs

filein=sys.argv[1]
fileout=sys.argv[2]
fileout1=sys.argv[3]

f=codecs.open(filein,encoding="utf-8")
w=codecs.open(fileout,encoding="utf-8",mode='w')
w1=codecs.open(fileout1,encoding="utf-8",mode='w')
lineno=0
for l in f:
    lineno+=1
    l1=l
    l=re.sub(r'</c>( *?\()<c>(.*?)</c>(\) *?)<c>',lambda s:s.group(1)+s.group(2)+s.group(3),l)
    #remove the tags of expression containing consecutive <c> and </c> tags seperated by '(' or ')' with 0 or more spaces
    #like(line 95)-> <>AGALLOCHA</c> (<c>WIGHT ET ARN.</c>) <c>ENGL.</c>] = <c>BALSAMODENDRUM
    #should look like->  <>AGALLOCHA WIGHT ET ARN. ENGL.</c>] = <c>BALSAMODENDRUM


    l=re.sub(r'</c>( *?\[)<c>(.*?)</c>(\] *?)<c>',lambda s:s.group(1)+s.group(2)+s.group(3),l)
        #remove the tags of expression containing consecutive <c> and </c> tags seperated by '[' or ']' with 0 or more spaces
        #like)line 343)->  <P>(3) <c>N. ODORATA</c> [<c>SOLAND. IN</c>] <c>AIT.</c> (Ainslie 2, p. 381);
        #should look like ->  <P>(3) <c>N. ODORATA SOLAND. IN AIT.</c> (Ainslie 2, p. 381);

    if l!=l1:
        #write log of lines which were changed
        w1.write("%d  %s"%(lineno,l1))
        w1.write("%d  %s"%(lineno,l))
        w1.write("\n")
    w.write(l)

        
