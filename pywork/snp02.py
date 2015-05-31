import os
import codecs
import unicodedata
import sys

filein=sys.argv[1] 
fileout=sys.argv[2]
f=codecs.open(filein,encoding="utf-8") #open input file(snp.txt)
w=codecs.open(fileout,encoding="utf-8",mode='w') #create new file(snp01.txt) for output
lineno=0 
for l in f: 
    lineno+=1
    if lineno>=81 and lineno<=3313:
        if l[1]=="P" or l[1]=="H":
            t=3
        else:
            t=2
        issequence=0 #flag to indicate if a sequence of capital letters is being processed , issequence=0(no such sequence) ,issequence=1(sequence is being processed)
        for x in range(len(l)):
            if x<t:
                w.write(l[x])
            else:
                if issequence==0: # if sequence is not 
                    if ord(l[x])>=65 and ord(l[x])<=90:# if capital letter
                        if (ord(l[x+1])>=65 and ord(l[x+1])<=90)or(l[x+1]==" "):# if it is not a normal word
                            w.write("<c>") # start a new sequence
                            issequence=1 #issequence=1 
                        w.write(l[x]) 
                    else:# if not a capital letter write as it is
                        w.write(l[x]) 
                else:# if sequence is there
                    if ord(l[x])>=65 and ord(l[x])<=90:# if capital letter
                        w.write(l[x])
                    else:# if not capital letter
                        if l[x] != " ":# if not white space
                            w.write("</c>")# end the sequence
                            issequence=0 # issequence=1
                        w.write(l[x]) 
    else:
        w.write(l)
    
    
                        
                        
                    
                        

                    
                    
            
            
            
                
        
                
                
            
    

