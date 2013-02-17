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
								assert emptySymbol not in candidates
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

	def actionTable(self, emptySymbol='EPSILON'):
		first = self.first_1(emptySymbol)
		follow = self.follow_1(emptySymbol)
		M = {}
		for s in self.symbols:
			M[s] = {}
		print M
		for i, rule in enumerate(self.rules):
			print i, rule
			A = rule[0]
			foundEpsilon = True
			current_symbol = 0
			while foundEpsilon:  # will not loop because follow never contains epsilon
				foundEpsilon = False
				current_symbol += 1
				if current_symbol >= len(rule):
					print "\tcandidates : follow of", A
					candidates = follow[A]
					assert emptySymbol not in candidates
				else:
					print "\tcandidates : first of", rule[current_symbol]
					candidates = first[rule[current_symbol]]
				for candidate in candidates:
					print "\t\tcandidate : ", candidate
					assert candidate not in M[A] or M[A][candidate] == i, "Grammar is not LL1. Conflicts between rules " + str(M[A][candidate]) + " and " + str(i)
					if (candidate == emptySymbol):
						foundEpsilon = True
					else:
						M[A][candidate] = i
		for t in self.terminals:
			M[t][t] = "M"
		return M
