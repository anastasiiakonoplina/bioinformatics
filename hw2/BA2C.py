import numpy as np

string = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
profile = [[0.2, 0.2, 0.3, 0.2, 0.3], [0.4, 0.3, 0.1, 0.5, 0.1], [0.3, 0.3, 0.5, 0.2, 0.4], [0.1, 0.2, 0.1, 0.1, 0.2]]


def mostProb(string, k, profile):
	letters = ['A', 'C', 'G', 'T']
	count = 0
	for i in range(0, len(profile[0])):
		column = []
		for j in range(0, 4):
			column.append(profile[j][i])

		
	return column

print mostProb(string, k, profile)
