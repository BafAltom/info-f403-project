import parser
import token
import scanner

def test_1():
	from grammars_examples import g1
	ll1_parser = parser.LL1Parser(g1)

	inputTokens = []
	inputTokens.append(token.token("begin"))
	inputTokens.append(token.token("Id", "a"))
	inputTokens.append(token.token(":="))
	inputTokens.append(token.token("Id", "b"))
	inputTokens.append(token.token("+"))
	inputTokens.append(token.token("Nb", "4"))
	inputTokens.append(token.token(";"))
	inputTokens.append(token.token("write"))
	inputTokens.append(token.token("("))
	inputTokens.append(token.token("Id", "a"))
	inputTokens.append(token.token("+"))
	inputTokens.append(token.token("("))
	inputTokens.append(token.token("Nb", "2"))
	inputTokens.append(token.token("-"))
	inputTokens.append(token.token("Id", "a"))
	inputTokens.append(token.token(")"))
	inputTokens.append(token.token(")"))
	inputTokens.append(token.token(";"))
	inputTokens.append(token.token("end"))
	inputTokens.append(token.token("$"))

	out = ll1_parser.parse(inputTokens)
	assert out[-1] == 'A'

	# unknown symbol (*)
	inputTokens = []
	inputTokens.append(token.token("begin"))
	inputTokens.append(token.token("Id"))
	inputTokens.append(token.token(":="))
	inputTokens.append(token.token("Id"))
	inputTokens.append(token.token("*"))  # ##
	inputTokens.append(token.token("Nb"))
	inputTokens.append(token.token(";"))
	inputTokens.append(token.token("write"))
	inputTokens.append(token.token("("))
	inputTokens.append(token.token("Id"))
	inputTokens.append(token.token("+"))
	inputTokens.append(token.token("("))
	inputTokens.append(token.token("Nb"))
	inputTokens.append(token.token("-"))
	inputTokens.append(token.token("Id"))
	inputTokens.append(token.token(")"))
	inputTokens.append(token.token(")"))
	inputTokens.append(token.token(";"))
	inputTokens.append(token.token("end"))
	inputTokens.append(token.token("$"))

	try:
		out = ll1_parser.parse(inputTokens)
	except parser.ParseError as parse_e:
		assert parse_e.errorType == "Unknown symbol", "Got " + repr(parse_e.errorType)
		assert parse_e.symbol == "*", "Got " + repr(parse_e.symbol)

	# mismatched parenthesis
	inputTokens = []
	inputTokens.append(token.token("begin"))
	inputTokens.append(token.token("Id"))
	inputTokens.append(token.token(":="))
	inputTokens.append(token.token("Id"))
	inputTokens.append(token.token("+"))
	inputTokens.append(token.token("Nb"))
	inputTokens.append(token.token(";"))
	inputTokens.append(token.token("write"))
	inputTokens.append(token.token("("))
	inputTokens.append(token.token("Id"))
	inputTokens.append(token.token("+"))
	inputTokens.append(token.token("("))
	inputTokens.append(token.token("Nb"))
	inputTokens.append(token.token("-"))
	inputTokens.append(token.token("Id"))
	inputTokens.append(token.token(")"))
	inputTokens.append(token.token("("))  # ###
	inputTokens.append(token.token(")"))
	inputTokens.append(token.token(";"))
	inputTokens.append(token.token("end"))
	inputTokens.append(token.token("$"))

	try:
		out = ll1_parser.parse(inputTokens)
	except parser.ParseError as parse_e:
		assert parse_e.errorType == "Misplaced symbol", "Got " + repr(parse_e.errorType)
		assert parse_e.symbol == "(", "Got " + repr(parse_e.symbol)

def test_2():
	from grammars_examples import g2
	ll1_parser = parser.LL1Parser(g2)

	inputTokens = []
	inputTokens.append(token.token("ID"))
	inputTokens.append(token.token("-"))
	inputTokens.append(token.token("("))
	inputTokens.append(token.token("ID"))
	inputTokens.append(token.token(")"))
	inputTokens.append(token.token("$"))

	out = ll1_parser.parse(inputTokens)
	assert out[-1] == 'A'

	inputTokens = []
	inputTokens.append(token.token("ID"))
	inputTokens.append(token.token("-"))
	inputTokens.append(token.token("("))
	inputTokens.append(token.token("ID"))
	inputTokens.append(token.token("("))  # ##
	inputTokens.append(token.token(")"))
	inputTokens.append(token.token("$"))

	try:
		out = ll1_parser.parse(inputTokens)
	except parser.ParseError as parse_e:
		assert parse_e.errorType == "Misplaced symbol", "Got " + repr(parse_e.errorType)
		assert parse_e.symbol == ")", "Got " + repr(parse_e.symbol)

def test_3():
	from grammars_examples import g3
	ll1_parser = parser.LL1Parser(g3)

	inputTokens = []
	inputTokens.append(token.token("id", "a"))
	inputTokens.append(token.token("*"))
	inputTokens.append(token.token("("))
	inputTokens.append(token.token("id", "a"))
	inputTokens.append(token.token("+"))
	inputTokens.append(token.token("id", "b"))
	inputTokens.append(token.token(")"))
	inputTokens.append(token.token("$"))
	out = ll1_parser.parse(inputTokens)

	assert out[-1] == 'A'
	out_tree = ll1_parser.parseTree
	assert (out_tree.value.name == 'S')
	assert (out_tree.children[0].value.name == 'E')
	assert (out_tree.children[0].children[0].children[0].children[0].value.value == 'a')

def test_4():
	from grammars_examples import g6

	ll1_parser = parser.LL1Parser(g6, verbose=False)
	perl_scanner = scanner.PerlScanner()
	inputTokens = perl_scanner.scans("inputTests/test5.pl")
	ll1_parser.parse(inputTokens)
	print ll1_parser.parseTree

test_1()
test_2()
test_3()
test_4()
