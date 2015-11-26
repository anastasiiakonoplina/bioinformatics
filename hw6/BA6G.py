cycle = '2 1 3 4 5 6 8 7 9 10 12 11 13 14 16 15 18 17 19 20 21 22 24 23 25 26 27 28 29 30 31 32 34 33 36 35 37 38 40 39 42 41 44 43 46 45 47 48 49 50 52 51 53 54 55 56 57 58 59 60 62 61 63 64 65 66 67 68 69 70 71 72 73 74 76 75 77 78 80 79 82 81 83 84 86 85 88 87 90 89 91 92 94 93 96 95 98 97 100 99 102 101 103 104 106 105 107 108 109 110 111 112 113 114 115 116 117 118 120 119 122 121 123 124 126 125 128 127 130 129 131 132 134 133 135 136'

def preprocess(perm):
	p = []
	perm = perm.split(' ')
	for i in perm:
		integ = int(i)
		p.append(integ)
	return p

def cycleToChrom(cycle):
	res = []
	for i in range(0, len(cycle) - 1, 2):
		if cycle[i] < cycle[i+1]:
			res.append('+' + str(cycle[i+1]/2))
		else:
			res.append('-' + str(cycle[i]/2))
	return ' '.join(res)

print cycleToChrom(preprocess(cycle))