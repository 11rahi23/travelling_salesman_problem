from collections import defaultdict, deque
def generateGraph(edges):
	graph = defaultdict(dict)
	for u,v, dist in edges:
		graph[u][v] = dist

	return graph

weighted_edges = [['a','b', 6], ['a', 'c', 3], ['b', 'c', 1], ['c', 'b', 4], ['b', 'd', 2], ['c', 'd', 8], ['c', 'e', 2], ['d', 'e', 9], ['e', 'd', 7]]
directed_wieghted_graph = generateGraph(weighted_edges)

#print(directed_wieghted_graph)

def dijkstra(graph, source):
	queue =[]
	reached = []

	distance = {i: float("inf") for i in graph}
	distance[source]=0
	mdist = 0

	predecessor = {}


	reached.append(source)

	queue.append(source)

	print (distance[source])

	while queue:
		curr=queue.pop(0)
		print (curr)
		if curr not in reached:
			reached.append(curr)

		for neighbour in graph[curr]:
			print (neighbour)
			mdist=distance[curr]+graph[curr][neighbour]
			print(mdist)
			print(distance[neighbour])

			if mdist<distance[neighbour]:
				distance[neighbour] = min(mdist, distance[neighbour])
				print(distance[neighbour])
				queue.append(neighbour)
				predecessor[neighbour]=curr
				print(predecessor[neighbour])

	print (distance, reached)
	

	return distance, predecessor

def shortest_path(graph, source, dest):

	distance, predecessor = dijkstra(graph, source)
	path = deque()
	curr=dest

	while curr != source:
		path.appendleft(curr)
		curr=predecessor[curr]

	path.appendleft(source)

	print (path)



#shortest_path(directed_wieghted_graph, 'a', 'e')

edges = [['s', 'p', 1], ['s', 'e', 9], ['s', 'd', 3], ['p','q', 15], ['e', 'r', 2], ['e', 'h', 8], ['d', 'c', 8], ['d','e',2], ['d','b',1], ['r', 'f',1], ['h', 'q', 3], ['c', 'a', 5], ['e', 'r', 2], ['b', 'a', 2], ['f', 'g', 2], ['h', 'p', 2], ['r', 'f', 1], ['p', 'q', 15], ['f', 'g', 2]]

graph1=generateGraph(edges)

shortest_path(graph1, 's', 'g')




