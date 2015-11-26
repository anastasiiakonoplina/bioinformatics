string = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

def hammingDistance(str1, str2):
	ham_dist = 0
	for i in range(0, len(str1)):
		if str1[i] != str2[i]:
			ham_dist += 1
	return ham_dist

def appxMatch(pattern, string, ham_dist):
	res = []
	for i in range(0, len(string) - len(pattern)):
		dist = hammingDistance(pattern, string[i:(i + len(pattern))])
		if dist <= ham_dist:
			res.append(i)
	return res

def freqWordsMismatch(string, k, d):
	res = {}
	all_words = []
	words = []
	letters = ['A', 'C', 'T', 'G']
	for i in range(0, len(string) - k -1):
		word = string[i:(i + k)]
		words.append(word)
		for letter in word:
			mismatch = [letters[j] for j in range(len(letters)) if letters[j] != letter]
			for m in mismatch:
				new_word = word.replace(letter,m)
				if new_word not in words:
					words.append(new_word)
	for word in words:
		res[word] = len(appxMatch(word, string, d))
	maxValue = max(res.values())
	result = [key for key in res.keys() if res[key] == maxValue] 
	return result
			
			

print complement(string)





print freqWordsMismatch(string, k, d)
