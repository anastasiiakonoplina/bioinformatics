def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

genom = readGenome('lambda_virus.fa')

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if (t[i+j] != p[j]):  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

def naive2m(p, t):
    occurrences = []
    m =0
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if (t[i+j] != p[j]):  # compare characters
            	m += 1
            	if m > 2:
	                match = False
	                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

print len(naive('AGGT', genom)) + len(naive(reverseComplement('AGGT'), genom))
print len(naive('TTAA', genom))
print min(naive('ACTAAGT', genom), naive(reverseComplement('ACTAAGT'), genom))
print min(naive('AGTCGA', genom), naive(reverseComplement('AGTCGA'), genom))



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

print appxMatch('AGGAGGTT', genom, 2)

