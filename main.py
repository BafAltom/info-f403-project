# See :
# - slides 115-124 of the course Syllabus
# - TP6

import cfgrammar

class LL1Compiler:
	def __init__(self, grammar, M):
		self.grammar = grammar
		self.M = M  # dict-matrix where M[symbol1][symbol2] contains the index of an element of self.rules (or None)

		self.stack = []
		self.input = None
		self.output = None
		self.error = False
		self.success = False

	def parse(self, inputText, startSymbol='S', endSymbol="$"):
		self.input = inputText  # list of symbols
		self.output = []
		self.error = False
		self.accept = False

		self.stack.append(startSymbol)

		while (not self.error and not self.success):
			x = self.stack[-1]
			u = self.input[0]  # only one character as we have an LL1-parser
			if (x in self.grammar.symbols and u in self.M[x]):
				self.produce(self.M[x][u])
			elif (x in self.terminals and x != endSymbol):
				self.match()
			elif (x == u and x == '$'):
				self.accept()
			else:  # Not expected
				self.error()
		print(self.output)

	def error(self):
		# TODO : state dump to console
		self.error = True

	def accept(self):
		self.output.append("A")
		self.accept = True

	def produce(self, i):
		self.output.append("P" + str(i))
		self.stack.pop()
		for j, produced in enumerate(self.grammar.rules[i]):
			if (j > 0):
				self.stack.append(produced)

	def match(self):
		self.output.append("M")
		self.stack.pop()
		self.input.pop(0)
