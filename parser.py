from scanner import token

class parseTreeNode:
	def __init__(self, value):
		self.value = value
		self.father = None
		self.children = []

	def giveChild(self, value):
		child = parseTreeNode(value)
		child.father = self
		self.children.append(child)

	def getDepth(self):
		current_depth = 1
		current_node = self
		while (current_node.father):
			current_node = current_node.father
			current_depth += 1
		return current_depth

	def __repr__(self):
		my_repr = "\t" * self.getDepth()
		my_repr += str(self.value) + "\n"
		for child in self.children:
			my_repr += str(child)
		return my_repr

class LL1Parser:
	def __init__(self, grammar, verbose=False):
		self.grammar = grammar
		self.M = grammar.actionTable()

		self.endSymbol = "__UNDEFINED"

		self.input = None

		self.parseTree = None
		self.currentNode = None

		self.verbose = verbose
		self.error = False
		self.success = False
		self.output = None

	def parse(self, inputText, endSymbol="$"):

		self.input = inputText  # list of symbols
		self.endSymbol = endSymbol
		self.output = []
		self.error = False
		self.success = False

		self.parseTree = parseTreeNode(token.token(self.grammar.startSymbol))
		self.currentNode = self.parseTree

		self.parse_recursiveCall()
		return self.output

	def parse_recursiveCall(self):
		if (self.error):
			return

		if (self.verbose):
			print "-----"
			print "input", self.input
			print "output", self.output
			print "parseTree :\n", self.parseTree
			print "currentNode", self.currentNode.value
			#print "first", self.grammar.first_1()
			#print "follow", self.grammar.follow_1()
			#print "action", self.grammar.actionTable()

		stack_token = self.currentNode.value
		input_token = self.input[0]  # only one character as we have an LL1-parser
		# notation from the syllabus - pp. 116
		X = stack_token.name
		u = input_token.name
		assert X in self.grammar.symbols

		if (self.verbose):
			print "from stack", stack_token
			print "from input", input_token

		if (u in self.M[X]):
			self.produce(self.M[X][u])
		elif (X in self.grammar.terminals and X != self.endSymbol):
			self.match()
		elif (X == u and X == '$'):
			self.trigger_accept()
		else:
			self.trigger_error()

	def trigger_error(self):
		self.output.append("E")

		if (self.verbose):
			print "------ error"
			print "currentNode", self.currentNode.value
			print "input", self.input
			print "output", self.output

		self.error = True

	def trigger_accept(self):
		self.output.append("A")
		self.success = True
		if (self.verbose):
				print "accept"

	def produce(self, i):
		if (self.verbose):
			print "produce", i
		self.output.append("P" + str(i))
		saved_current = self.currentNode
		for produced in self.grammar.rules[i][1:]:
			if (produced != self.grammar.emptySymbol):
				self.currentNode.giveChild(token.token(produced))
				self.currentNode = self.currentNode.children[-1]
				self.parse_recursiveCall()
				self.currentNode = saved_current
		self.currentNode = saved_current

	def match(self):
		if (self.verbose):
			print "match"
		parseTreeToken = self.currentNode.value
		inputToken = self.input.pop(0)
		assert parseTreeToken.name == inputToken.name, "match : input and stack does not match"

		parseTreeToken.value = inputToken.value
		self.output.append("M")
