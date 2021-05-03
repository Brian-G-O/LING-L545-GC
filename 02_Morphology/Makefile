all: trmorpho.gen.hfst

trmorpho.lexc.hfst: trmorpho.lexc
	hfst-lexc trmorpho.lexc -o trmorpho.lexc.hfst
trmorpho.twol.hfst: trmorpho.twol
	hfst-twolc trmorpho.twol -o trmorpho.twol.hfst
trmorpho.gen.hfst: trmorpho.lexc.hfst trmorpho.twol.hfst
	hfst-compose-intersect -1 trmorpho.lexc.hfst -2 trmorpho.twol.hfst -o trmorpho.gen.hfst
