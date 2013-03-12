from scanner import token

class ASMcodeGenerator:
	def __init__(self, abstractTree):
		self.code = "" # Contiendra la fonction main
		self.header = "" # contiendra le header avec les param ASM et les variables qu'on doit definir avant (string, ...)
		self.funct = "" # Contiendra les fonctions
		self.tree = abstractTree
		self.register = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		self.listVariable = dict() # cle = nom de la variable, value = numero du registre ou elle est stockee
		self.listString = dict() # cle = string, value = lien vers le string (str1, ...)
		self.numberOfCond = 0
	
		
	def generate_code(self):
		print "tree :"
		print self.tree
		print "generation du code"
		
		self.header = self.header + "	.arch armv5te\n"
		self.header = self.header + "	.fpu softvfp\n"
		self.header = self.header + "	.eabi_attribute 20 , 1\n"
		self.header = self.header + "	.eabi_attribute 21 , 1\n"
		self.header = self.header + "	.eabi_attribute 23 , 3\n"
		self.header = self.header + "	.eabi_attribute 24 , 1\n"
		self.header = self.header + "	.eabi_attribute 25 , 1\n"
		self.header = self.header + "	.eabi_attribute 26 , 2\n"
		self.header = self.header + "	.eabi_attribute 30 , 6\n"
		self.header = self.header + "	.eabi_attribute 18 , 4\n \n"
		self.header = self.header + "	.text\n \n"
		

		

		#self.instruct_list()
		for codeNode in self.tree.children:
			if codeNode.value.value =="Funct-List":
				self.funct_list(codeNode)
				
			elif codeNode.value.name =="Instr-List":
				self.code = self.code + "	.global main\n"
				self.code = self.code + "	.type main , % function\n\n"
				self.code = self.code + "main :\n"
				self.instruct_list(codeNode)
			else:
				raise "bug main"
		
		

		self.code = self.code + "\n"
		self.code = self.code + "	BX LR\n"
		self.code = self.code + ".end\n"
		
		


		print "fin generation du code"
		
		
		return self.header + "\n \n" + self.funct + "\n \n" + self.code	
	
	def instruct_list(self, codeNode):
		print "instruct-list"

		for child in codeNode.children:
			if child.value.name =="Cond":
				self.cond(child)
			elif child.value.name =="Assign":
				self.assign(child)
			elif child.value.name =="return":
				self.retur(child)
			elif child.value.name !="Instr" and child.value.value !="END":
				raise "bug instruct-list"
			self.code = self.code +"\n"
			
	
	def funct_list(self, codeNode):
		print "funct-list"
	
	def cond(self, codeNode):
		print "cond =============================================================> OK (manque appel de fonction)"	
		if codeNode.children[0].value.name == "OPERATOR": # On a une expression
			self.expression(codeNode.children[0])
			self.code = self.code + " else"+str(self.numberOfCond)+"\n"
					
		if codeNode.children[0].value.name == "Instr-List": # On a un instruc-list
			self.instruct_list(codeNode.children[0])

		elif codeNode.children[1].value.name == "Instr-List": # On a un instruc-list
			self.instruct_list(codeNode.children[1])

		
		if len(codeNode.children) > 2 and codeNode.children[2].value.name == "Cond": # On a un else ou elsif
			self.code = self.code + "	B end\n"
			self.code = self.code + "else"+str(self.numberOfCond)+": "
			self.numberOfCond = self.numberOfCond + 1
			self.cond(codeNode.children[2])
		else:
			self.code = self.code + "end:\n"
		
		
			
			
		
		
		
		
		
		
		
	
	def assign(self, codeNode):
		print "assign =============================================================> OK (manque appel de fonction)"
		##print codeNode
		var = self.setRegisterOfVariable(codeNode.value.value)
		for child in codeNode.children:
			
			if child.value.name == "OPERATOR": # On a une expression
				result = self.expression(child)
				self.code = self.code + "	MOV R"+str(var)+" R"+str(result)+"\n"
				# Si on a plus besoin du registre contenant le resultat de l assignation on l efface
				if result not in self.listVariable.values():
					self.register[result] = 0
					
			elif child.value.name == "STRING": # On a un string
				# Les string doivent etre declare avant le code, donc ajoute au header
				if child.value.value not in self.listString.keys():
					self.listString[child.value.value] =  "str" + str(len(self.listString))
					self.header = self.header + self.listString[child.value.value]+ ":	.string \""+child.value.value+"\"\n"

				# On gere ensuite l assignation
				self.code = self.code + "	MOV R"+str(var)+" "+self.listString[child.value.value]+"\n"

			elif child.value.name == "INT": # On a un entier
				self.code = self.code + "	MOV R"+str(var)+" #"+child.value.value+"\n"
				
			elif child.value.name == "VARIABLE": # On a une variable
				self.code = self.code + "	MOV R"+str(var)+" R"+str(self.getRegisterOfVariable(child.value.value))+"\n"

				
			else:
				raise "bug assignation"
				
				

	def retur(self, codeNode):
		print "return ===================================================================> OK (manque appel de fonction)"
		
		for child in codeNode.children:
			
			if child.value.name == "OPERATOR": # On a une expression
				result = self.expression(child)
				self.code = self.code + "	MOV R0 R"+str(result)+"\n"
				# Si on a plus besoin du registre contenant le resultat de l assignation on l efface
				if result not in self.listVariable.values():
					self.register[result] = 0
					
			elif child.value.name == "STRING": # On a un string
				# Les string doivent etre declare avant le code, donc ajoute au header
				if child.value.value not in self.listString.keys():
					self.listString[child.value.value] =  "str" + str(len(self.listString))
					self.header = self.header + self.listString[child.value.value]+ ":	.string \""+child.value.value+"\"\n"

				# On gere ensuite l assignation
				self.code = self.code + "	MOV R0 "+self.listString[child.value.value]+"\n"

			elif child.value.name == "INT": # On a un entier
				self.code = self.code + "	MOV R0 #"+child.value.value+"\n"
				
			elif child.value.name == "VARIABLE": # On a une variable
				self.code = self.code + "	MOV R0 R"+str(self.getRegisterOfVariable(child.value.value))+"\n"

				
			else:
				raise "bug return"
			

	
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
			op = "???"
		elif codeNode.value.value == "GT":
			op = "BLE"
		elif codeNode.value.value == "EQUIV":
			op = "BEQ"
	
		# On calcule les deux parametres du calcul
		cmpt =0
		for child in codeNode.children:
			if child.value.name == "VARIABLE":
				print child.value.value
				Reg.append(self.getRegisterOfVariable(child.value.value))
			
			elif child.value.name == "INT":
				print "int"
				Reg.append(self.getFreeRegister())
				self.code = self.code + "	MOV R"+ str(Reg[cmpt])+" #"+str(child.value.value)+"\n"
			
			elif child.value.name == "STRING":
				# Les string doivent etre declare avant le code, donc ajoute au header
				if child.value.value not in self.listString.keys():
					self.listString[child.value.value] =  "str" + str(len(self.listString))
					self.header = self.header + self.listString[child.value.value]+ ":	.string \""+child.value.value+"\"\n"
				
				# ensuite on s occupe des calculs
				Reg.append(self.getFreeRegister())
				self.code = self.code + "	MOV R"+ str(Reg[cmpt])+" "+self.listString[child.value.value]+"\n"
					
			elif child.value.name == "OPERATOR":
				Reg.append(self.expression(child))
			
			cmpt = cmpt+1
		
		if op == "ADD" or op == "SUB" or op == "MUL" or op == "???": # Operateur "standard"
			# On fait le calcul
			Reg.append( self.getFreeRegister())
			self.code = self.code + "	" + op + " R"+str(Reg[2])+ " R"+str(Reg[0])+ " R"+str(Reg[1])+"\n"
		else:	# Operateur de comparaison
			self.code = self.code + "	CMP" + " R"+str(Reg[0])+ " R"+str(Reg[1])+"\n"
			self.code = self.code + "	" + op
		
		
		# Si les deux registres utilise dans le calculs ne sont pas ceux d une variable on les effaces
		# On regardera pour effacer le troisieme registre du resltat dans la fonction appelante
		if Reg[0] not in self.listVariable.values():
			self.register[Reg[0]] = 0
		if Reg[1] not in self.listVariable.values():
			self.register[Reg[1]] = 0
			
		if op == "ADD" or op == "SUB" or op == "MUL" or op == "???": # Operateur "standard"
			return Reg[2]
	
	
	
	def getFreeRegister(self):
		cmpt = 4
		##print self.register
		for reg in self.register[4:32]:
			if reg == 0:
				self.register[cmpt]=1
				return cmpt
			else:
				cmpt = cmpt+1
		
		# TO DO voir comment gerer si tous les registres sont occupes, doit alors utiliser le stack (c.f. R13)
	
	def getRegisterOfVariable(self, var):
		##print self.listVariable
		if var in self.listVariable.keys():
			return self.listVariable[var]
		
		else:
			raise "la variable "+ var +" doit etre assignee avant de pouvoir etre utilisee"
			
			
	def setRegisterOfVariable(self, var): # utilise uniquement, pr assignation
		##print self.listVariable
		if var in self.listVariable.keys():
			return self.listVariable[var]
		
		else:
			##print "nouv registre pour " + var
			reg = self.getFreeRegister()
			self.listVariable[var] = reg
			return reg
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def funct_list2(self):
		# TO DO
		print "funct-list"
	
	def instruct_list2(self):
		# TO DO
		# Doit verifier quel type d instruct
		
		if self.tokenList[0].name =="COND":
			self.tokenList = self.tokenList[1:]
			self.cond2()
		elif self.tokenList[0].name =="ASSIGN":
			self.assign2()
		elif self.tokenList[0].name =="RETURN":
			self.retur2()
		else:
			raise "bug instruct-list"
			
	def assign2(self):
		# TO DO
		print "assignation"
		
		
	def retur2(self):
		# TO DO
		print "return"
		
		
		
	def cond2(self):
		cmpt = 0
		while self.tokenList[0].name =="open-cond" or self.tokenList[0].name =="add-cond":
			self.code = self.code + "	CMP "
			
			self.tokenList = self.tokenList[1:]
			self.exp_cond2()
			
			self.code = self.code + " else"+str(cmpt)+"\n"
			
			#self.instruct_list()
			self.code = self.code + "	instructions pr le if ou else if\n"
			
			self.code = self.code + "	B end\n"
			self.code = self.code + "else"+str(cmpt)+": "
			cmpt = cmpt + 1
			
		
		# close-cond	
		self.tokenList = self.tokenList[1:]	
		self.code = self.code + "	instructions pr le else\n"
		self.code = self.code + "end:\n"
			
			
			

		
		
	def exp_cond2(self):
		codeTmp =""
		if self.tokenList[0].name =="VARIABLE":
			print "to do : add var pr cond"
		elif self.tokenList[0].name =="INT":
			self.code = self.code + "#" + self.tokenList[0].value+" "
		elif self.tokenList[0].name =="STRING":
			print "to do : add string pr cond"
		elif self.tokenList[0].name =="EXP":
			print "to do : add exp pr cond"
		else:
			raise "bug exp-cond premier param"
		
		self.tokenList = self.tokenList[1:]
		
		
		if self.tokenList[0].name =="GT":
			codeTmp ="	BLE "
		elif self.tokenList[0].name =="EQUIV":
			codeTmp ="	BEQ "
		else:
			raise "bug exp-cond comparateur"

		self.tokenList = self.tokenList[1:]
		
		if self.tokenList[0].name =="VARIABLE":
			print "to do : add var pr cond"
		elif self.tokenList[0].name =="INT":
			self.code = self.code + "#" + self.tokenList[0].value + "\n"
		elif self.tokenList[0].name =="STRING":
			print "to do : add string pr cond"
		elif self.tokenList[0].name =="EXP":
			print "to do : add exp pr cond"
		else:
			raise "bug exp-cond premier param"
		
		self.tokenList = self.tokenList[1:]
		
		self.code = self.code + codeTmp
