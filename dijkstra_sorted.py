from Romania import GenerateGraph, ApprCost
from collections import deque
from collections import OrderedDict
import operator

graph= GenerateGraph()
#print (graph)

def dijkstra(graph, source, dest):

	path = []
	queue = []
	dist = []


	distance ={}
	distance[source]=0

	reach_cost={}
	reach_cost[source]=0

	predecessor = {i:float("inf") for i in graph}
	predecessor[source] =source

	queue.append(source)

	iteration =0

	while queue:
		curr=queue.pop(0)
		#print(curr)
		#print(distance[curr])

		if curr==dest:
			return predecessor, iteration

		for neighbour in graph[curr]:
			#print ("neighbour: ", neighbour)
			distance[neighbour]=distance[curr]+graph[curr][neighbour]
			#print(distance[neighbour])
			if predecessor[curr] != neighbour:
				predecessor[neighbour]=curr

		
		distance=dict(sorted(distance.items(), key=lambda item: item[1]))
		#print(distance)

		(k := next(iter(distance)), distance.pop(k))

		#print(distance)

		lcost_next = list(distance.keys())[0]
		queue.append(lcost_next)
		#print("lcost_next:", lcost_next)

		#for neighbour in graph[curr]:
		#	if lcost_next==neighbour:
		#		print("Yes")
		#		predecessor[lcost_next]=curr
		#	else:
		#		continue

		#if predecessor[lcost_next] !=float("inf"):
		#	print(predecessor[lcost_next])
		#else:
		#	print("Not yet assigned")


		#for items in sorted_distance:
		#	predecessor[curr]=get_keys_from_value(sorted_distance, list(sorted_distance.values())[0])
		#	print (predecessor[curr])

		iteration +=1





		



			
	return predecessor, iteration

	

def shortest_path(source, dest):
	graph=GenerateGraph()
	predecessor, iteration = dijkstra(graph, source, dest)

	path = deque()

	curr=dest

	while curr != source:
		path.appendleft(curr)
		curr=predecessor[curr]
		#print("path :", path)

	path.appendleft(source)

	print("Shortest path from ", source, "to ", dest, "is : ", path)
	print("Number of iteration for Dijkstra UCS is: ", iteration)

shortest_path('Arad', 'Bucharest')
