To run maxmatch and get results out of japanese.dict, run this command:

cat japanese.dict | python3 maxmatch2.py

My program had an average WER of 98.7715881540586%.

This was found by taking the sums of percents (which added up to 1287388.38%) and dividing them by the total number of WER results (13,034).

Examples to support my findings include:

100% examples:

REF: に
HYP: れ
EVA: S
WER: 100.00%

REF: 不 快
HYP:   に
EVA: D S
WER: 100.00%

REF: 感
HYP: 不
EVA: S
WER: 100.00%

REF: を
HYP: 快
EVA: S
WER: 100.00%

REF: 示 す
HYP:   感
EVA: D S
WER: 100.00%

REF: 住 民
HYP:   を
EVA: D S
WER: 100.00%

REF: は
HYP: 示
EVA: S
WER: 100.00%

REF: い
HYP: す
EVA: S
WER: 100.00%

REF: ま し
HYP:   住
EVA: D S
WER: 100.00%

REF: た
HYP: 民
EVA: S
WER: 100.00%

REF: が
HYP: は
EVA: S
WER: 100.00%

REF: ,
HYP: い
EVA: S
WER: 100.00%

REF: 現 在
HYP:   ま
EVA: D S
WER: 100.00%

Less than 100% examples:

REF: こ れ
HYP: こ
EVA:   D
WER: 50.00%

REF: は
HYP: は
EVA:
WER: 0.00%

REF: を
HYP: を
EVA:
WER: 0.00%

There are very few less-than-100% WER instances, however more can be found by looking at the numbers.txt file.
