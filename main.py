# See :
# - slides 115-124 of the course Syllabus
# - TP6

import cfgrammar

class LL1Compiler:
	def __init__(self, grammar):
		self.grammar = grammar
		self.M = grammar.actionTable()

		self.stack = []
		self.input = None
		self.output = None
		self.error = False
		self.success = False

	def parse(self, inputText, endSymbol="$"):
		self.input = inputText  # list of symbols
		self.output = []
		self.error = False
		self.success = False

		self.stack.append(self.grammar.startSymbol)

		while (not self.error and not self.success):
			"""
			print "-----"
			print "stack", self.stack
			print "input", self.input
			print "output", self.output
			"""

			x = self.stack[-1]
			u = self.input[0]  # only one character as we have an LL1-parser
			print "x", x
			print "u", u
			if (x in self.grammar.symbols and u in self.M[x]):
				self.produce(self.M[x][u])
			elif (x in self.grammar.terminals and x != endSymbol):
				self.match()
			elif (x == u and x == '$'):
				self.trigger_accept()
			else:  # Not expected
				self.trigger_error()
		return self.output

	def trigger_error(self):
		self.output.append("E")
		self.error = True
		print "------ error"
		print "stack", self.stack
		print "input", self.input
		print "output", self.output

	def trigger_accept(self):
		self.output.append("A")
		self.success = True
		print("accept")

	def produce(self, i):
		print "produce", i
		self.output.append("P" + str(i))
		self.stack.pop()
		for produced in reversed(self.grammar.rules[i][1:]):
			if (produced != self.grammar.emptySymbol):
				self.stack.append(produced)

	def match(self):
		print "match"
		a = self.stack.pop()
		b = self.input.pop(0)
		assert a == b, "match : input and stack does not match"
		self.output.append("M")

if __name__ == '__main__':
	EPSILON = 'EPSILON'
	rules = [
		['S', 'expr', '$'],
		['expr', '-', 'expr'],
		['expr', '(', 'expr', ')'],
		['expr', 'var', 'expr-tail'],
		['expr-tail', '-', 'expr'],
		['expr-tail', EPSILON],
		['var', 'ID', 'var-tail'],
		['var-tail', '(', 'expr', ')'],
		['var-tail', EPSILON]
	]
	terminals = ['$', '-', 'ID', '(', ')', EPSILON]

	g = cfgrammar.CFGrammar(terminals, rules)

	M = g.actionTable()
	for a, b in M.items():
		print a, b

	comp = LL1Compiler(g)

	inputString = ['ID', '-', '(', 'ID', ')', '$']
	out = comp.parse(inputString)
	assert out[-1] == 'A'

	inputString = ['ID', '-', '(', 'ID', '(', ')', '$']
	out = comp.parse(inputString)
	assert out[-1] == 'E'

