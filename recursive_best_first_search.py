from Romania import GenerateGraph, ApprCost

romania=GenerateGraph()

f_cost = {i:None for i in romania}
dist = {i:None for i in romania}


def RBFS(graph, source, dest, f_limit):
	global f_cost
	print (f_cost[source])
	queue=[]
	cost=ApprCost()
	
	queue.append(source)
	#f[source]=float("inf")

	curr = source

	print("curr: ", curr)

	if curr == dest:
		print(f_limit)
		return curr, dest, f_limit 

	for neighbour in graph[curr]:
		print("neighbour:", neighbour)
		print("f[", neighbour, "] :", f_cost[neighbour])
		if dist[curr] is None:
			print("None came")
			dist[neighbour]=graph[curr][neighbour]
		else:
			if dist[neighbour] is None:
				dist[neighbour]=0
			print("dist[", neighbour, "] was :", dist[neighbour])
			dist[neighbour]=dist[curr]+graph[curr][neighbour]
		print("dist:", neighbour, " :",dist[neighbour])
		reach_cost = dist[neighbour] + cost[neighbour]
		print("reach_cost: ", reach_cost)
		
		if f_cost[neighbour] is None:
			f_cost[neighbour]=reach_cost
		else:
			f_cost[neighbour]=max(reach_cost, f_cost[neighbour])
			print("f_cost[neighbour]=", f_cost[neighbour])

	#print (f)

	
	


	while True:
		f_cost=dict(filter(lambda item: item[1] is not None, f_cost.items()))
		f_cost=dict(sorted(f_cost.items(), key=lambda item: item[1]))
		print(f_cost)
		best=list(f_cost.keys())[0]
		print("best :",best)
		if f_cost[best]>f_limit:
			print ("Failed")
			return False, dest, f_limit

		alternative=list(f_cost.keys())[1]
		print("alternative :" , alternative)

		result, dest, f_cost[best] = RBFS(graph, best, 'Bucharest', min(f_cost[alternative], f_limit) )




def shortest_path(source, dest, f_limit):
	graph=GenerateGraph()
	predecessor, iteration = RBFS(graph, source, dest, f_limit)

	path = deque()

	curr=dest

	while curr != source:
		path.appendleft(curr)
		curr=predecessor[curr]
		#print("path :", path)

	path.appendleft(source)

	print("Shortest path from ", source, "to ", dest, "is : ", path)
	print ("number of iteration for A* is :", iteration)




result, f_limit=RBFS(romania, 'Arad', 'Bucharest', 700)
print(result, f_limit)
