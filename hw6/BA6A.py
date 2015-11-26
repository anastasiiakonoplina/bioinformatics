perm = '-12 +68 +44 -82 +99 +65 +98 +71 -48 +106 +21 -84 -53 +117 -6 +108 -55 +66 -18 -43 +107 +56 -96 -94 -5 +80 -20 +10 +24 -60 +121 -35 +30 +34 +104 +93 +81 -38 -72 -14 +41 +102 -50 -33 +64 +126 +88 +1 -51 +87 +32 +13 +8 -25 -73 -69 +92 -42 -4 +46 -15 +17 +9 -124 +123 -120 -89 -109 -83 +111 +45 +95 -100 -118 +2 -61 -52 -116 +23 -57 -112 -67 +76 +37 +70 +26 -125 +62 -31 -49 -113 -78 -7 +16 +28 -85 -91 -122 -11 +90 -103 -22 -3 -27 -101 -75 -19 -54 -119 -97 +77 -36 -79 -105 -115 +59 -47 -58 +40 -29 +114 +63 -110 +74 -39 -86'

def changeSign(sign):
	if sign == '+':
		res = '-'
	else: 
		res = '+'
	return res

def greedySorting(perm):
	p = []
	signs = {}
	result = []
	perm = perm.split(' ')
	for i in perm:
		integ = int(i)
		if integ > 0:
			signs[integ] = '+'
		else:
			signs[abs(integ)] = '-'
		p.append(abs(integ))
	for e in range(1, len(p) + 1):
		i = p.index(e) 
		if i + 1 != e:
			l1 = list(reversed(p[e-1:(i+1)]))
			p = p[0:e-1] + l1 + p[i+1:]
			for item in l1:
				signs[item] = changeSign(signs[item])
			res = []
			for el in p:
				res.append(signs[el] + str(el))
			result.append(res)
		if signs[e] == '-':
			res =[]
			signs[e] = changeSign(signs[e])
			for el in p:
				res.append(signs[el] + str(el))
			result.append(res)
		final = []
		for array in result:
			final.append('(' + ' '.join(array) + ')')
	return '\n'.join(final)


print greedySorting(perm)
