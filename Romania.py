from collections import defaultdict

def GenerateGraph():
	graph = defaultdict(dict)

	edges= [['Arad', 'Sibiu', 140], ['Arad', 'Zerind', 75], ['Arad', 'Timisoara', 118], ['Zerind', 'Arad', 75], ['Zerind', 'Oradea', 71], ['Timisoara', 'Arad', 118], ['Timisoara', 'Lugoj', 111], ['Sibiu', 'Arad', 140], ['Sibiu', 'Oradea', 151], ['Sibiu', 'Fagaras', 99], ['Sibiu', 'Rimnicu Vilcea', 80], ['Oradea', 'Zerind', 71], ['Oradea', 'Sibiu', 151], ['Lugoj', 'Timisoara',111], ['Lugoj', 'Mehadia', 70], ['Fagaras', 'Sibiu', 99], ['Fagaras', 'Bucharest', 211], ['Rimnicu Vilcea', 'Sibiu', 80], ['Rimnicu Vilcea', 'Craiova', 146], ['Rimnicu Vilcea', 'Pitesti', 97], ['Mehadia', 'Lugoj', 70], ['Mehadia', 'Drobeta', 75], ['Drobeta', 'Mehadia', 75], ['Drobeta', 'Craiova', 120], ['Craiova', 'Drobeta', 120], ['Craiova', 'Rimnicu Vilcea', 146], ['Craiova', 'Pitesti', 138], ['Pitesti', 'Rimnicu Vilcea', 97], ['Pitesti', 'Bucharest', 101], ['Pitesti', 'Craiova', 138], ['Bucharest', 'Pitesti', 101], ['Bucharest', 'Fagaras', 211], ['Bucharest', 'Giurgiu', 90], ['Bucharest', 'Urziceni', 85], ['Urziceni','Bucharest', 85], ['Urziceni', 'Hirsova', 98], ['Urziceni', 'Vaslui', 142], ['Hirsova', 'Urziceni', 98], ['Hirsova', 'Eforie', 86], ['Eforie', 'Hirsova', 86], ['Vaslui', 'Urziceni', 142], ['Vaslui', 'Iasi', 92], ['Iasi', 'Vaslui', 92], ['Iasi', 'Neamt', 87], ['Neamt', 'Iasi', 87]]

	for u,v, dist in edges:
		graph[u][v] = dist

	


	return graph 




def ApprCost():

	graph= defaultdict(dict)

	distance = {}

	distance['Arad']=366
	distance['Bucharest']=0
	distance['Craiova']=160
	distance['Drobeta']=242
	distance['Eforie']=161
	distance['Fagaras']=176
	distance['Giurgiu']=77
	distance['Hirsova']=151
	distance['Iasi']=226
	distance['Lugoj']=244
	distance['Mehadia']=241
	distance['Neamt']=234
	distance['Oradea']=380
	distance['Pitesti']=100
	distance['Rimnicu Vilcea']=193
	distance['Sibiu']=253
	distance['Timisoara']=329
	distance['Urziceni']=80
	distance['Vaslui']=199
	distance['Zerind']=374

	return distance

