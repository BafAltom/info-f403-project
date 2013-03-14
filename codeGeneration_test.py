from scanner import token
import codeGeneration
from scanner import scanner
import parser
import syntaxtreeabstracter

def test_1():
	
	from grammars_examples import g6
	ll1_parser = parser.LL1Parser(g6, verbose=False)

	perl_scanner = scanner.PerlScanner()
	inputTokens = perl_scanner.scans("inputTests/test.pl")
	#print inputTokens
	ll1_parser.parse(inputTokens)
	parseTree = ll1_parser.parseTree
	sta = syntaxtreeabstracter.SyntaxTreeAbstracter(parseTree)
	sta.abstract()
	
	
	code_generator = codeGeneration.ASMcodeGenerator(sta.ast)
	code = code_generator.generate_code()
	
	print ""
	print "code ASM :\n"
	print code



test_1()
