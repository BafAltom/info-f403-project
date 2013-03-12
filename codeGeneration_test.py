from scanner import token
import codeGeneration


def test_1():
	
	code_generator = codeGeneration.ASMcodeGenerator()
	tokenList = []
	tokenList.append(token.token("COND"))
	tokenList.append(token.token("open-cond"))
	tokenList.append(token.token("INT", "2"))
	tokenList.append(token.token("GT"))
	tokenList.append(token.token("INT", "3"))
	tokenList.append(token.token("add-cond"))
	tokenList.append(token.token("INT", "4"))
	tokenList.append(token.token("EQUIV"))
	tokenList.append(token.token("INT", "5"))
	tokenList.append(token.token("close-cond"))
	tokenList.append(token.token("END-SYMBOL"))
	code = code_generator.generate_code(tokenList)
	
	print ""
	print "code ASM :\n"
	print code



test_1()
