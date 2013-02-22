import cfgrammar

EPSILON = 'EPSILON'

def test_1():
	from grammars_examples import g1
	first = g1.first_1()
	follow = g1.follow_1()

	assert 'Nb' in first['expr-list']
	assert 'read' in first['st-tail']
	assert ')' in follow['prim-tail']
	assert 'end' in follow['st-list']

	assert EPSILON not in first['add-op']
	assert ')' not in follow['st']
	# TODO : More verifications

def test_2():
	from grammars_examples import g2
	M = g2.actionTable()

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
	from grammars_examples import g3
	first = g3.first_1()
	follow = g3.follow_1()
	M = g3.actionTable()

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

test_1()
test_2()
test_3()
