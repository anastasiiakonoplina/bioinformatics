import random

k = 8
t = 5

dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

def formProfile(word, k):
	alpha = ['A', 'C', 'G', 'T']
	profile = [[0] * k for _ in range(4)]
	for w in word:
		for i in range(0, len(w) - k +1):
			string = w[i:i+k]
			for l in range(0, len(string)):
				index = alpha.index(string[l])
				profile[index][l] += 1.0/((len(w) - k + 1) * len(word))
	return profile

def score(array):
	alpha = ['A', 'C', 'G', 'T']
	res = 0
	for i in range(0, len(array[0])):
		let = {'A':0, 'C':0, 'G':0, 'T':0}
		for word in array:
			let[word[i]] += 1
		maxval = max(let, key=let.get)
		for word in array:
			if word[i] != maxval:
				res += 1
	return res

def mostProb(string, k, profile):
	alpha = ['A', 'C', 'G', 'T']
	max_prob = 0
	res = string[0:k]
	for i in range(0, len(string) - k + 1):
		prob = 0
		word = string[i:i+k]
		prob = 1
		for l in range(0, len(word)):
			index = alpha.index(word[l])
			prob = prob * profile[index][l]
		if prob > max_prob:
			max_prob = prob
			res = word
	return res

def randomMotifSearch(dna, k ,t):
	motifs = []
	for string in dna:
		rand = random.randint(0, len(string) - k + 1)
		motifs.append(string[rand:rand + k])
	bestMotifs = list(motifs)
	for i in range(0, 1000):
		profile = formProfile(bestMotifs, k)
		motifs = []
		for string in dna:
			motifs.append(mostProb(string, k, profile))
		if score(motifs) < score(bestMotifs):
			bestMotifs = list(motifs)
	return '\n'.join(bestMotifs)


print randomMotifSearch(dna, k, t)
