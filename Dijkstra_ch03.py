from collections import defaultdict, deque
from Romania import GenerateGraph

def generateGraph(edges):
	graph = defaultdict(dict)

	for u,v,dist in edges:
		graph[u][v]=dist

	print (graph)

	return graph 


def dijkstra(graph, source, goal):

	queue = []
	distance = {i: float("inf") for i in graph}
	predecessor = {}

	distance[source] = 0

	mdist = 0


	queue.append(source)

	while queue:
		curr=queue.pop(0)
		print (curr)

		for neighbour in graph[curr]:

			print ("neighbour :",neighbour)
			mdist=distance[curr]+graph[curr][neighbour]

			print(mdist)
			print(distance[neighbour])

			if mdist<distance[neighbour]:
				distance[neighbour]=mdist
				print(distance[neighbour])
				predecessor[neighbour]=curr
				queue.append(neighbour)
				print("current queue :", queue)
				print ("predecessor[", neighbour, "] : ",predecessor[neighbour])
			if neighbour==goal:
				return predecessor, distance
		


	print(distance)


	return predecessor, distance

#def shortest_path(edges, source, dest):
def shortest_path(source, dest):
	#graph=generateGraph(edges)
	graph=GenerateGraph()

	predecessor, distance = dijkstra(graph, source, dest)

	curr= 0

	curr= dest

	path = deque()

	while curr != source:
		path.appendleft(curr)
		curr=predecessor[curr]

	path.appendleft(source)

	print ("The distance from", source, "to ", dest, "is : ", distance[dest])
	print ("The path is :  ", path)


#edges = [['s', 'p', 1], ['s', 'e', 9], ['s', 'd', 3], ['p', 'q', 15], ['e', 'r', 2], ['e', 'h', 8], ['d', 'c', 8], ['d','e',2], ['d','b',1], ['r', 'f',1], ['h', 'q', 3], ['h', 'p',2], ['c', 'a', 5], ['b', 'a', 2], ['f', 'g', 2], ['h', 'p', 2], ['r', 'f', 1], ['f', 'g', 2]]
#shortest_path(edges, 's', 'g')

#edges1=[['a','b', 6], ['a', 'c', 3], ['b', 'c', 1], ['c', 'b', 4], ['b', 'd', 2], ['c', 'd', 8], ['c', 'e', 2], ['d', 'e', 9], ['e', 'd', 7]]

#shortest_path(edges1, 'a', 'd')

edges2 = [['A', 'B', 5], ['A','D',3],['A','E',12], ['A','F',5], ['B','A',5],['B','D',1],['B','G',2],['D','B',1],['D','G',1],['D','E',1],['D','A',3],['G','B',2],['G','D',1],['G','C',2],['C','G',2],['C','E',1],['C','F',16],['E','A',12],['E','D',1],['E','C',1],['E','F',2],['F','A',5],['F','E',2],['F','C',16]]
#shortest_path(edges2, 'A', 'G')
shortest_path('Arad', 'Bucharest')