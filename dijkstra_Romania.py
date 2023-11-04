from Romania import GenerateGraph
from collections import deque

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

			print (neighbour)
			mdist=distance[curr]+graph[curr][neighbour]

			print(mdist)
			print(distance[neighbour])

			if mdist<distance[neighbour]:
				distance[neighbour]=mdist
				print(distance[neighbour])
				predecessor[neighbour]=curr
				queue.append(neighbour)
				print (predecessor[neighbour])
			if neighbour==goal:
				return predecessor, distance
		


	print(distance)


	return predecessor, distance

def shortest_path(source, dest):

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

shortest_path('Arad', 'Bucharest')