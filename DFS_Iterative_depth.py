graph = {"A": ["B", "C", "D"],
	"B": ["E"],
	"C": ["F", "G"],
	"D": ["H"],
	"E": ["I"],
	"F": ["J"]}


def dfs_non_recursive(graph, source, depth, goal):
	path = []
	stack = []
	level = 0
	if source is None or source not in graph:
		return "Invalid Input"
	if source not in stack:
		stack.append(source)

	for i in range(depth):
		while (stack):
			s= stack.pop()
			if s not in path:
				path.append(s)
				print(path)
			if goal in path:
				return path	
			
			if s not in graph:
				continue
			for neighbour in graph[s]:
				stack.append(neighbour)
			level+=1
			print (level)

			if level>i:
				print("Reached maximum depth and did not find any result")
				break
	 


	#return " ".join(path)


DFS_path = dfs_non_recursive(graph, "A", 5, "J")

print(DFS_path)
