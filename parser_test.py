import parser

def test_1():
	from grammars_examples import g1
	ll1_parser = parser.LL1Parser(g1)

	inputString = ["begin", "Id", ":=", "Id", "+", "Nb", ";", "write", "(", "Id", "+", "(", "Nb", "-", "Id", ")", ")", ";", "end", "$"]

	out = ll1_parser.parse(inputString)
	assert out[-1] == 'A'

#                                              v unknown symbol
	inputString = ["begin", "Id", ":=", "Id", "*", "Nb", ";", "write", "(", "Id", "+", "(", "Nb", "-", "Id", ")", ")", ";", "end", "$"]

	out = ll1_parser.parse(inputString)
	assert out[-1] == 'E'

	inputString = ["begin", "Id", ":=", "Id", "+", "Nb", ";", "write", "(", "Id", "+", "(", "Nb", "-", "Id", ")", ";", "end", "$"]

	out = ll1_parser.parse(inputString)
	assert out[-1] == 'E'

def test_2():
	from grammars_examples import g2
	ll1_parser = parser.LL1Parser(g2)

	inputString = ['ID', '-', '(', 'ID', ')', '$']
	out = ll1_parser.parse(inputString)
	assert out[-1] == 'A'

	inputString = ['ID', '-', '(', 'ID', '(', ')', '$']
	out = ll1_parser.parse(inputString)
	assert out[-1] == 'E'

def test_3():
	from grammars_examples import g3
	ll1_parser = parser.LL1Parser(g3)

	inputString = ['id', '*', '(', 'id', '+', 'id', ')', '$']
	out = ll1_parser.parse(inputString)
	assert out[-1] == 'A'

test_1()
test_2()
test_3()
