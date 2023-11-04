#Defining the graph as an adjacency list in python dictionary
graph = {"A": ["B", "C", "D"],
	"B": ["E"],
	"C": ["F", "G"],
	"D": ["H"],
	"E": ["I"],
	"F": ["J"]}


def BFS_non_recursive(graph, source, path = [], queue = []):
	#if source not in path:
		#path.append(source)
	if source not in graph:
		return path
	if source not in queue:
		queue.append(source)
		
		while queue:
			m=queue.pop(0)
			if m not in path:
				path.append(m)
			if m not in graph:
				return path

			for neighbour in graph[m]:
				if neighbour not in path:
					path.append(neighbour)
				if neighbour not in queue:
					queue.append(neighbour)


	return (path)

print(BFS_non_recursive(graph, "A"))





