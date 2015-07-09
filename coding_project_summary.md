	                       #Markup of Sanskrit Names of Plants
	
	Shubham Vaishnav and Beenoo Yadav , student of Indian School of Mines, Dhanbad ,
worked on project "Markup of Sanskrit Names of Plants". 
As summer intern at Indian institute of technology(IIT) Kharagpur , under supervision professor Pawan Goyal.
The work is done between (18th may to 6 July ) in the year 2015.

	The aim of project is to markup the "sanskrit names of plants and thier botanical 
equivalent" in a data file snp.txt in lines 81-3313. The same is achieved by processing 
the snp.txt file through series of python codes which modified the snp.txt through series
of snp...txt files . the final result is in the file snp06.txt generated  by snp06.py 
python program .

	1)snp01.py this program is identifying the sequence of capital letter and marking them 
by <c>..</c> tag .
ex. "<>but Vs4s identifies it as CARPOPOGON PRURIENS; see: {%kapi-"   this will look like 
"<>but Vs4s identifies it as <c>CARPOPOGON PRURIENS</c>; see: {%kapi-" this in snp01.txt 
and how to run this program is given in notes.txt of pywork folder in repository.
	
	2)snp02.py ,as in snp01.txt the program is marking up the letters of a word which starts 
with a capital letter, but does not consist entirely of capital letters . in snp02.py we are 
removing such c~tags.how to run the program is given in notes.txt.
ex. line 94
snp01.txt, <P>(1) a) <c>C</c>hopra: [<c>COMMIPHORA ROXBURGHII </c>(<c>ARN</c>.) <c>ENGL</c>.] = [<c>C</c>.
snp02.txt, <P>(1) a) Chopra: [<c>COMMIPHORA ROXBURGHII </c>(<c>ARN</c>.) <c>ENGL</c>.] = [<c>C</c>.
	
	3)snp03.py, is doing following improvement
a)move ending space out of segment
ex.line 168
snp02.txt 
<>16-19; Avk; Bpn, p. 365; Chopra; Dutt; <c>DWH </c>2, p. 164-166; Gul;
snp03.txt,
<>16-19; Avk; Bpn, p. 365; Chopra; Dutt; <c>DWH</c> 2, p. 164-166; Gul;
 - the space was kept , but moved it from before </c> to after </c>

 b)move a following period into segment
ex.line 155
snp02.txt
<P>(4) P. <c>CORIACEA C</c>. B. <c>CLARKE </c>(<c>PA </c>1, 2, p. 32: used as a substitute);
snp03.txt
<P>(4) P. <c>CORIACEA C.</c> B. <c>CLARKE</c> (<c>PA</c> 1, 2, p. 32: used as a substitute);

c)merge almost consecutive capitalized segments
ex. line 155
snp02.txt
<P>(4) <c>P. CORIACEA C.</c> <c>B. CLARKE</c> (<c>PA</c> 1, 2, p. 32: used as a substitute);
changed to
<P>(4) <c>P. CORIACEA C. B. CLARKE</c> (<c>PA</c> 1, 2, p. 32: used as a substitute);

	4)snp04.py, tackles where a biological identification spans two lines (starts on one line, ends on
next line.)
ex.
snp03.txt
<>fact that Chopra identifies <c>C. ROXBURGHII ENGL.</c> with <c>C.</c>
<><c>AGALLOCHA ENGL.</c>, distinguished as two species in the Index
snp04.txt
<>fact that Chopra identifies <c>C. ROXBURGHII ENGL.</c> with <c>C.
<>AGALLOCHA ENGL.</c>, distinguished as two species in the Index

slightly different case, lines 101 and 102
snp03.txt
<P>a) <c>COMMIPHORA MUKUL ENGL.</c> = <c>C. ROXBURGHII ENGL.</c> = <c>BAL</c>-
<><c>SAMODENDRUM ROXBURGHII STOCKS</c> = <c>B. WIGHTII ARN.</c>;
snp04.txt
<P>a) <c>COMMIPHORA MUKUL ENGL.</c> = <c>C. ROXBURGHII ENGL.</c> = <c>BAL-
<>SAMODENDRUM ROXBURGHII STOCKS</c> = <c>B. WIGHTII ARN.</c>;

The ending '-' in <c>BAL</c>-    is the difference.

	5)snplist1.py,
generate all c~tag into a file called snp04_list1.txt for snp04.txt

	6)snplist2.py,
arrange all c~tag generated from snplist1.py along with their occurrence in a file snp04_list2.txt 
	
three files were made using snp04_list2.txt 
 snp04_one_noperiod_bot.txt,
 snp04_one_noperiod_nobot.txt,
 snp04_one_period
 
	7)snpo5.py, reads the content of snp04_one_noperiod_bot.txt file into a dictionary these are 
the tags which has to be removed .it is done by following part of program,
for l in f1:
    #Read snp04_one_noperiod_nobot into a dict (nobot)
    #The keys of nobot are the lines of the file, after stripping the line-ending character(s)) 
    l = l.rstrip('\r\n')
    nobot[l] = T

after this program read all c~tag from the snp04.txt and check if it is present in above dictionary,
if yes it removes the c~tag. this is done by following part of program,
for l in f:
    #find c-tags from snp04.txt
    caps=re.findall(r'<c>.*?</c>',l)
    for x in caps:
        #if x in caps
        if x in nobot:
            #if x is in dict(nobot) remove c-tags
            m=re.search(r'<c>(.*?)</c>',x)
            l=re.sub(x,m.group(1),l)

	8)snp06.py,merging parenthetical botanical words 
ex.
snp05.txt,
<P>(3) a) [<c>TRACHYSPERMUM AMMI</c> (<c>LINN.</c>) <c>SPRAGUE</c>] (Chopra) = <c>CARUM
snp06.txt,
<P>(3) a) [<c>TRACHYSPERMUM AMMI (LINN.) SPRAGUE</c>] (Chopra) = <c>CARUM

after this two program snplist1.py and snplist2.py was run on the final data snp06.txt to 
generate  the two files snp06_list1.txt and snp06_list2.txt

NOTE: how to run python programs are given into a file notes.txt under folder pywork in the repository "Markup-Sanskrit-Names-of-Plants" 