from scanner import token

class ASMcodeGenerator:
	def __init__(self, abstractTree):
		self.code = ""  # Contiendra la fonction main
		self.header = ""  # contiendra le header avec les param ASM et les variables qu'on doit definir avant (string, ...)
		self.funct = "" # contiendra les fonctions
		self.tree = abstractTree
		self.listRegister = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.listVariable = dict()  # cle = nom de la variable, value = numero du registre ou elle est stockee
		self.listString = dict()  # cle = string, value = lien vers le string (str1, ...)
		self.listStringLen = dict()  # cle = string, value = lien vers la longueur du string (len1, ...)
		self.listTypeVariable = dict() # cle = variable, value = type
		self.listTypeFunct = dict() # cle = funt-name, value = type du retour
		self.currentFunction = ""
		self.saveListVariable = list()  # utilise quand doit sauver le contexte lors du passage dans une fonction
		self.saveListRegister = list()  # idem
		self.saveCurrentFunct = list() 	# idem

		# Pour gerer les conditions imbriquees, on utilise ces quatres parametres afin
		# de retenir dans quel condition on est ce qui permet de gerer les JUMP
		# pour les end
		self.currentCondBlock = 0
		self.maxCondBlock = 0
		self.initCondBlock = 0
		# pour les else
		self.listOfCond = list()
		self.listOfCond.append(0)


	def generate_code(self):
		print "tree :"
		print self.tree
		print "generation du code"

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

		#self.instruct_list()
		for codeNode in self.tree.children:
			if codeNode.value.name == "Instr-List":
				self.code = self.code + "	.global _start\n"
				#self.code = self.code + "	.type main, %function\n\n"
				self.code = self.code + "_start :\n"
				self.instruct_list(codeNode, True)

		
		for codeNode in self.tree.children:
			if codeNode.value.name == "Funct-List":
				self.funct = self.funct + "	.text\n \n"
				self.funct_list(codeNode)
				
				

		self.code = self.code + "	/* syscall exit*/ \n"
		self.code = self.code + "	MOV     R0, #0\n"
		self.code = self.code + "	MOV     R7, #1\n"
		self.code = self.code + "	SWI     #0\n"


		print "fin generation du code"
		print self.listTypeVariable
		print self.listTypeFunct

		return self.header + "\n \n" + self.funct  + "\n \n" + self.code

	def funct_list(self, codeNode):
		for child in codeNode.children:
			assert child.value.name == "Funct", "Fonction definie au mauvais endroit"
			self.funct = self.funct + ".global "+ child.value.value+"\n"
			self.funct = self.funct + ".type "+ child.value.value+", %function\n"
			self.funct = self.funct + ""+ child.value.value+":\n"
			self.funct = self.funct + "	PUSH	{R4-R11,R14}\n"
			self.saveCurrentFunct.append(self.currentFunction)
			self.currentFunction = child.value.value
			self.saveListVariable.append(self.listVariable)
			self.saveListRegister.append(self.listRegister)
			print "listVariable pre "+ child.value.value
			print self.listVariable
			print "listRegister pre "+ child.value.value
			print self.listRegister
			self.listVariable = dict()
			self.listRegister = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			print "listVariable new = "
			print self.listVariable
			print "listRegister new = "
			print self.listRegister
			
			cmpt = 0
			for child2 in child.children:
				if child2.value.name == "arg":
					#print "voir comment gere les arguments"
					if cmpt > 3:
						raise Exception("a function take at most 4 parameters") # POUR LE MOMENT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
					
					var = self.setRegisterOfVariable(child2.value.value)	
					self.funct = self.code + "	MOV 	R"+str(var)+", R"+str(cmpt)+"\n"
					cmpt = cmpt + 1
					
				else: # instructions
					assert child2.value.name == "Instr-List", "instruct-list au mauvais endroit"
					#print "listVariable new 2= "
					#print self.listVariable
					self.instruct_list(child2, False)
			
			
			
			print "listVariable post "+ child.value.value
			print self.listVariable
			print "listReg post "+ child.value.value
			print self.listRegister
			self.listVariable = self.saveListVariable.pop()
			self.listRegister = self.saveListRegister.pop()
			self.currentFunction = self.saveCurrentFunct.pop()
			print "listVariable nettoye = "
			print self.listVariable
			print "listregister nettoye = "
			print self.listRegister
			self.funct = self.funct + "	POP	{R4-R11,R14}\n"
			self.funct = self.funct + "	BX	LR\n \n"
					
	
	def instruct_list(self, codeNode, main):
		print "instruct-list"

		for child in codeNode.children:
			if child.value.name =="Cond":
				self.cond(child, main)
			elif child.value.name =="Assign":
				self.assign(child, main)
			elif child.value.name =="return":
				self.retur(child, main)
			elif child.value.name =="Fct-Call":
				self.funct_call(child, main)
			elif child.value.name !="Instr" and child.value.value !="END":
				raise Exception("the structure of the instruction list is incorrect")
			if main:
				self.code = self.code +"\n"
			else:
				self.funct = self.funct +"\n"
			
	
	def funct_call(self, codeNode, main):
		print "funct-list ==================================================================> ok"
		code = ""
		if codeNode.value.value == "PERL-PRIN":
			for stringNode in codeNode.children:
				if stringNode.value.name == "STRING":
					self.registerString(stringNode.value.value)
					code = code + "	/* syscall write	*/ \n"
					code = code + "	MOV 	R0, #1\n"
					code = code + "	LDR 	R1, ="+self.listString[stringNode.value.value]+"\n"
					code = code + "	LDR 	R2, ="+self.listStringLen[stringNode.value.value]+"\n"
					code = code + "	MOV 	R7, #4\n"
					code = code + "	SWI 	#0\n"
				else:
					raise Exception("the print function take only strings as parameters")
			
		else: # fonctions definies par l utilisateur
			print "funct de l'user"
			cmpt = 0
			for stringNode in codeNode.children:
				if stringNode.value.name == "VARIABLE":
					code = code + "	MOV 	R"+str(cmpt)+", R"+str(self.getRegisterOfVariable(stringNode.value.value))+"\n"
					cmpt = cmpt +1
				else:
					raise Exception("the functions take only variable as parameters")
			code = code + "	BL	"+codeNode.value.value+"\n"
		
		if main:
			self.code = self.code + code
		else:
			self.funct = self.funct + code
		
		
		
		
	
	def cond(self, codeNode, main):
		print "cond =============================================================> OK"
		code = ""
		if codeNode.children[0].value.name == "OPERATOR": # On a une expression
			self.expression(codeNode.children[0], main)
			code = code + " else"+str(self.currentCondBlock)+str(self.listOfCond[self.currentCondBlock])+"\n"
			if main:
				self.code = self.code + code
			else:
				self.funct = self.funct + code
					
		if codeNode.children[0].value.name == "Instr-List": # On a un instruc-list
			self.instruct_list(codeNode.children[0], main)

		elif codeNode.children[1].value.name == "Instr-List": # On a un instruc-list
			self.currentCondBlock = self.currentCondBlock +1
			self.listOfCond.append(0) # Moche faudrait voir ou le mettre, la cree des list plus grande que ce dont on a besoin
			self.instruct_list(codeNode.children[1], main)
			self.currentCondBlock = self.currentCondBlock -1
		
		if len(codeNode.children) > 2 and codeNode.children[2].value.name == "Cond": # On a un else ou elsif
			code = code + "	B end"+str(self.currentCondBlock)+"\n"
			code = code + "else"+str(self.currentCondBlock)+str(self.listOfCond[self.currentCondBlock])+": \n"
			#self.numberOfCond = self.numberOfCond + 1
			self.listOfCond[self.currentCondBlock] = self.listOfCond[self.currentCondBlock] +1
			if main:
				self.code = self.code + code
			else:
				self.funct = self.funct + code
			self.cond(codeNode.children[2], main)
		else:
			code = code + "end"+str(self.currentCondBlock)+":\n"
			if main:
				self.code = self.code + code
			else:
				self.funct = self.funct + code
			if self.currentCondBlock > self.maxCondBlock:
				self.maxCondBlock = self.currentCondBlock
			elif self.currentCondBlock == self.initCondBlock:
				self.maxCondBlock = self.maxCondBlock +1
				self.currentCondBlock = self.maxCondBlock
				self.initCondBlock = self.maxCondBlock
		
		
			
			
		
		
		
		
		
		
		
	
	def assign(self, codeNode, main):
		print "assign =============================================================> OK"
		##print codeNode
		code = ""
		var = self.setRegisterOfVariable(codeNode.value.value)
		for child in codeNode.children:
			
			if child.value.name == "OPERATOR": # On a une expression
				# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				result, typ = self.expression(child, main)
				self.listTypeVariable[codeNode.value.value] = typ
				code = code + "	MOV 	R"+str(var)+", R"+str(result)+"\n"
				# Si on a plus besoin du registre contenant le resultat de l assignation on l efface
				if result not in self.listVariable.values():
					self.listRegister[result] = 0
					
			elif child.value.name == "STRING": # On a un string
				# Les string doivent etre declare avant le code, donc ajoute au header
				self.registerString(child.value.value)
				self.listTypeVariable[codeNode.value.value] = "STRING"

				# On gere ensuite l assignation
				code = code + "	LDR 	R"+str(var)+", "+self.listString[child.value.value]+"\n"

			elif child.value.name == "INT": # On a un entier
				code = code + "	MOV 	R"+str(var)+", #"+child.value.value+"\n"
				self.listTypeVariable[codeNode.value.value] = "INT"
				
			elif child.value.name == "VARIABLE": # On a une variable
				code = code + "	MOV 	R"+str(var)+", R"+str(self.getRegisterOfVariable(child.value.value))+"\n"
				print self.listTypeVariable
				self.listTypeVariable[codeNode.value.value] = self.listTypeVariable[child.value.value]
				
			elif child.value.name == "Fct-Call": # On a un appel de fonction
				self.listTypeVariable[codeNode.value.value] = self.listTypeFunct[child.value.value]
				self.funct_call(child, main)
				code = code + "	MOV 	R"+str(var)+", R0\n"
				
			else:
				raise Exception("An error occurs during an assignation of "+str(codeNode.value.value))
			
			if main:
				self.code = self.code + code
			else:
				self.funct = self.funct + code	
				

	def retur(self, codeNode, main):
		print "return ===================================================================> OK"
		code = ""
		for child in codeNode.children:
			
			if child.value.name == "OPERATOR": # On a une expression
				# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
				result, typ = self.expression(child, main)
				self.listTypeFunct[self.currentFunction] = typ
				code = code + "	MOV 	R0, R"+str(result)+"\n"
				# Si on a plus besoin du registre contenant le resultat de l assignation on l efface
				if result not in self.listVariable.values():
					self.listRegister[result] = 0
					
			elif child.value.name == "STRING": # On a un string
				# Les string doivent etre declare avant le code, donc ajoute au header
				self.registerString(child.value.value)
				self.listTypeFunct[self.currentFunction] = "STRING"
				
				# On gere ensuite l assignation
				code = code + "	LDR 	R0, "+self.listString[child.value.value]+"\n"

			elif child.value.name == "INT": # On a un entier
				code = code + "	MOV 	R0, #"+child.value.value+"\n"
				self.listTypeFunct[self.currentFunction] = "INT"
				
			elif child.value.name == "VARIABLE": # On a une variable
				code = code + "	MOV 	R0, R"+str(self.getRegisterOfVariable(child.value.value))+"\n"
				self.listTypeFunct[self.currentFunction] = self.listTypeVariable[child.value.value]
				
			elif child.value.name == "Fct-Call": # On a un appel de fonction
				self.funct_call(child, main)
				self.listTypeFunct[self.currentFunction] = self.listTypeFunct[child.value.value]
				# le resltat est deja dans R0
			else:
				raise Exception("An error occurs during a return")
			#self.code = self.code + "	MOV		PC, LR\n"
			
			if main:
				self.code = self.code + code
			else:
				self.funct = self.funct + code

	
	def expression(self, codeNode, main):
		print "exp reste a gere  DIV !"
		##print codeNode
		typ = None
		Reg = []
		op =""
		code =""
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
			op = "BLE"	# On inverse, donc on jump si <=
		elif codeNode.value.value == "EQUIV":
			op = "BNE"	# On inverse, on jump si les deux valeurs sont differentes
	
		# On calcule les deux parametres du calcul
		cmpt =0
		for child in codeNode.children:
			if child.value.name == "VARIABLE":
				print child.value.value
				typ = self.listTypeVariable[child.value.value]
				
				Reg.append(self.getRegisterOfVariable(child.value.value))
			
			elif child.value.name == "INT":
				print "int"
				typ = "INT"
				Reg.append(self.getFreeRegister())
				code = code + "	MOV 	R"+ str(Reg[cmpt])+", #"+str(child.value.value)+"\n"
			
			elif child.value.name == "STRING":
				typ = "STRING"
				# Les string doivent etre declare avant le code, donc ajoute au header
				self.registerString(child.value.value)		
				
				# ensuite on s occupe des calculs
				Reg.append(self.getFreeRegister())
				code = code + "	LDR 	R"+ str(Reg[cmpt])+", "+self.listString[child.value.value]+"\n"
					
			elif child.value.name == "OPERATOR":
				regist, typ = self.expression(child, main)
				Reg.append(regist)
				
			elif child.value.name == "Fct-Call": # On a un appel de fonction
				typ = self.listTypeFunct[child.value.value]
				self.funct_call(child, main)
				Reg.append(self.getFreeRegister())
				code = code + "	MOV 	R"+ str(Reg[cmpt])+", R0\n"
			
			cmpt = cmpt+1
		
		if op == "ADD" or op == "SUB" or op == "MUL": # Operateur "standard"
			# On fait le calcul
			Reg.append( self.getFreeRegister())
			code = code + "	" + op + "	R"+str(Reg[2])+ ", R"+str(Reg[0])+ ", R"+str(Reg[1])+"\n"
		else:	# Operateur de comparaison
			code = code + "	CMP" + "	R"+str(Reg[0])+ ", R"+str(Reg[1])+"\n"
			code = code + "		" + op
		
		
		# Si les deux registres utilise dans le calculs ne sont pas ceux d une variable on les effaces
		# On regardera pour effacer le troisieme registre du resltat dans la fonction appelante
		if Reg[0] not in self.listVariable.values():
			self.listRegister[Reg[0]] = 0
		if Reg[1] not in self.listVariable.values():
			self.listRegister[Reg[1]] = 0
			
		if main:
			self.code = self.code + code
		else:
			self.funct = self.funct + code
			
		if op == "ADD" or op == "SUB" or op == "MUL": # Operateur "standard"
			return Reg[2], typ
	
	
	
	def getFreeRegister(self):
		cmpt = 4
		##print self.register
		for reg in self.listRegister[4:11]:
			if reg == 0:
				self.listRegister[cmpt]=1
				return cmpt
			else:
				cmpt = cmpt+1
		
		# TO DO voir comment gerer si tous les registres sont occupes, doit alors utiliser le stack (c.f. R13)
	
	def getRegisterOfVariable(self, var):
		##print self.listVariable
		if var in self.listVariable.keys():
			return self.listVariable[var]
		
		else:
			raise Exception("the variable " +str(var)+" must be created before you can use it")
			
	def setRegisterOfVariable(self, var): # utilise uniquement, pr assignation
		##print self.listVariable
		if var in self.listVariable.keys():
			return self.listVariable[var]
		
		else:
			##print "nouv registre pour " + var
			reg = self.getFreeRegister()
			self.listVariable[var] = reg
			return reg
	
	
	def registerString(self, nameString):
		if nameString not in self.listString.keys():
			self.listString[nameString] =  "str" + str(len(self.listString))
			self.listStringLen[nameString] = "len" + str(len(self.listString)-1)
			self.header = self.header + self.listString[nameString]+ ":	.string \""+nameString+"\"\n"
			self.header = self.header + self.listStringLen[nameString]+ " = . - "+self.listString[nameString]+"\n"
	
	
	
