import itertools

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

mass = 1024


def peptideCount(mass):
	amount = mass/57
	all_peptides = map(''.join, itertools.product(table, repeat=10))
	return all_peptides

print peptideCount(mass)