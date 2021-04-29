import sys
#creates dictionary
dictionary= [((line), line.strip()) for line in open("japanese.dict").readlines()]
dictionary.sort()
#reverses its order
dictionary.reverse()

#defines maxmatch
def maxmatch(sentence, dictionary):
	if sentence == '':
		return []
		#should return nothing if sentence is blank
	for i in range(0, len(sentence)):
		firstword= sentence[i:]
		#looks for first i chars of sentence
		remainder= sentence[:i]
		#rest of sentence
		if firstword in dictionary:
			return list([firstword] + maxmatch(remainder, dictionary))
			#returns firstword if in dictionary
		firstword= sentence[0]
		#should reset first word [0]
		remainder= sentence[1:]
		#should reset remainder 
		return list([firstword] + maxmatch(remainder, dictionary))
		#repeats function
line= sys.stdin.readline()
#reads line from cat of .dict file
while line:
	print(' '.join(maxmatch(line.strip('\n'), dictionary)))
	line= sys.stdin.readline()
#while it reads the lines, prints the maxmatch results
