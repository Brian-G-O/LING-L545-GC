Error found when trying to use twol file:
$ hfst-twolc trmorpho.twol -o trmorpho.twol.hfst
Reading input from trmorpho.twol.
Writing output to trmorpho.twol.hfst.
Exception: HfstException in file: htwolcpre1-parser.yy on line: 541

This was not an isolated incident, as I tried this same command on the grn.lexc file and got the same error.

Instead, I decided to use both variations of a and e, i and ı, and k and ğ to show the potential characters in the .lexc file.
Ideally, the twol file would have been used and would have significantly cut down on the bloat.

Commands to run to use the twol file:
$ hfst-twolc trmorpho.twol -o trmorpho.twol.hfst
then using the Makefile:
$ make
then:
hfst-fst2strings trmorpho.gen.hfst

Minimal twol rules were added, ideally more would have been added if I was able to use it and see if I was getting the correct results.
