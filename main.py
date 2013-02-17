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

	def parse(self, inputText, startSymbol='S', endSymbol="$"):
		self.input = inputText  # list of symbols
		self.output = []
		self.error = False
		self.accept = False

		self.stack.append(startSymbol)

		while (not self.error and not self.success):
			print "-----"
			print "stack", self.stack
			print "input", self.input
			print "output", self.output

			x = self.stack[-1]
			u = self.input[0]  # only one character as we have an LL1-parser
			if (x in self.grammar.symbols and u in self.M[x]):
				self.produce(self.M[x][u])
			elif (x in self.grammar.terminals and x != endSymbol):
				self.match()
			elif (x == u and x == '$'):
				self.trigger_accept()
			else:  # Not expected
				self.trigger_error()
		print(self.output)

	def trigger_error(self):
		print "------ error"
		print "stack", self.stack
		print "input", self.input
		print "output", self.output
		self.error = True

	def trigger_accept(self):
		print("accept")
		self.output.append("A")
		self.accept = True

	def produce(self, i):
		print "produce", i
		self.output.append("P" + str(i))
		self.stack.pop()
		for j, produced in enumerate(self.grammar.rules[i]):
			if (j > 0):
				self.stack.append(produced)

	def match(self):
		print "match"
		self.output.append("M")
		self.stack.pop()
		self.input.pop(0)

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

	inputString = ['ID', '-', '(', 'ID', ')', '$']

	comp = LL1Compiler(g)
	comp.parse(inputString)