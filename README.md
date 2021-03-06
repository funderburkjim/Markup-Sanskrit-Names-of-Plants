# Markup-Sanskrit-Names-of-Plants
Proposal for Project for one of Pawan Goyal's students

The initial aim of this project is to improve one detail of the markup of
one of the digitizations at the [Cologne Sanskrit-Lexicon](http://www.sanskrit-lexicon.uni-koeln.de/).

The digitization in question is of *Meulenbeld's Sanskrit names of plants and their botanical equivalents*, which is referred to in the Cologne digitizations by
the code SNP.  The primary form of the digitization for this work is a text
file snp.txt (utf-8 encoding), a copy of which is [here](https://github.com/funderburkjim/Markup-Sanskrit-Names-of-Plants/blob/master/snp.txt) in this repository.

Our starting point, snp.txt, actually has two parts:
* Appendix 4 from the book mentioned above, comprising lines 81-3313 of snp.txt
* Some additions to the book, comprising lines 3424-4536 of snp.txt

When this project is completed, there will be a file snp_adj.txt in the
repository which will be a modified version of snp.txt; furthermore, the
modifications will be accomplished by one or more Python(version 2.7) programs and possibly some ancillary text files, also in the repository. The sequence of steps required to construct snp_adj.txt from snp.txt will be specified by a 
shell script (redo_adj.sh),  Thus, the construction of the adjusted digitization (snp_adj.txt) will be accomplished in a repeatable (programmatic) way - by rerunning the shell script.

  The first (and perhaps only) part of
the project will deal with capitalization in  Appendix 4 part of snp.txt.  

[Issue#1](https://github.com/funderburkjim/Markup-Sanskrit-Names-of-Plants/issues/1) describes the context of this capitalization problem.


[Issue#2](https://github.com/funderburkjim/Markup-Sanskrit-Names-of-Plants/issues/1) describes the motivating example of this capitalization problem.

[Issue#3](https://github.com/funderburkjim/Markup-Sanskrit-Names-of-Plants/issues/3) provides some suggestions that might (or might not) be helpful in solving the capitalization problem.

When the capitalization problem based on the first part (Appendix 4) is solved, a next step would be to identify and mark the scientific plant names appearing in the second part of the digitization.
