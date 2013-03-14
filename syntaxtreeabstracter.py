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

		thereWasAFctList = False
		# for loop : because the input tree can contain 1 or 0 "funct-list"
		for fctListInputNode in self.currentInputNode.findToken("FUNCT-LIST", maxDepth=2):
			thereWasAFctList = True
			fctListAbstractNode = parser.parseTreeNode(token.token("Funct-List"))
			for fctNode in fctListInputNode.findToken("FUNCT"):
				fctListAbstractNode.giveNodeChild(self.abstractFct(fctNode))
			self.currentAbstractNode.giveNodeChild(fctListAbstractNode)

		depthIntrList = 3 if thereWasAFctList else 2

		for instrListRoot in self.currentInputNode.findToken("INSTRUCT-LIST", maxDepth=depthIntrList):
			print "adding one instruction"
			self.currentAbstractNode.giveNodeChild(self.abstractInstrList(instrListRoot))

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
		abstractFctNode.giveNodeChild(self.abstractInstrList(instrRoot))

		return abstractFctNode

	def abstractInstrList(self, inputInstrListNode):
		abstractInstrListNode = parser.parseTreeNode(token.token("Instr-List"))
		nextInstrNode = inputInstrListNode
		while (nextInstrNode is not None):
			newNode, nextInstrNode = self.abstractInstr(nextInstrNode)
			abstractInstrListNode.giveNodeChild(newNode)
		return abstractInstrListNode

	def abstractInstr(self, inputInstrListNode):
		assert inputInstrListNode.value.name == "INSTRUCT-LIST"
		abstractInstrNode = parser.parseTreeNode(token.token("Instr", value="END"))  # will be deleted if a real instruction is found
		nextInstruction = None  # ditto
		for inputInstrNode in inputInstrListNode.findToken("INSTRUCT", maxDepth=1):
			instrTypeNode = inputInstrNode.children[0]
			instrType = instrTypeNode.value.name
			if (instrType == "FUNCT-CALL"):
				abstractInstrNode = self.abstractFctCall(instrTypeNode)
			elif (instrType == "VARIABLE"):
				abstractInstrNode = self.abstractAssign(inputInstrNode)
			elif (instrType == "COND"):
				abstractInstrNode = self.abstractCond(inputInstrNode)
			elif (instrType == "RET"):
				abstractInstrNode = self.abstractReturn(inputInstrNode)
			else:
				raise Exception("Instruction of unknown type : " + str(instrType))
			for nextInstrNode in inputInstrListNode.findToken("INSTRUCT-LIST", maxDepth=1):
				nextInstruction = nextInstrNode
		return abstractInstrNode, nextInstruction

	def abstractFctCall(self, fctCallNode):
		#assert instrNode.value.name == "INSTRUCT", "Problem with INSTRUCT Node (Wrong name) :\n" + str(instrNode)
		#fctCallNode = instrNode.children[0]
		# un funct-call peut venir d'un simple-exp, donc vire cette partie
		assert fctCallNode.value.name == "FUNCT-CALL"
		assert len(fctCallNode.children) == 4
		nameNode = fctCallNode.children[0]
		name = nameNode.value.name
		if (name == "FUNCT-NAME"):  # user-defined fct
			name = nameNode.value.value
		abstractFctCallNode = parser.parseTreeNode(token.token("Fct-Call", value=name))
		# children are the arguments
		for argRoot in fctCallNode.findToken("FUNCT-CALL-ARG", maxDepth=2):
			for firstArgNode in argRoot.findToken("FUNCT-CALL-ARG-BEG"):
				expNode = firstArgNode.children[0]
				assert expNode.value.name == "EXP"
				abstractFctCallNode.giveNodeChild(self.abstractExp(expNode))
			for nextArgNode in filter(lambda x: len(x.children) > 0, argRoot.findToken("FUNCT-CALL-ARG-END")):
				expNode = nextArgNode.children[1]
				assert expNode.value.name == "EXP"
				abstractFctCallNode.giveNodeChild(self.abstractExp(expNode))
		return abstractFctCallNode

	def abstractReturn(self, instrNode):
		assert instrNode.value.name == "INSTRUCT"
		assert instrNode.children[0].value.name == "RET"
		expNode = instrNode.children[1]
		assert expNode.value.name == "EXP", "2nd children is not EXP : " + str(instrNode)
		abstractReturnNode = parser.parseTreeNode(token.token("return"))
		abstractReturnNode.giveNodeChild(self.abstractExp(expNode))
		return abstractReturnNode

	def abstractCond(self, condNode):
		if condNode.value.name == "INSTRUCT":
			condNode = condNode.children[0]
			assert condNode.value.name == "COND"
		else:
			assert condNode.value.name == "COND-END"

		abstractCondNode = parser.parseTreeNode(token.token("Cond"))
		assert len(condNode.children) > 3

		if not condNode.children[0].value.name == "CLOSE-COND":  # this cond is a final 'end'
			try:
				ifNode = condNode.findToken("EXP", maxDepth=1).next()
			except StopIteration:
				raise Exception("Symbol 'EXP' was not found in COND Node : \n" + str(condNode))
			abstractCondNode.giveNodeChild(self.abstractExp(ifNode))

		try:
			thenNode = condNode.findToken("INSTRUCT-LIST", maxDepth=1).next()
		except StopIteration:
			raise Exception("Symbol 'INSTRUCT-LIST' was not found in COND Node : \n" + str(condNode))
		abstractCondNode.giveNodeChild(self.abstractInstrList(thenNode))

		if not condNode.children[0].value.name == "CLOSE-COND":  # this cond is a final 'end'
			try:
				elseNode = condNode.findToken("COND-END", maxDepth=1).next()
			except StopIteration:
				raise Exception("Symbol 'COND-END' was not found in COND Node : \n" + str(condNode))
			abstractCondNode.giveNodeChild(self.abstractCond(elseNode))

		return abstractCondNode

	def abstractAssign(self, instrNode):
		assert instrNode.value.name == "INSTRUCT"
		varNode = instrNode.children[0]
		expNode = instrNode.children[2]
		assert varNode.value.name == "VARIABLE"
		assert instrNode.children[1].value.name == "EQUAL"
		assert expNode.value.name == "EXP"
		abstractAssignNode = parser.parseTreeNode(token.token("Assign", value=varNode.value.value))
		abstractAssignNode.giveNodeChild(self.abstractExp(expNode))
		return abstractAssignNode

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
			assert expType in operators, str(expType + " is not in the list of accepted operators : " + str(operators))
			abstractExpNode = parser.parseTreeNode(token.token("OPERATOR", value=expType))
			abstractExpNode.giveNodeChild(nextLevelFct(expNextLNode))
			abstractExpNode.giveNodeChild(nextLevelFct(expTailNextLNode))
			return abstractExpNode
		else:
			raise Exception("Misformed expression node (should have 2 or 0 children) :\n" + str(thisLevelExpNode))

	def abstractExp(self, expNode):
		return self.abstractExpLevel(expNode, "EXP", "EXP-2", self.abstractExp2, ["EQUIV", "GT"])

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
