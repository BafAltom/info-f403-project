from scanner import scanner
from scanner import token
import parser

class SyntaxTreeAbstracter:
	def __init__(self, completeParseTree):
		self.inputTree = completeParseTree
		self.currentInputNode = completeParseTree
		self.ast = parser.parseTreeNode(token.token("AST-ROOT"))
		self.currentAbstractNode = self.ast

	def abstract(self):
		assert self.currentInputNode.value.name == "S"
		assert len(self.currentInputNode.children) == 2

		# for loop : because the input tree can contain 1 or 0 "funct-list"
		for fctListInputNode in self.currentInputNode.findToken("FUNCT-LIST", maxDepth=2):
			fctListAbstractNode = parser.parseTreeNode(token.token("Funct-List"))
			for fctNode in fctListInputNode.findToken("FUNCT"):
				fctListAbstractNode.giveNodeChild(self.abstractFct(fctNode))
			self.currentAbstractNode.giveNodeChild(fctListAbstractNode)

		for instrListRoot in self.currentInputNode.findToken("INSTRUCT-LIST", maxDepth=3):
			self.currentAbstractNode.giveNodeChild(self.abstractInstr(instrListRoot))

	def abstractFct(self, inputFctNode):
		try:
			idNode = inputFctNode.findToken("ID", maxDepth=1).next()
		except StopIteration:
			raise Exception("Symbol 'ID' was not found in function Node : \n" + str(inputFctNode))
		abstractFctNode = parser.parseTreeNode(token.token("Funct", value=idNode.value.value))

		try:
			argRoot = inputFctNode.findToken("ARG-LIST", maxDepth=1).next()
		except StopIteration:
			raise Exception("Symbol 'ARG-LIST' was not found in function Node : \n" + str(inputFctNode))
		for varNode in argRoot.findToken("VARIABLE"):
			abstractFctNode.giveChild(token.token("arg", value=varNode.value.value))

		try:
			instrRoot = inputFctNode.findToken("INSTRUCT-LIST", maxDepth=1).next()
		except StopIteration:
			raise Exception("Symbol 'INSTRUCT-LIST' was not found in function Node : \n" + str(inputFctNode))
		abstractFctNode.giveNodeChild(self.abstractInstr(instrRoot))

		return abstractFctNode

	def abstractInstr(self, inputInstrListNode):
		abstractInstrNode = parser.parseTreeNode(token.token("Instr", value="END"))  # will be deleted if a real instruction is found
		for inputInstrNode in inputInstrListNode.findToken("INSTRUCT", maxDepth=1):
			inputInstrNode = inputInstrListNode.findToken("INSTRUCT").next()
			instrTypeNode = inputInstrNode.children[0]
			instrType = instrTypeNode.value.name
			newNode = None
			absractInstrType = ""
			if (instrType == "FUNCT-CALL"):
				absractInstrType = "Funct-call"
				newNode = self.abstractFctCall(instrTypeNode)
			elif (instrType == "VARIABLE"):
				absractInstrType = "Assign"
				newNode = self.abstractAssign(instrTypeNode)
			elif (instrType == "IF"):
				absractInstrType = "Cond"
				newNode = self.abstractCond(instrTypeNode)
			elif (instrType == "RET"):
				absractInstrType = "Return"
				newNode = self.abstractReturn(inputInstrNode)
			else:
				raise Exception("Instruction of unknown type : " + str(instrType))
			abstractInstrNode = parser.parseTreeNode(token.token("Instr", value=absractInstrType))
			abstractInstrNode.giveNodeChild(newNode)

			for nextInstrNode in inputInstrListNode.findToken("INSTRUCT-LIST", maxDepth=1):
				abstractInstrNode.giveNodeChild(self.abstractInstr(nextInstrNode))

		return abstractInstrNode

	def abstractFctCall(self, fctCallNode):
		return parser.parseTreeNode(token.token("fct-call", value="???"))

	def abstractReturn(self, instrNode):
		assert instrNode.value.name == "INSTRUCT"
		assert instrNode.children[0].value.name == "RET"
		expNode = instrNode.children[1]
		assert expNode.value.name == "EXP", "2nd children is not EXP : " + str(instrNode)
		abstractReturnNode = parser.parseTreeNode(token.token("return"))
		abstractReturnNode.giveNodeChild(self.abstractExp(expNode))
		return abstractReturnNode

	def abstractCond(self, condNode):
		return parser.parseTreeNode(token.token("cond", value="???"))

	def abstractAssign(self, assignNode):
		return parser.parseTreeNode(token.token("assign", value="???"))

	def abstractExpLevel(self, thisLevelExpNode, thisLevelName, nextLevelName, nextLevelFct, operators):  # this method abstract methods abstractExp, abstractExp2 and abstractExp3
		# exp : always has 2 children : exp2 and exp-tail
		expNextLNode = thisLevelExpNode.children[0]
		expTailNode = thisLevelExpNode.children[1]
		assert expNextLNode.value.name == nextLevelName, str(expNextLNode.value.name) + " == " + str(nextLevelName)
		assert expTailNode.value.name == thisLevelName + "-TAIL"
		if len(expTailNode.children) == 0:
			return nextLevelFct(expNextLNode)
		elif len(expTailNode.children) == 2:
			expTailNextLNode = expTailNode.children[1]
			assert expTailNextLNode.value.name == nextLevelName
			expType = expTailNode.children[0].value.name
			assert expType in operators
			abstractExpNode = parser.parseTreeNode(expType)
			abstractExpNode.giveNodeChild(nextLevelFct(expNextLNode))
			abstractExpNode.giveNodeChild(nextLevelFct(expTailNextLNode))
			return abstractExpNode
		else:
			raise Exception("Misformed expression node (should have 2 or 0 children) :\n" + str(thisLevelExpNode))

	def abstractExp(self, expNode):
		return self.abstractExpLevel(expNode, "EXP", "EXP-2", self.abstractExp2, ["EQ", "GT"])

	def abstractExp2(self, exp2Node):
		return self.abstractExpLevel(exp2Node, "EXP-2", "EXP-3", self.abstractExp3, ["ADD", "MINUS"])

	def abstractExp3(self, exp3Node):
		return self.abstractExpLevel(exp3Node, "EXP-3", "SIMPLE-EXP", self.abstractSimpleExp, ["MUL", "DIV"])

	def abstractSimpleExp(self, simpleExpNode):
		simpleExpTypeNode = simpleExpNode.children[0]
		simpleExpType = simpleExpTypeNode.value.name
		if (simpleExpType == "INT" or simpleExpType == "STRING" or simpleExpType == "VARIABLE"):
			return parser.parseTreeNode(token.token(simpleExpType, value=simpleExpTypeNode.value.value))
		elif (simpleExpType == "FUNCT-CALL"):
			return self.abstractFctCall(simpleExpTypeNode)
		elif (simpleExpType == "OPEN-PAR"):
			return self.abstractExp(simpleExpNode.children[1])
		else:
			raise Exception("Unknown Simple Expression Type : " + str(simpleExpType))

if __name__ == '__main__':
	from grammars_examples import g6
	ll1_parser = parser.LL1Parser(g6, verbose=False)

	perl_scanner = scanner.PerlScanner()
	inputTokens = perl_scanner.scans("inputTests/test.pl")
	#print inputTokens
	ll1_parser.parse(inputTokens)
	parseTree = ll1_parser.parseTree
	sta = SyntaxTreeAbstracter(parseTree)
	sta.abstract()
	print sta.ast
