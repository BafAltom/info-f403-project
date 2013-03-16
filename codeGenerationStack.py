from scanner import token
import random

class ASMcodeGenerator:
	def __init__(self, abstractTree):
		self.code = ""  # Contiendra la fonction main
		self.header = ""  # contiendra le header avec les param ASM et les variables qu'on doit definir avant (string, ...)
		self.tree = abstractTree
		self.listRegister = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.listVariable = dict()  # cle = nom de la variable, value = numero du registre ou elle est stockee
		self.listString = dict()  # cle = string, value = lien vers le string (str1, ...)
		self.listStringLen = dict()  # cle = string, value = lien vers la longueur du string (len1, ...)
		reg0 = list()
		reg1 = list()
		reg2 = list()
		reg3 = list()
		reg4 = list()
		reg5 = list()
		reg6 = list()
		reg7 = list()
		reg8 = list()
		reg9 = list()
		reg10 = list()
		reg11 = list()
		self.stack = [reg0,reg1,reg2,reg3,reg4, reg5, reg6, reg7, reg8, reg9, reg10, reg11]
		
		
		self.saveListVariable = list()  # utilise quand doit sauver le contexte lors du passage dans une fonction
		self.saveListRegister = list()  # idem
		self.saveStack = list() # idem

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
			if codeNode.value.name == "Funct-List":
				self.code = self.code + "	.text\n \n"
				self.funct_list(codeNode)
			elif codeNode.value.name == "Instr-List":
				self.code = self.code + "	.global _start\n"
				#self.code = self.code + "	.type main, %function\n\n"
				self.code = self.code + "_start :\n"
				self.instruct_list(codeNode)
			else:
				raise "bug main"

		self.code = self.code + "	/* syscall exit*/ \n"
		self.code = self.code + "	MOV     R0, #0\n"
		self.code = self.code + "	MOV     R7, #1\n"
		self.code = self.code + "	SWI     #0\n"


		print "fin generation du code"

		return self.header + "\n \n" + "\n \n" + self.code

	def funct_list(self, codeNode):
		for child in codeNode.children:
			assert child.value.name == "Funct", "Fonction definie au mauvais endroit"
			self.code = self.code + ".global "+ child.value.value+"\n"
			self.code = self.code + ".type "+ child.value.value+", %function\n"
			self.code = self.code + ""+ child.value.value+":\n"
			self.code = self.code + "	PUSH	{R4-R11,R14}\n"
			self.saveListVariable.append(self.listVariable)
			self.saveListRegister.append(self.listRegister)
			self.saveStack.append(self.stack)
			print "listVariable pre "+ child.value.value
			print self.listVariable
			print "listRegister pre "+ child.value.value
			print self.listRegister
			self.listVariable = dict()
			self.listRegister = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			reg0 = list()
			reg1 = list()
			reg2 = list()
			reg3 = list()
			reg4 = list()
			reg5 = list()
			reg6 = list()
			reg7 = list()
			reg8 = list()
			reg9 = list()
			reg10 = list()
			reg11 = list()
			self.stack = [reg0,reg1,reg2,reg3,reg4, reg5, reg6, reg7, reg8, reg9, reg10, reg11]
			print "listVariable new = "
			print self.listVariable
			print "listRegister new = "
			print self.listRegister
			
			cmpt = 0
			for child2 in child.children:
				if child2.value.name == "arg":
					#print "voir comment gere les arguments"
					if cmpt > 3:
						raise "maximum quatre parametre" # POUR LE MOMENT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
					
					var = self.setRegisterOfVariable(child2.value.value)	
					self.code = self.code + "	MOV 	R"+str(var)+", R"+str(cmpt)+"\n"
					cmpt = cmpt + 1
					
				else: # instructions
					assert child2.value.name == "Instr-List", "instruct-list au mauvais endroit"
					#print "listVariable new 2= "
					#print self.listVariable
					self.instruct_list(child2)
			
			
			
			print "listVariable post "+ child.value.value
			print self.listVariable
			print "listReg post "+ child.value.value
			print self.listRegister
			self.listVariable = self.saveListVariable.pop()
			self.listRegister = self.saveListRegister.pop()
			self.stack = self.saveStack.pop()
			print "listVariable nettoye = "
			print self.listVariable
			print "listregister nettoye = "
			print self.listRegister
			self.code = self.code + "	POP	{R4-R11,R14}\n"
			self.code = self.code + "	BX	LR\n \n"
					
	
	def instruct_list(self, codeNode):
		print "instruct-list"

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
				raise "bug instruct-list"
			self.code = self.code +"\n"
			
	
	def funct_call(self, codeNode):
		print "funct-list ==================================================================> ok"
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
					raise "perl-print ne prend que des strings"
			
		else: # fonctions definies par l utilisateur
			print "funct de l'user"
			cmpt = 0
			for stringNode in codeNode.children:
				if stringNode.value.name == "VARIABLE":
					self.code = self.code + "	MOV 	R"+str(cmpt)+", R"+str(self.getRegisterOfVariable(stringNode.value.value))+"\n"
					cmpt = cmpt +1
				else:
					raise "les fonctions ne prennent que des variables"
			self.code = self.code + "	BL	"+codeNode.value.value+"\n"
		
		
		
		
		
		
	
	def cond(self, codeNode):
		print "cond =============================================================> OK"	
		if codeNode.children[0].value.name == "OPERATOR": # On a une expression
			self.expression(codeNode.children[0])
			self.code = self.code + " else"+str(self.currentCondBlock)+str(self.listOfCond[self.currentCondBlock])+"\n"
			self.cleanRegisters()
					
		if codeNode.children[0].value.name == "Instr-List": # On a un instruc-list
			self.instruct_list(codeNode.children[0])

		elif codeNode.children[1].value.name == "Instr-List": # On a un instruc-list
			self.currentCondBlock = self.currentCondBlock +1
			self.listOfCond.append(0) # Moche faudrait voir ou le mettre, la cree des list plus grande que ce dont on a besoin
			self.instruct_list(codeNode.children[1])
			self.currentCondBlock = self.currentCondBlock -1
		
		if len(codeNode.children) > 2 and codeNode.children[2].value.name == "Cond": # On a un else ou elsif
			self.code = self.code + "	B end"+str(self.currentCondBlock)+"\n"
			self.code = self.code + "else"+str(self.currentCondBlock)+str(self.listOfCond[self.currentCondBlock])+": \n"
			#self.numberOfCond = self.numberOfCond + 1
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
			self.cleanRegisters()
		
		
			
			
		
		
		
		
		
		
		
	
	def assign(self, codeNode):
		print "assign =============================================================> OK"
		##print codeNode
		var = self.setRegisterOfVariable(codeNode.value.value)
		for child in codeNode.children:
			
			if child.value.name == "OPERATOR": # On a une expression
				result = self.expression(child)
				self.code = self.code + "	MOV 	R"+str(var)+", R"+str(result)+"\n"
				# Si on a plus besoin du registre contenant le resultat de l assignation on l efface
				if result not in self.listVariable.values():
					self.cleanRegister(result)
					
			elif child.value.name == "STRING": # On a un string
				# Les string doivent etre declare avant le code, donc ajoute au header
				self.registerString(self, child.value.value)
				#if child.value.value not in self.listString.keys():
				#	self.listString[child.value.value] =  "str" + str(len(self.listString))
				#	self.header = self.header + self.listString[child.value.value]+ ":	.string \""+child.value.value+"\"\n"
				#	self.header = self.header + "len" + str(len(self.listString)-1)+ " = . - "+self.listString[child.value.value]+"\n"

				# On gere ensuite l assignation
				self.code = self.code + "	LDR 	R"+str(var)+", "+self.listString[child.value.value]+"\n"

			elif child.value.name == "INT": # On a un entier
				self.code = self.code + "	MOV 	R"+str(var)+", #"+child.value.value+"\n"
				
			elif child.value.name == "VARIABLE": # On a une variable
				self.code = self.code + "	MOV 	R"+str(var)+", R"+str(self.getRegisterOfVariable(child.value.value))+"\n"
				
			elif child.value.name == "Fct-Call": # On a un appel de fonction
				self.funct_call(child)
				self.code = self.code + "	MOV 	R"+str(var)+", R0\n"
				
			else:
				raise "bug assignation"
				
				

	def retur(self, codeNode):
		print "return ===================================================================> OK"
		
		for child in codeNode.children:
			
			if child.value.name == "OPERATOR": # On a une expression
				result = self.expression(child)
				self.code = self.code + "	MOV 	R0, R"+str(result)+"\n"
				# Si on a plus besoin du registre contenant le resultat de l assignation on l efface
				if result not in self.listVariable.values():
					self.register[result] = 0
					
			elif child.value.name == "STRING": # On a un string
				# Les string doivent etre declare avant le code, donc ajoute au header
				self.registerString(self, child.value.value)
				#if child.value.value not in self.listString.keys():
				#	self.listString[child.value.value] =  "str" + str(len(self.listString))
				#	self.header = self.header + self.listString[child.value.value]+ ":	.string \""+child.value.value+"\"\n"
				#	self.header = self.header + "len" + str(len(self.listString)-1)+ " = . - "+self.listString[child.value.value]+"\n"

				# On gere ensuite l assignation
				self.code = self.code + "	LDR 	R0, "+self.listString[child.value.value]+"\n"

			elif child.value.name == "INT": # On a un entier
				self.code = self.code + "	MOV 	R0, #"+child.value.value+"\n"
				
			elif child.value.name == "VARIABLE": # On a une variable
				self.code = self.code + "	MOV 	R0, R"+str(self.getRegisterOfVariable(child.value.value))+"\n"
				
			elif child.value.name == "Fct-Call": # On a un appel de fonction
				self.funct_call(child)
				# le resltat est deja ans R0

				
			else:
				raise "bug return"
			#self.code = self.code + "	MOV		PC, LR\n"

	
	def expression(self, codeNode):
		print "exp reste a gere  DIV !"
		##print codeNode
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
			raise "La division n est pas autorisee"
		elif codeNode.value.value == "GT":
			op = "BLE"	# On inverse, donc on jump si <=
		elif codeNode.value.value == "EQUIV":
			op = "BNE"	# On inverse, on jump si les deux valeurs sont differentes
	
		# On calcule les deux parametres du calcul
		cmpt =0
		for child in codeNode.children:
			if child.value.name == "VARIABLE":
				print child.value.value
				Reg.append(self.getRegisterOfVariable(child.value.value))
			
			elif child.value.name == "INT":
				print "int"
				if cmpt ==0:
					Reg.append(self.getFreeRegister())
				else:
					Reg.append(self.getFreeRegisterOtherThan(Reg[0]))
				self.code = self.code + "	MOV 	R"+ str(Reg[cmpt])+", #"+str(child.value.value)+"\n"
			
			elif child.value.name == "STRING":
				# Les string doivent etre declare avant le code, donc ajoute au header
				self.registerString(self, child.value.value)
				#if child.value.value not in self.listString.keys():
				#	self.listString[child.value.value] =  "str" + str(len(self.listString))
				#	self.header = self.header + self.listString[child.value.value]+ ":	.string \""+child.value.value+"\"\n"
				#	self.header = self.header + "len" + str(len(self.listString)-1)+ " = . - "+self.listString[child.value.value]+"\n"
				
				
				
				# ensuite on s occupe des calculs
				Reg.append(self.getFreeRegister())
				self.code = self.code + "	LDR 	R"+ str(Reg[cmpt])+", "+self.listString[child.value.value]+"\n"
					
			elif child.value.name == "OPERATOR":
				Reg.append(self.expression(child))
				
			elif child.value.name == "Fct-Call": # On a un appel de fonction
				self.funct_call(child)
				Reg.append(self.getFreeRegister())
				self.code = self.code + "	MOV 	R"+ str(Reg[cmpt])+", R0\n"
			
			cmpt = cmpt+1
		
		if op == "ADD" or op == "SUB" or op == "MUL": # Operateur "standard"
			# On fait le calcul
			if cmpt ==0:
				Reg.append(self.getFreeRegister())
			else:
				Reg.append(self.getFreeRegisterOtherThanS(Reg[0], Reg[1]))
			self.code = self.code + "	" + op + "	R"+str(Reg[2])+ ", R"+str(Reg[0])+ ", R"+str(Reg[1])+"\n"
		else:	# Operateur de comparaison
			self.code = self.code + "	CMP" + "	R"+str(Reg[0])+ ", R"+str(Reg[1])+"\n"
			self.code = self.code + "		" + op
		
		
		# Si les deux registres utilise dans le calculs ne sont pas ceux d une variable on les effaces
		# On regardera pour effacer le troisieme registre du resltat dans la fonction appelante
		if op == "ADD" or op == "SUB" or op == "MUL": # Operateur "standard"
			if Reg[0] not in self.listVariable.values():
				self.cleanRegister(Reg[0])
			if Reg[1] not in self.listVariable.values():
				self.cleanRegister(Reg[1])
			return Reg[2]
		else:
			# Si comparateur, on ne peut les supprimer directement, ou on couperait l instruction du jump en deux
			if Reg[0] not in self.listVariable.values():
				Reg[0]=0
			if Reg[1] not in self.listVariable.values():
				Reg[1]=0
			
	
	
	
	def getFreeRegister(self):
		cmpt = 4
		self.cleanRegisters()
		##print self.register
		for reg in self.listRegister[4:12]:
			if reg == 0:
				self.listRegister[cmpt]=1
				return cmpt
			else:
				cmpt = cmpt+1
		
		# si arrive ici c'est que tous les registres sont utilises
		# On choisit un registre et on le push pour le liberer
		cmpt = random.randint(4,11)
		var = self.getKeyByValue(cmpt)
		if var is not None:
			self.stack[cmpt].append(var)
			self.listVariable[var]=12
			self.code = self.code + "	PUSH	{R"+str(cmpt)+"}\n"
		
		return cmpt
		
	def getFreeRegisterOtherThan(self, num):
		cmpt = 4
		self.cleanRegisters()
		##print self.register
		for reg in self.listRegister[4:12]:
			if reg == 0 and reg != num:
				self.listRegister[cmpt]=1
				return cmpt
			else:
				cmpt = cmpt+1
		
		# si arrive ici c'est que tous les registres sont utilises
		# On choisit un registre et on le push pour le liberer
		cmpt = random.randint(4,11)
		while cmpt == num:
			cmpt = random.randint(4,11)
		
		var = self.getKeyByValue(cmpt)
		print "on a chosit le reg num "+str(cmpt)
		print "on obtient var =" +str(var)
		print self.listRegister
		print "on push dans le stack !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		if var is not None:
			self.stack[cmpt].append(var)
			self.listVariable[var]=12
			self.code = self.code + "	PUSH	{R"+str(cmpt)+"}\n"
		return cmpt
		
	def getFreeRegisterOtherThanS(self, num1, num2):
		cmpt = 4
		self.cleanRegisters()
		##print self.register
		for reg in self.listRegister[4:12]:
			if reg == 0 and reg != num1 and reg != num2:
				self.listRegister[cmpt]=1
				return cmpt
			else:
				cmpt = cmpt+1
		
		# si arrive ici c'est que tous les registres sont utilises
		# On choisit un registre et on le push pour le liberer
		cmpt = random.randint(4,11)
		while cmpt == num1 or cmpt == num2 :
			cmpt = random.randint(4,11)
		
		var = self.getKeyByValue(cmpt)
		print "on a chosit le reg num "+str(cmpt)
		print "on obtient var =" +str(var)
		print self.listRegister
		print "on push dans le stack !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		print self.stack[cmpt]
		print "on ajoute "+str(var)
		if var is not None:
			self.stack[cmpt].append(var)
			print "on obtient"
			print self.stack[cmpt]
			self.listVariable[var]=12
			self.code = self.code + "	PUSH	{R"+str(cmpt)+"}\n"
		return cmpt
		
		# TO DO voir comment gerer si tous les registres sont occupes, doit alors utiliser le stack (c.f. R13)
	
	def getRegisterOfVariable(self, var):
		##print self.listVariable
		reg = self.getRegister(var)
		if reg != 0:
			return self.listVariable[var]
		
		else:
			raise "la variable "+ str(var) +" doit etre assignee avant de pouvoir etre utilisee"
			
			
	def setRegisterOfVariable(self, var): # utilise uniquement, pr assignation
		##print self.listVariable
		reg = self.getRegister(var)
		if reg != 0:
			return self.listVariable[var]
		
		else:
			##print "nouv registre pour " + var
			reg = self.getFreeRegister()
			self.listVariable[var] = reg
			return reg
	
	
	def getRegister(self, var):
		reg = 0
		cmpt = 0
		self.cleanRegisters()
		print "on cherche var "+str(var)
		print self.stack
		# On regarde dans les vecteurs
		if var in self.listVariable.keys():
			reg = self.listVariable[var]
		
		print "result du premier if "+str(reg)
		# On regarde dans le stack
		if reg == 12:
			for regis in self.stack:
				if cmpt >3:
					for re in regis:	
						if re == var:
							print "trouve : reg "+str(cmpt)
							reg = cmpt
							self.popVariable(var, reg)
				if reg == 12:
					cmpt = cmpt + 1
		
		return reg
			
		
	
	def registerString(self, nameString):
		if nameString not in self.listString.keys():
			self.listString[nameString] =  "str" + str(len(self.listString))
			self.listStringLen[nameString] = "len" + str(len(self.listString)-1)
			self.header = self.header + self.listString[nameString]+ ":	.string \""+nameString+"\"\n"
			self.header = self.header + self.listStringLen[nameString]+ " = . - "+self.listString[nameString]+"\n"
	
	
	
	def getKeyByValue(self, regNumber):
		print self.listVariable
		print "on cherche "+str(regNumber)
		for key, value in self.listVariable.items():
			if value == regNumber:
				print "we find "+str(key)
				return key
	
	
	def popVariable(self, var, reg):

		print self.stack
		print "on pop"
		print "reg ="+str(reg)
		find = False
		while not find:
			print "boucle"
			# On pop pour ARM
			oldValue = self.getKeyByValue(reg)
			if oldValue is None:
				newValue = self.cleanRegister(reg)
				if newValue == var:
					find = True
			else:
				dest = self.getFreeRegisterOtherThan(reg)
				print "dest = "+str(dest)
				self.code = self.code + "	MOV		R"+str(dest)+",	R"+str(reg)+"\n"
				self.code = self.code + "	POP		{R"+str(reg)+"}\n"
				
				# On pop pour le codeGenerator
				# la variable deplacee
				
				print "oldValue = "+str(oldValue)
				self.listVariable[oldValue] = dest
				
				# la variable popee
				newValue = self.stack[reg].pop()
				print "newValue = "+str(newValue)
				self.listVariable[newValue] = reg
						

				if newValue == var:
					find = True
			
		print self.stack
				
	def cleanRegister(self, reg):
		if len(self.stack[reg]) > 0:
			self.code = self.code + "	POP		{R"+str(reg)+"}\n"
			newValue = self.stack[reg].pop()
			self.listVariable[newValue] = reg
			return newValue
		else:
			self.listRegister[reg] = 0
			
	def cleanRegisters(self):
		cmpt = 0
		for reg in self.stack:	
			if (self.listRegister[cmpt] == 0) and (len(reg) > 0):
				self.code = self.code + "	POP		{R"+str(cmpt)+"}\n"
				newValue = reg.pop()
				self.listVariable[newValue] = cmpt
			
			cmpt = cmpt +1
	

