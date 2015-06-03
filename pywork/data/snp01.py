import os
import codecs
import unicodedata
os.chdir("C:\Users\HP PC\Desktop\summer project\Markup-Sanskrit-Names-of-Plants")
f=codecs.open("snp.txt",encoding="utf-8")
w=codecs.open("snp01.txt",encoding="utf-8",mode='w')
lineno=0
for l in f:
    lineno+=1
    if lineno>=81 and lineno<=3313:
        if l[1]=="P" or l[1]=="H":
            t=3
        else:
            t=2
        issequence=0
        for x in range(len(l)):
            if x<t:
                w.write(l[x])
            else:
                if issequence==0:
                    if ord(l[x])>=65 and ord(l[x])<=90:
                        w.write("<c>")
                        issequence=1
                        w.write(l[x])
                    else:
                        w.write(l[x])
                else:
                    if ord(l[x])>=65 and ord(l[x])<=90:
                        w.write(l[x])
                    else:
                        if l[x] != " ":
                            w.write("<\c>")
                            issequence=0
                        w.write(l[x])
    else:
        w.write(l)
    
    
                        
                        
                    
                        

                    
                    
            
            
            
                
        
                
                
            
    

