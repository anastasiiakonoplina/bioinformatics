import itertools

dna = ["GTACTGTATTTAATGGCACGTCCTG", "GGAAGCTAAGTCCGGACGCTGGCCC", "TCCAGGTGTGCAAAAAAGTTGGTAA", "CCCACCGGGACGTTCTCCGGAGTGC", "AACGCTCCGGTAAACTACGACGCAT", "TTAGCGGAAAGCGGTCGGTCTCCGG", "TTCTGGCCGAAAAGGAAAGGTCCGG", "ATTTGATAATTGCGTGCGCCTCCGG", "TCCCGGGTACCGGGCATATCTTGCC", "TCCTGCTTCGGTCCTCATCTCGTAA"]
k = 5
d = 1

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

def appxMatch(pattern, string, ham_dist):
	res = []
	for i in range(0, len(string) - len(pattern) + 1):
		dist = hammingDistance(pattern, string[i:(i + len(pattern))])
		if dist <= ham_dist:
			res.append(i)
	return res

def motifEnumeration (dna, k, d):
	patterns = {}
	string = dna[0]
	pats = []
	for i in range(0, len(string) - k + 1):
		pats.extend(generateMismatches(string[i:(i + k)], "ATCG", d))
	for pat in pats:
		count = 0
		for item in dna:
			if (len(appxMatch(pat, item, d)) > 0):
				count += 1
		if (count == len(dna)) & (pat not in patterns):
			patterns[pat] = count
	res = " ".join(patterns)
	return res

print motifEnumeration(dna, k, d)