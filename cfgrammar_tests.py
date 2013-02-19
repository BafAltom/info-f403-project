import cfgrammar

EPSILON = 'EPSILON'

def test_1():
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

	assert 'Nb' in first['expr-list']
	assert 'read' in first['st-tail']
	assert ')' in follow['prim-tail']
	assert 'end' in follow['st-list']

	assert EPSILON not in first['add-op']
	assert ')' not in follow['st']
	# TODO : More verifications

def test_2():
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

	assert M['S']['-'] == 0
	assert M['S']['('] == 0
	assert M['S']['ID'] == 0
	assert ')' not in M['S']
	assert M['expr']['('] == 2
	assert ')' not in M['expr']
	assert M['expr-tail']['$'] == 5
	assert '(' not in M['expr-tail']
	assert M['var']['ID'] == 6
	assert M['var-tail'][')'] == 8

def test_3():
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
	terminals = ['$', '+', '*', 'id', '(', ')', EPSILON]

	g = cfgrammar.CFGrammar(terminals, rules)
	first = g.first_1()
	follow = g.follow_1()
	M = g.actionTable()


	assert 'id' in first['E']
	assert '(' in first['E']
	assert '+' not in first['E']
	assert '$' in follow['E']
	assert ')' in follow['E']
	assert '$' in follow['E2']
	assert ')' in follow['E2']
	assert '$' in follow['T']
	assert ')' in follow['T']
	assert '+' in follow['T']
	assert '*' not in follow['T']
	assert '$' in follow['F']
	assert ')' in follow['F']
	assert '+' in follow['F']
	assert '*' in follow['F']
	assert '(' not in follow['F']

	assert len(M['S']) == 2
	assert M['S']['id'] == 0
	assert M['S']['('] == 0
	assert len(M['E']) == 2
	assert len(M['E2']) == 3
	assert M['E2']['+'] == 2
	assert M['E2'][')'] == 3
	assert M['E2']['$'] == 3
	assert len(M['E2']) == 3
	assert len(M['T']) == 2
	assert len(M['T2']) == 4
	assert M['T2']['+'] == 6
	assert M['T2']['*'] == 5
	assert M['T2'][')'] == 6
	assert M['T2']['$'] == 6
	assert len(M['F']) == 2
	assert M['F']['id'] == 8


#test_1()
#test_2()
test_3()