import random
from collections import Counter

graph = {}
graph['A'] = ['C', 'D', 'G']
graph['B'] = ['K']
graph['C'] = ['D', 'E']
graph['D'] = ['B', 'J']
graph['E'] = ['F', 'H', 'N']
graph['F'] = ['I']
graph['G'] = ['M']
graph['H'] = ['G']
graph['J'] = ['I']
graph['K'] = ['D']
graph['L'] = ['M']
graph['M'] = ['F', 'L']
graph['N'] = ['A', 'G']
graph['I'] = ['A']

def randwalk(graph, start, visited, nodes):
	nodes.append(start)
	if start not in visited:
		visited.append(start)
	if len(visited) == 14:
		print Counter(nodes)
	else:
		next_node = random.choice(graph[start])
		randwalk(graph, next_node, visited, nodes)

print randwalk(graph, 'A', [], [])