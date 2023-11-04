from Romania import GenerateGraph, ApprCost
from collections import deque

graph= GenerateGraph()
#print (graph)

def Greedy(graph, source, dest):

	path = []
	queue = []

	cost = ApprCost()


	distance ={i:float("inf") for i in graph}
	distance[source]=0
	minNeighbour = float("inf")

	predecessor = {}

	queue.append(source)

	while queue:
		curr=queue.pop(0)
		print(curr)
		print(cost[curr])

		if curr==dest:
			return predecessor


		for neighbour in graph[curr]:
			print(neighbour)
			
			if cost[neighbour]<minNeighbour:
				minNeighbour = cost[neighbour]
				if cost[neighbour]<cost[curr]:
					predecessor[neighbour]=curr
					print(predecessor[neighbour])
					queue.append(neighbour)

	return predecessor

	

def shortest_path(source, dest):
	graph=GenerateGraph()
	predecessor = Greedy(graph, source, dest)

	path = deque()

	curr=dest

	while curr != source:
		path.appendleft(curr)
		curr=predecessor[curr]

	path.appendleft(source)

	print(path)

shortest_path('Arad', 'Bucharest')





