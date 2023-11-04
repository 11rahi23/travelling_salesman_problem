#Defining the graph as an adjacency list in python dictionary
graph = {"A": ["B", "C", "D"],
	"B": ["E"],
	"C": ["F", "G"],
	"D": ["H"],
	"E": ["I"],
	"F": ["J"]}

def dfs_non_recursive(graph, source, path = [], stack = []):
	if source is None or source not in graph:
		return "Invalid Input"
	if source not in stack:
		stack.append(source)

	while (stack):
		s= stack.pop()
		if s not in path:
			path.append(s)
		if s not in graph:
			continue
		for neighbour in graph[s]:
			stack.append(neighbour)

	return " ".join(path)


DFS_path = dfs_non_recursive(graph, "A")

print(DFS_path)
