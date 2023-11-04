import numpy

val=[]
missing=[]

numbers = int(input("Enter number of elements: "))

for i in range(0,numbers):
	element = int(input())

	val.append(element)

print (val)

def findMissing(val):
	for i in range(max(val)):
		if i not in val:
			missing.append(i)



findMissing(val)
print (missing)


class Node:
	def __init__(self, data):

		self.value= data
		self.left=None
		self.right=None

	def insert(self, data):

		if data<self.value:
			if self.left is None:
				self.left = Node(data)
			else:
				self.left.insert(data)

		elif data>self.value:
			if self.right is None:
				self.right=Node(data)

			else:
				self.right.insert(data)

		else:
			self.value=data

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.value) ,
		if self.right:
			self.right.PrintTree()



root=Node(val[0])
for i in range(1,len(val)):
	root.insert(i)

root.PrintTree()

