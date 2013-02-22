EPSILON = 'EPSILON'
import cfgrammar

# --------------------------
# G1 from slide 115 of the syllabus

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

terminals = set(['$', 'begin', 'end', 'Id', ':=', 'read', 'write', '(', ')', ',', 'Nb', '+', '-', ';', EPSILON])
g1 = cfgrammar.CFGrammar(terminals, rules)

#-----------------------------------------------------------------------------------
# G2 : from TP6

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
terminals = set(['$', '-', 'ID', '(', ')', EPSILON])

g2 = cfgrammar.CFGrammar(terminals, rules)

# ------------------------------------------------------------------------
# G3 : from slide 130
rules = [
	['S', 'E', '$'],
	['E', 'T', 'E2'],
	['E2', '+', 'T', 'E2'],
	['E2', EPSILON],
	['T', 'F', 'T2'],
	['T2', '*', 'F', 'T2'],
	['T2', EPSILON],
	['F', '(', 'E', ')'],
	['F', 'id'],
]
terminals = set(['$', '+', '*', 'id', '(', ')', EPSILON])

g3 = cfgrammar.CFGrammar(terminals, rules)
