perm ='+1 -2 -3 +4'

def preprocess(perm):
	p = []
	perm = perm.split(' ')
	for i in perm:
		integ = int(i)
		p.append(integ)
	return p


def bp_num(p, breaks):
	print breaks
	start = p[0]
	for i in range(1, len(p)):
		if start > 0:
			if (start + i) != p[i]:
				breaks += 1
				p = p[i:]
				bp_num(p, breaks)
		if start < 0:
			if (start + i) != p[i]:
				breaks += 1
				p = p[i:]
				bp_num(p, breaks)
	return breaks


print bp_num(preprocess(perm), 0)


