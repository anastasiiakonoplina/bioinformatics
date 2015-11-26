import itertools

dna = ["CTGGGGTTAATCCACGCGGACCTGTCGGTTGTTATTGAAGAG", "TAGCCCTACTGAACAGGCATCCGGGTTACTGCCAGGTCCTAG", "GTTATTTTCAGAGGCGAAAGAGAACGGATGCCATCACGGGTG", "CGTGGACATAAAAGAATGGGAAATTACTCTGTTAATACCAAC", "TGCTGAGCGCCATTGAATGTTACTACACAAATTTGATGGATT", "GTCGCCGTTAAGCGCATTCGCAGGGTTAATCCATAAGCTACT", "CGCCCGAATCACAGGTTCCAATCCCGGTCAGTTAGTTGAAGT", "AAAAGAGTTATTTCAACTGCCGAGCCACGTAGTCTGACTCAG", "ATACGAGAGCTGCTTCTTGTTACTAAAGAAATATATGAGCTG", "GTTAATTCCTGTATGGGTAGTAAACAGATACGAACCCGTGAG"]
k = 6

def generateMismatches(word, letters, i):
	res = []
	for d in range(i+1):
	    for locs in itertools.combinations(range(len(word)), d):
	      thisWord = [[char] for char in word]
	      for loc in locs:
	        origChar = word[loc]
	        thisWord[loc] = [l for l in letters if l != origChar]
	      for poss in itertools.product(*thisWord):
	      	res.append("".join(poss))
	return res

def hammingDistance(str1, str2):
	ham_dist = 0
	for i in range(0, len(str1)):
		if str1[i] != str2[i]:
			ham_dist += 1
	return ham_dist


def medianString(dna, k):
	all_words = []
	words = {}
	uwords = []
	for item in dna:
		for i in range(0, len(item) - k + 1):
			word = item[i: i + k]
			all_words.extend(generateMismatches(word, "ATCG", k - 1))
			uwords = list(set(all_words))
	for word in uwords:
		distance = 0
		for item in dna:
			dist = []
			for i in range(0, len(item) - k + 1):
				dist.append(hammingDistance(word, item[i:i + k]))
			distance += min(dist)
		words[word] = distance
	minValue = min(words.values())
	result = [key for key in words.keys() if words[key] == minValue] 
	return result

print medianString(dna, k)