import cfgrammar

EPSILON = 'EPSILON'

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
g = cfgrammar.CFGrammar(terminals, rules)
first = g.first_1()
follow = g.follow_1()
"""
for a, b in first.items():
	print a, b
print "----"
for a, b in follow.items():
	print a, b
"""

# TODO : Verify that the code returns exact values (TP 6 slide 11)

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
#print g.first_1()
M = g.actionTable()
for a, b in M.items():
	print a, b
