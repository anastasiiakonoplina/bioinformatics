import random
import networkx as nx

graph = ['0 -> 2',
'1 -> 3',
'2 -> 1',
'3 -> 0,4',
'6 -> 3,7',
'7 -> 8',
'8 -> 9',
'9 -> 6']

def makeGraph(graph):
	res = []
	pair = []
	for edge in graph:
		pair.append(edge.split(" -> "))
	for string in pair:
		if ',' in string[1]:
			nodes = string[1].split(",")
			for node in nodes:
				res.append((string[0], node))
		else:
			res.append((string[0], string[1]))
	return res

def eulerianGraph(graph):
	res = []
 	graph = makeGraph(graph)
 	G = nx.DiGraph()
 	G.add_edges_from(graph)
 	path = list(nx.bfs_edges(G))
 	for edge in path:
 		res.append(edge[0])
 	first = res[0]
 	res = '->'.join(res) + '->' + first
 	return res

print eulerianGraph(graph)

