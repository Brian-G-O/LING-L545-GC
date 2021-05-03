Command to run for results:
cat frenchinput.txt | python3 /source/ud-scripts/conllu-analyser.py fr-analyser.tsv | vislcg3 -t -g fr.cg3

First rule removes determiner if there is punctuation to its right.

Second rule removes a pronoun if there is not another pronoun to its right (in this case, "la" is not a pronoun since the next word is not a pronoun).

Third rule removes adverb if there is not a verb to its right.

Fourth rule removes adjective if there is not a noun to its right.

Fifth rule removes noun if there is another noun to its right.

Strange errors I have found, "la" is not listed as having a determiner, instead there are two "le"'s both labeled as DET.

The analyser does not like contractions such as c'est and qu'on. Previously I decided to split them up as "ce est" and "que on" so the analyser can analyze better.

However, I felt it was pointless to use incorrect grammar since the analyser thereotically should be used on real and grammatically correct French phrases.

Rule three used to help disambiguate "que" in relation to "on", but with the given frenchinput.txt file it does nothing.
