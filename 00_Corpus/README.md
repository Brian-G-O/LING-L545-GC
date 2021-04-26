The segmenter.py code handles Turkish text by segmenting each line by punctuation (ex. !,?,.).
Some tokens such as Dr. and Prof. used the period and would incorrectly segment it as a sentence, these were added as exceptions.
Other exceptions include, "vs., b., III., etc.".
Out of the 98 lines, 91 are well-segmented sentences. 7 lines are either one word sentences (Which I assumed was intended to be on its own given the first letter is capitalized and a sentence ends directly before it) (ex. Ölümü.), Titles using a colon (ex. Kore Savaşı:),
and one sentence inside parenthesis that I found difficult to seperate from the sentence it was inside (ex. (... sürer.)).
