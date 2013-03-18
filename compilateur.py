import codeGeneration
import scanner
import parser
import syntaxtreeabstracter
import sys
import getopt
import re

def compilePerl(verbose, perlFile):

	from grammars_examples import g6

	perl_scanner = scanner.PerlScanner()
	inputTokens = perl_scanner.scans(perlFile)
	if verbose:
		print "-------------------------------------------------------------------------------------------------"
		print " token list :\n"
		print "-------------------------------------------------------------------------------------------------"
		for token in inputTokens:
			print token
		print ""

	ll1_parser = parser.LL1Parser(g6, verbose=False)
	ll1_parser.parse(inputTokens)
	parseTree = ll1_parser.parseTree

	sta = syntaxtreeabstracter.SyntaxTreeAbstracter(parseTree)
	sta.abstract()

	code_generator = codeGeneration.ASMcodeGenerator(sta.ast)
	code = code_generator.generate_code()

	if verbose:
		print "-------------------------------------------------------------------------------------------------"
		print " parse tree :\n"
		print "-------------------------------------------------------------------------------------------------"
		print parseTree
		print "-------------------------------------------------------------------------------------------------"
		print " abstract syntax tree :\n"
		print "-------------------------------------------------------------------------------------------------"
		print sta.ast
		print "-------------------------------------------------------------------------------------------------"
		print "ASM code :\n"
		print "-------------------------------------------------------------------------------------------------"
		print code
	return code





try:
	opts, args = getopt.getopt(sys.argv[1:], "i:v", ["help", "input="])
except getopt.GetoptError as err:
	print(err)
	sys.exit(2)

perlFile = None
asmFile = None
verbose = False
for o, a in opts:
	if o == "-v":
		verbose = True
	elif o in ("-i", "--input"):
		perlFile = a
	else:
		print("Option {} unknow".format(o))
		sys.exit(2)

asmFile = re.search("[/].*\.pl", perlFile)
if not asmFile:
	asmFile = re.search(".*\.pl", perlFile)
	asmFile = asmFile.group()[:-2] + "S"
else:
	asmFile = asmFile.group()[1:-2] + "S"


code = compilePerl(verbose, perlFile)

outputFile = open(asmFile, "w")
outputFile.write(code)
outputFile.close()

print "The ASM code has been created in the file " + str(asmFile)
