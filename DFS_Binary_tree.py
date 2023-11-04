#dataset = 100, 12, 92, 112, 123, 2

class Node:
	def __init__(self, value):
		self.left=None
		self.right=None
		self.value=value

	def insert(self, value):
		if value<self.value:
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.insert(value)

		if value>self.value:
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.insert(value)


def DFSpreorder(root):

	if root:
		print (root.value)
	if root.left:
		DFSpreorder(root.left)
	if root.right:
		DFSpreorder(root.right)


def BFS(root):

	queue =[]
	reached =[]

	reached.append(root.value)

	queue.append(root)

	while queue:
		i=queue.pop(0)
		if i.left:
			if i.left not in queue:
				queue.append(i.left)
			if i.left.value not in reached:
				reached.append(i.left.value)
		if i.right:
			if i.right not in queue:
				queue.append(i.right)
			if i.right.value not in reached:
				reached.append(i.right.value)

	print ("BFS", reached)			




t = Node(100)
t.insert(12)
t.insert(92)
t.insert(112)
t.insert(123)
t.insert(2)
t.insert(11)
t.insert(52)
t.insert(3)
t.insert(66)
t.insert(10)

print("DFS:")
DFSpreorder(t)
BFS(t)