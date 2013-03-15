class parseTreeNode:
	def __init__(self, value):
		self.value = value
		self.father = None
		self.children = []  # must stay a list as the order is important

	def giveChild(self, value):
		child = parseTreeNode(value)
		self.giveNodeChild(child)

	def giveNodeChild(self, node):
		node.father = self
		self.children.append(node)

	def findToken(self, value, maxDepth=None, allowSelf=False):
		if (maxDepth is None):
			maxDepth = -2
		if(maxDepth == -1):
			return

		if (allowSelf and self.value.name == value):
			yield self
		for child in self.children:
			for found in child.findToken(value, maxDepth=maxDepth-1, allowSelf=True):
				yield found

	def getDepth(self):
		if self.father is None:
			return 0
		return self.father.getDepth() + 1

	def __repr__(self):
		my_repr = "\t" * self.getDepth()
		my_repr += str(self.value) + "\n"
		for child in self.children:
			my_repr += str(child)
		return my_repr

