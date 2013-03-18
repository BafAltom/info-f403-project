import token

class ASMcodeGenerator:
	def __init__(self, abstractTree):
		self.code = ""  # Contiendra le code
		self.header = ""  # contiendra le header avec les param ASM et les variables qu'on doit definir avant (string, ...)
		self.tree = abstractTree
		self.listRegister = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.listVariable = dict()  # cle = nom de la variable, value = numero du registre ou elle est stockee
		self.listString = dict()  # cle = string, value = lien vers le string (str1, ...)
		self.listStringLen = dict()  # cle = string, value = lien vers la longueur du string (len1, ...)
		self.listFunction = dict()  # cle = nom de la fonction, value = nombre de parametre
		self.saveListVariable = list()  # utilise quand doit sauver le contexte lors du passage dans une fonction
		self.saveListRegister = list()  # idem
		

		# Pour gerer les conditions imbriquees, on utilise ces quatres parametres afin
		# de retenir dans quel condition on est ce qui permet de gerer les branchements
		self.currentCondBlock = 0
		self.maxCondBlock = 0
		self.initCondBlock = 0
		self.listOfCond = list()
		self.listOfCond.append(0)


	def generate_code(self):
		self.header += "	.arch armv5te\n"
		self.header += "	.fpu softvfp\n"
		self.header += "	.eabi_attribute 20 , 1\n"
		self.header += "	.eabi_attribute 21 , 1\n"
		self.header += "	.eabi_attribute 23 , 3\n"
		self.header += "	.eabi_attribute 24 , 1\n"
		self.header += "	.eabi_attribute 25 , 1\n"
		self.header += "	.eabi_attribute 26 , 2\n"
		self.header += "	.eabi_attribute 30 , 6\n"
		self.header += "	.eabi_attribute 18 , 4\n \n"
		self.header += "	.data\n \n"

		for codeNode in self.tree.children:
			if codeNode.value.name == "Funct-List":
				self.code = self.code + "	.text\n \n"
				self.funct_list(codeNode)
			elif codeNode.value.name == "Instr-List":
				self.code = self.code + "	.global _start\n"
				self.code = self.code + "_start :\n"
				self.instruct_list(codeNode)
			else:
				raise Exception("the structure of the code is incorrect")

		self.code = self.code + "	/* syscall exit*/ \n"
		self.code = self.code + "	MOV     R0, #0\n"
		self.code = self.code + "	MOV     R7, #1\n"
		self.code = self.code + "	SWI     #0\n"


		return self.header + "\n \n" + "\n \n" + self.code

	def funct_list(self, codeNode):
		for child in codeNode.children:
			assert child.value.name == "Funct", "Function define at the wrong place"
			self.code = self.code + ".global "+ child.value.value+"\n"
			self.code = self.code + ".type "+ child.value.value+", %function\n"
			self.code = self.code + ""+ child.value.value+":\n"
			self.code = self.code + "	PUSH	{R4-R11,R14}\n"
			self.saveListVariable.append(self.listVariable)
			self.saveListRegister.append(self.listRegister)
			self.listVariable = dict()
			self.listRegister = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			
			cmpt = 0
			for child2 in child.children:
				if child2.value.name == "arg":
					if cmpt > 4:
						raise Exception("a function take at most 4 parameters") 
					
					var = self.setRegisterOfVariable(child2.value.value)	
					self.code = self.code + "	MOV 	R"+str(var)+", R"+str(cmpt)+"\n"
					cmpt = cmpt + 1
					self.listFunction[child.value.value] = cmpt					
				else: # instructions
					assert child2.value.name == "Instr-List", "instruct-list au mauvais endroit"
					self.instruct_list(child2)
			
			self.listVariable = self.saveListVariable.pop()
			self.listRegister = self.saveListRegister.pop()
			self.code = self.code + "	POP	{R4-R11,R14}\n"
			self.code = self.code + "	BX	LR\n \n"
					
	
	def instruct_list(self, codeNode):
		for child in codeNode.children:
			if child.value.name =="Cond":
				self.cond(child)
			elif child.value.name =="Assign":
				self.assign(child)
			elif child.value.name =="return":
				self.retur(child)
			elif child.value.name =="Fct-Call":
				self.funct_call(child)
			elif child.value.name !="Instr" and child.value.value !="END":
				raise Exception("the structure of the instruction list is incorrect")
			self.code = self.code +"\n"
			
	
	def funct_call(self, codeNode):
		if codeNode.value.value == "PERL-PRIN":
			for stringNode in codeNode.children:
				if stringNode.value.name == "STRING":
					self.registerString(stringNode.value.value)
					self.code = self.code + "	/* syscall write	*/ \n"
					self.code = self.code + "	MOV 	R0, #1\n"
					self.code = self.code + "	LDR 	R1, ="+self.listString[stringNode.value.value]+"\n"
					self.code = self.code + "	LDR 	R2, ="+self.listStringLen[stringNode.value.value]+"\n"
					self.code = self.code + "	MOV 	R7, #4\n"
					self.code = self.code + "	SWI 	#0\n"
				else:
					raise Exception("the print function take only strings as parameters")
			
		else: # fonctions definies dans le code
			if codeNode.value.value in self.listFunction.keys():
				cmpt = 0
				for stringNode in codeNode.children:
					if stringNode.value.name == "VARIABLE":
						self.code = self.code + "	MOV 	R"+str(cmpt)+", R"+str(self.getRegisterOfVariable(stringNode.value.value))+"\n"
						cmpt = cmpt +1
					else:
						raise Exception("the functions "+str(codeNode.value.value)+"take only variable as parameters")
				self.code = self.code + "	BL	"+codeNode.value.value+"\n"
				if cmpt != self.listFunction[codeNode.value.value]:
					raise Exception("the functions "+str(codeNode.value.value)+" must have "+str(self.listFunction[codeNode.value.value])+" parameters")
			else:
				raise Exception("the functions "+str(codeNode.value.value)+" must be declared before you can use it")
		
		
	
	def cond(self, codeNode):
		if codeNode.children[0].value.name == "OPERATOR": # On a une expression
			self.expression(codeNode.children[0])
			self.code = self.code + " else"+str(self.currentCondBlock)+str(self.listOfCond[self.currentCondBlock])+"\n"
					
		if codeNode.children[0].value.name == "Instr-List": # On a un instruc-list
			self.currentCondBlock = self.currentCondBlock +1
			self.listOfCond.append(0)
			self.instruct_list(codeNode.children[0])
			self.currentCondBlock = self.currentCondBlock -1

		elif codeNode.children[1].value.name == "Instr-List": # On a un instruc-list		
			self.currentCondBlock = self.currentCondBlock +1
			self.listOfCond.append(0)
			self.instruct_list(codeNode.children[1])
			self.currentCondBlock = self.currentCondBlock -1
		
		if len(codeNode.children) > 2 and codeNode.children[2].value.name == "Cond": # On a un else ou elsif
			self.code = self.code + "	B end"+str(self.currentCondBlock)+"\n"
			self.code = self.code + "else"+str(self.currentCondBlock)+str(self.listOfCond[self.currentCondBlock])+": \n"
			self.listOfCond[self.currentCondBlock] = self.listOfCond[self.currentCondBlock] +1
			self.cond(codeNode.children[2])
		else:
			self.code = self.code + "end"+str(self.currentCondBlock)+":\n"
			if self.currentCondBlock > self.maxCondBlock:
				self.maxCondBlock = self.currentCondBlock
			elif self.currentCondBlock == self.initCondBlock:
				self.maxCondBlock = self.maxCondBlock +1
				self.currentCondBlock = self.maxCondBlock
				self.initCondBlock = self.maxCondBlock
		
			
		
	
	def assign(self, codeNode):
		var = self.setRegisterOfVariable(codeNode.value.value)
		for child in codeNode.children:		
			if child.value.name == "OPERATOR":
				result = self.expression(child)
				self.code = self.code + "	MOV 	R"+str(var)+", R"+str(result)+"\n"
				# Si on a plus besoin du registre contenant le resultat de l assignation on l efface
				if result not in self.listVariable.values():
					self.listRegister[result] = 0					
			elif child.value.name == "STRING":
				# Les string doivent etre declare avant le code, donc ajoute au header
				self.registerString(child.value.value)
				
				# On gere ensuite l assignation
				self.code = self.code + "	LDR 	R"+str(var)+", ="+self.listString[child.value.value]+"\n"
			elif child.value.name == "INT": 
				self.code = self.code + "	MOV 	R"+str(var)+", #"+child.value.value+"\n"				
			elif child.value.name == "VARIABLE": 
				self.code = self.code + "	MOV 	R"+str(var)+", R"+str(self.getRegisterOfVariable(child.value.value))+"\n"				
			elif child.value.name == "Fct-Call":
				self.funct_call(child)
				self.code = self.code + "	MOV 	R"+str(var)+", R0\n"			
			else:
				raise Exception("An error occurs during an assignation of "+str(codeNode.value.value))
				
				

	def retur(self, codeNode):		
		for child in codeNode.children:			
			if child.value.name == "OPERATOR": 
				result = self.expression(child)
				self.code = self.code + "	MOV 	R0, R"+str(result)+"\n"
				# Si on a plus besoin du registre contenant le resultat de l assignation on l efface
				if result not in self.listVariable.values():
					self.listRegister[result] = 0					
			elif child.value.name == "STRING":
				# Les string doivent etre declare avant le code, donc ajoute au header
				self.registerString(child.value.value)
				# On gere ensuite l assignation
				self.code = self.code + "	LDR 	R0, ="+self.listString[child.value.value]+"\n"
			elif child.value.name == "INT": 
				self.code = self.code + "	MOV 	R0, #"+child.value.value+"\n"				
			elif child.value.name == "VARIABLE": 
				self.code = self.code + "	MOV 	R0, R"+str(self.getRegisterOfVariable(child.value.value))+"\n"				
			elif child.value.name == "Fct-Call":
				self.funct_call(child)
				# le resltat est deja ans R0				
			else:
				raise Exception("An error occurs during a return")

	
	def expression(self, codeNode):
		Reg = []
		op =""
		# On regarde quel type d operation on a
		if codeNode.value.value == "ADD":
			op = "ADD"
		elif codeNode.value.value == "MINUS":
			op = "SUB"
		elif codeNode.value.value == "MUL":
			op = "MUL"
		elif codeNode.value.value == "DIV":
			raise Exception("The division is not allowed")
		elif codeNode.value.value == "GT":
			op = "BLE"	# On inverse, donc on saute si <=
		elif codeNode.value.value == "EQUIV":
			op = "BNE"	# On inverse, on saute si les deux valeurs sont differentes
	
		# On calcule les deux parametres du calcul
		cmpt =0
		for child in codeNode.children:
			if child.value.name == "VARIABLE":
				Reg.append(self.getRegisterOfVariable(child.value.value))		
			elif child.value.name == "INT":
				Reg.append(self.getFreeRegister())
				self.code = self.code + "	MOV 	R"+ str(Reg[cmpt])+", #"+str(child.value.value)+"\n"			
			elif child.value.name == "STRING":
				# Les string doivent etre declare avant le code, donc ajoute au header
				self.registerString(child.value.value)								
				# ensuite on s occupe des calculs
				Reg.append(self.getFreeRegister())
				self.code = self.code + "	LDR 	R"+ str(Reg[cmpt])+", ="+self.listString[child.value.value]+"\n"					
			elif child.value.name == "OPERATOR":
				Reg.append(self.expression(child))				
			elif child.value.name == "Fct-Call":
				self.funct_call(child)
				Reg.append(self.getFreeRegister())
				self.code = self.code + "	MOV 	R"+ str(Reg[cmpt])+", R0\n"			
			cmpt = cmpt+1
		
		
		if op == "ADD" or op == "SUB" or op == "MUL": # Operateur "standard"
			Reg.append( self.getFreeRegister())
			self.code = self.code + "	" + op + "	R"+str(Reg[2])+ ", R"+str(Reg[0])+ ", R"+str(Reg[1])+"\n"
		else:	# Operateur de comparaison
			self.code = self.code + "	CMP" + "	R"+str(Reg[0])+ ", R"+str(Reg[1])+"\n"
			self.code = self.code + "		" + op
		
		
		# Si les deux registres utilise dans le calculs ne sont pas ceux d une variable on les effaces
		# On regardera pour effacer le troisieme registre du resltat dans la fonction appelante
		if Reg[0] not in self.listVariable.values():
			self.listRegister[Reg[0]] = 0
		if Reg[1] not in self.listVariable.values():
			self.listRegister[Reg[1]] = 0
			
		if op == "ADD" or op == "SUB" or op == "MUL":
			return Reg[2]
	
	
	def getFreeRegister(self):
		cmpt = 4
		for reg in self.listRegister[4:11]:
			if reg == 0:
				self.listRegister[cmpt]=1
				return cmpt
			else:
				cmpt = cmpt+1
	
	def getRegisterOfVariable(self, var):
		if var in self.listVariable.keys():
			return self.listVariable[var]	
		else:
			raise Exception("the variable " +str(var)+" must be created before you can use it")
			
	def setRegisterOfVariable(self, var): # utilise uniquement, pr assignation
		if var in self.listVariable.keys():
			return self.listVariable[var]	
		else:
			reg = self.getFreeRegister()
			self.listVariable[var] = reg
			return reg
			
	def registerString(self, nameString):
		if nameString not in self.listString.keys():
			self.listString[nameString] =  "str" + str(len(self.listString))
			self.listStringLen[nameString] = "len" + str(len(self.listString)-1)
			self.header = self.header + self.listString[nameString]+ ":	.string \""+nameString+"\"\n"
			self.header = self.header + self.listStringLen[nameString]+ " = . - "+self.listString[nameString]+"\n"
	
	
	
if __name__ == '__main__':
	from grammars_examples import g6
	import scanner
	import parser
	import syntaxtreeabstracter
	import re
	import sys
	import getopt
	
	try:
		opts, args = getopt.getopt(sys.argv[1:], "i:", ["help", "input="])
	except getopt.GetoptError as err:
		print(err) 
		sys.exit(2)
 
	perlFile = None
	for o, a in opts:
		if o in ("-i", "--input"):
			perlFile = a
		else:
			print("Option {} unknow".format(o))
			sys.exit(2)
	
	ll1_parser = parser.LL1Parser(g6, verbose=False)
	perl_scanner = scanner.PerlScanner()
	inputTokens = perl_scanner.scans(perlFile)
	ll1_parser.parse(inputTokens)
	parseTree = ll1_parser.parseTree
	sta = syntaxtreeabstracter.SyntaxTreeAbstracter(parseTree)
	sta.abstract()
	code_generator = ASMcodeGenerator(sta.ast)
	code = code_generator.generate_code()
	print code
