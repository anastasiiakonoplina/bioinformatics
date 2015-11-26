table = {}
table['G'] = 57
table['A'] = 71
table['S'] = 87
table['P'] = 97
table['V'] = 99
table['T'] = 101
table['C'] = 103
table['I'] = 113
table['L'] = 113
table['N'] = 114
table['D'] = 115
table['K'] = 128
table['Q'] = 128
table['E'] = 129
table['M'] = 131
table['H'] = 137
table['F'] = 147
table['R'] = 113
table['Y'] = 163
table['W'] = 186

protein = 'NQEL'

def theorSpectrum(protein, table):
	peps = [protein]
	res = [0]
	res1 = []
	for size in range(1, len(protein)):
		for i in range (0, len(protein)):
			if size <= len(protein[i:i + size]):
				peps.append(protein[i:i + size])
			else:
				peps.append(protein[i:i + size] + protein[0:size - len(protein[i:i + size])])
	for pep in peps:
		num = 0
		for l in pep:
			num = num + table[l]
		res.append(num)
	res = sorted(res)
	for r in res:
		res1.append(str(r))
	return ' '.join(res1)

print theorSpectrum(protein, table)







