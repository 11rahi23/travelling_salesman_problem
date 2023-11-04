from Romania import GenerateGraph, ApprCost
from collections import deque
from collections import OrderedDict
import operator

graph= GenerateGraph()
#print (graph)
global distance, reach_cost, predecessor, cost, source, dest

distance ={i:float("inf") for i in graph}
distance['Arad']=0

reach_cost={}
reach_cost['Arad']=0

predecessor = {i:float("inf") for i in graph}
predecessor['Arad'] =None

cost = ApprCost()
# predecessor1 = {i:float("inf") for i in graph}
# predecessor1[source] =source

# predecessor2 = {i:float("inf") for i in graph}
# predecessor2[source] =source

# predecessor3 = {i:float("inf") for i in graph}
# predecessor3[source] =source

def Astar(graph, source, dest):

	path = []
	queue = []
	dist = []
	path1 = []
	queue1 = []
	dist1 = []
	path2 = []
	queue2 = []
	dist2 = []
	path3 = []
	queue3 = []
	dist3 = []

	#cost = ApprCost()


	#weighted Astar
	#weight=1.01

	global distance, reach_cost, predecessor, cost



	# distance ={i:float("inf") for i in graph}
	# distance[source]=0

	# reach_cost={}
	# reach_cost[source]=0

	# predecessor = {i:float("inf") for i in graph}
	# predecessor[source] =source

	# predecessor1 = {i:float("inf") for i in graph}
	# predecessor1[source] =source

	# predecessor2 = {i:float("inf") for i in graph}
	# predecessor2[source] =source

	# predecessor3 = {i:float("inf") for i in graph}
	# predecessor3[source] =source



	iteration =0

	seed1, seed2, seed3 = initial_dfs(source)
	while True:
	

		# reach_cost1 = beam1(seed1)
		# reach_cost2 = beam2(seed2)
		# reach_cost3 = beam3(seed3)

		# reach_cost= {**reach_cost1, **reach_cost2, **reach_cost3}

		reach_cost=dict(sorted(reach_cost.items(), key=lambda item: item[1]))
		# print("reach_cost dictionary: ", reach_cost)

		seed1 = list(reach_cost.keys())[0]
		#print("seed1:", seed1)
		seed2 = list(reach_cost.keys())[1]
		#print("seed2:", seed2)
		seed3 = list(reach_cost.keys())[2]
		#print("seed3:", seed3)


		if seed1 == dest:
			print_predecessor(source)
			break

		#if seed2 == dest:
		#	print_predecessor(source)
		#	break

		#if seed3 == dest:
		#	print_predecessor(source)
		#	break

		beam1(seed1)
		beam2(seed2)
		beam3(seed3)



		



def initial_dfs(source):

	global distance, reach_cost, predecessor, cost, dest

	print("initial_dfs")

	curr=source
	graph=GenerateGraph()
	#print(curr)
	#print(cost[curr])
	#print(reach_cost[curr])

	for neighbour in graph[curr]:
	#	print ("neighbour: ", neighbour)
		distance[neighbour]=distance[curr]+graph[curr][neighbour]
		#for weighted Astar
		#reach_cost[neighbour]=distance[neighbour]+weight*cost[neighbour]
		reach_cost[neighbour]=distance[neighbour]+cost[neighbour]
	#	print(distance[neighbour])
	#	print(reach_cost[neighbour])
		#if predecessor[neighbour] is None:
			#predecessor[neighbour]=curr
		if predecessor[curr] != neighbour:
			predecessor[neighbour]=curr
			#print("predecessor[", neighbour,"] = ", curr)

		#print("predecessor after initial_dfs: ", predecessor)

		
	reach_cost=dict(sorted(reach_cost.items(), key=lambda item: item[1]))
	#print(reach_cost)

	(k := next(iter(reach_cost)), reach_cost.pop(k))

	print(reach_cost)

	seed1 = list(reach_cost.keys())[0]
	print("seed1 from initial_dfs: ", seed1)

	seed2 = list(reach_cost.keys())[1]
	print("seed1 from initial_dfs: ", seed2)

	seed3 = list(reach_cost.keys())[2]
	print("seed1 from initial_dfs: ", seed3)


		

	return seed1, seed2, seed3



			
	#return predecessor, iteration

def beam1(seed1):

	global distance, reach_cost, predecessor, cost, dest

	#print("beam1")

	curr=seed1
		#print(curr)
		#print(cost[curr])
		#print(reach_cost[curr])

	if curr==dest:
		return
		# print_predecessor(curr)			
	for neighbour in graph[curr]:
		#print ("neighbour from beam1: ", neighbour)
		distance[neighbour]=distance[curr]+graph[curr][neighbour]
			#for weighted Astar
			#reach_cost[neighbour]=distance[neighbour]+weight*cost[neighbour]
		reach_cost[neighbour]=distance[neighbour]+cost[neighbour]
	#		print(distance[neighbour])
	#		print(reach_cost[neighbour])
		if predecessor[curr] != neighbour:
			predecessor[neighbour]=curr
			#print("predecessor[", neighbour,"] = ", curr)

		#print("predecessor after beam1 neighbouring: ", predecessor)


		
	reach_cost=dict(sorted(reach_cost.items(), key=lambda item: item[1]))
	#print("reach_cost from beam1: ",reach_cost)

	reach_cost.pop(curr)

	#(k := next(iter(reach_cost)), reach_cost.pop(k))

	# print("reac_cost from beam1 after pruning init: ", reach_cost)


			
	return 

def beam2(seed2):

	global distance, reach_cost, predecessor, cost, dest
	#print(beam2)

	curr=seed2
		#print(curr)
		#print(cost[curr])
		#print(reach_cost[curr])

	if curr==dest:
		# print_predecessor(source)
		return		
	for neighbour in graph[curr]:
		#print ("neighbour from beam2: ", neighbour)
		distance[neighbour]=distance[curr]+graph[curr][neighbour]
			#for weighted Astar
			#reach_cost[neighbour]=distance[neighbour]+weight*cost[neighbour]
		reach_cost[neighbour]=distance[neighbour]+cost[neighbour]
	#		print(distance[neighbour])
	#		print(reach_cost[neighbour])
		if predecessor[curr] != neighbour:
			predecessor[neighbour]=curr
			#print("predecessor[", neighbour,"] = ", curr)

		#print("predecessor after beam2 neighbouring: ", predecessor)

		
	reach_cost=dict(sorted(reach_cost.items(), key=lambda item: item[1]))
	#print("reach_cost from beam2: ",reach_cost)
	reach_cost.pop(curr)
	
	#(k := next(iter(reach_cost)), reach_cost.pop(k))

	# print("reach_cost from beam2 after pruning init: ",reach_cost)


			
	return 

def beam3(seed3):

	global distance, reach_cost, predecessor, cost, dest
	#print(beam3)

	curr=seed3
		#print(curr)
		#print(cost[curr])
		#print(reach_cost[curr])

	if curr==dest:
		return
		# print_predecessor(curr)		
	for neighbour in graph[curr]:
		#print ("neighbour from beam3: ", neighbour)
		distance[neighbour]=distance[curr]+graph[curr][neighbour]
			#for weighted Astar
			#reach_cost[neighbour]=distance[neighbour]+weight*cost[neighbour]
		reach_cost[neighbour]=distance[neighbour]+cost[neighbour]
	#		print(distance[neighbour])
	#		print(reach_cost[neighbour])
		if predecessor[curr] != neighbour:
			predecessor[neighbour]=curr
			#print("predecessor[", neighbour,"] = ", curr)
		#print("predecessor after beam3 neighbouring: ", predecessor)

		
	reach_cost=dict(sorted(reach_cost.items(), key=lambda item: item[1]))
	#print("reach_cost from beam3: ",reach_cost)

	reach_cost.pop(curr)

	#(k := next(iter(reach_cost)), reach_cost.pop(k))

	# print("reach_cost from beam3 after pruning init: ",reach_cost)

	return 


def print_predecessor(source):
	global predecessor, dest
	path = deque()

	curr=dest

	while curr != source:
		path.appendleft(curr)
		curr=predecessor[curr]
		#print("path :", path)

	path.appendleft(source)

	print("Shortest path from ", source, "to ", dest, "is : ", path)
	#print ("number of iteration for A* is :", iteration)




	

def shortest_path(init, destination):
	global source, dest

	source=init
	dest= destination

	graph=GenerateGraph()
	Astar(graph, source, dest)
	


	# # path = deque()

	# # curr=dest

	# # while curr != source:
	# # 	path.appendleft(curr)
	# # 	curr=predecessor[curr]
	# # 	#print("path :", path)

	# # path.appendleft(source)

	# print("Shortest path from ", source, "to ", dest, "is : ", path)
	# print ("number of iteration for A* is :", iteration)

shortest_path('Arad', 'Bucharest')

