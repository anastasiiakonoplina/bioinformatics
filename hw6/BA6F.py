chrom ='+1 -2 -3'
def preprocess(perm):
	p = []
	perm = perm.split(' ')
	for i in perm:
		integ = int(i)
		p.append(integ)
	return p

def chromToCycle(chrom):
	nodes = []
	for item in chrom:
		if item > 0:
			nodes.append(str(2*item-1))
			nodes.append(str(2*item))
		if item < 0:
			nodes.append(str(-2*item))
			nodes.append(str(-2*item-1))
	return '(' + ' '.join(nodes) + ')'

print chromToCycle(preprocess(chrom)) 