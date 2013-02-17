class CFGrammar:
	@staticmethod
	def findSymbols(rules):
		symbols = []
		for r in rules:
			for s in r:
				if s not in symbols:
					symbols.append(s)
		return symbols

	def __init__(self, terminals, rules):
		self.symbols = CFGrammar.findSymbols(rules)
		self.terminals = terminals
		for t in terminals:
			assert t in self.symbols, "Provided terminal " + str(t) + " was not found in symbols"

		# self.rules : list of lists of symbols, with the first one being the left part of the rule
		# e.g. A -> B C D will be ['A', 'B', 'C', 'D']
		self.rules = rules

	def first_1(self, emptySymbol='EPSILON'):  # returns a dict matching each symbol to their 'first'
		first = {}
		for A in self.symbols:
			if A in self.terminals:
				first[A] = [A]
			else:
				first[A] = []
		stable = False
		cnt = 0
		while not stable:
			cnt += 1
			#print(cnt)
			stable = True
			for A in self.symbols:
				#print "\tSymbol : ", A
				for rule in filter(lambda x: x[0] == A, self.rules):
					#print "\t\tRule : ", rule
					found_epsilon = True
					current_symbol = 0
					while found_epsilon and current_symbol + 1 < len(rule):
						found_epsilon = False
						current_symbol += 1
						for candidate in first[rule[current_symbol]]:
							#print "\t\t\tCandidate : ", candidate
							if candidate == emptySymbol:
								found_epsilon = True
							if candidate not in first[A]:
								stable = False
								first[A].append(candidate)
		#print "first took " + str(cnt) + " turns"
		return first

	def follow_1(self, emptySymbol='EPSILON'):
		# TODO : handle epsilon case
		follow = {}
		first = self.first_1(emptySymbol)
		for A in self.symbols:
			follow[A] = []
		stable = False
		cnt = 0
		while (not stable):
			cnt += 1
			#print (cnt)
			stable = True
			for rule in self.rules:
				#print "\tRule : ", rule
				for i, A in enumerate(rule):
					if (i == 0):
						continue
					else:
						#print "\t\t", i, A
						foundEpsilon = True
						epsilonOffset = 0
						while foundEpsilon:
							foundEpsilon = False
							epsilonOffset += 1
							if i + epsilonOffset >= len(rule):
								#print "\t\t\tCandidates : follow of ", rule[0]
								candidates = follow[rule[0]]
							else:
								#print "\t\t\tCandidates : first of ", rule[i + epsilonOffset]
								candidates = first[rule[i + epsilonOffset]]
							for candidate in candidates:
								#print "\t\t\t\tCandidate : ", candidate
								if candidate == emptySymbol:
									foundEpsilon = True
								elif candidate not in follow[A]:
									stable = False
									follow[A].append(candidate)
									#print "\t\t\t\tadded"
		#print "follow took", cnt, "turns"
		return follow

EPSILON = 'EPSILON'

if __name__ == '__main__':
	rules = [
	['S', 'program', '$'],
	['program', 'begin', 'st-list', 'end'],
	['st-list', 'st', 'st-tail'],
	['st-tail', 'st', 'st-tail'],
	['st-tail', EPSILON],
	['st', 'Id', ':=', 'expression', ';'],
	['st', 'read', '(', 'id-list', ')', ';'],
	['st', 'write', '(', 'expr-list', ')', ';'],
	['id-list', 'Id', 'id-tail'],
	['id-tail', ',', 'Id', 'id-tail'],
	['id-tail', EPSILON],
	['expr-list', 'expression', 'expr-tail'],
	['expr-tail', ',', 'expression', 'expr-tail'],
	['expr-tail', EPSILON],
	['expression', 'prim', 'prim-tail'],
	['prim-tail', 'add-op', 'prim', 'prim-tail'],
	['prim-tail', EPSILON],
	['prim', '(', 'expression', ')'],
	['prim', 'Id'],
	['prim', 'Nb'],
	['add-op', '+'],
	['add-op', '-']
	]
	terminals = ['$', 'begin', 'end', 'Id', ':=', 'read', 'write', '(', ')', ',', 'Nb', '+', '-', ';', EPSILON]
	g = CFGrammar(terminals, rules)

	g.first_1()
	g.follow_1()
	"""
	for a, b in g.first_1().items():
		print a, b
	"""

	"""
	for a, b in g.follow_1().items():
		print a, b
	"""

