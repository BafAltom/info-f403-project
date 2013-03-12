from scanner import token

class ASMcodeGenerator:
	def __init__(self):
		self.code = ""
		self.tokenList = []
		self.Register = []
	
		
	def generate_code(self, token_list):
		self.tokenList = token_list
		print "liste des tokens :"
		for tok in self.tokenList:
			print tok
		print "generation du code"
		
		self.code = self.code + "	.arch armv5te\n"
		self.code = self.code + "	.fpu softvfp\n"
		self.code = self.code + "	.eabi_attribute 20 , 1\n"
		self.code = self.code + "	.eabi_attribute 21 , 1\n"
		self.code = self.code + "	.eabi_attribute 23 , 3\n"
		self.code = self.code + "	.eabi_attribute 24 , 1\n"
		self.code = self.code + "	.eabi_attribute 25 , 1\n"
		self.code = self.code + "	.eabi_attribute 26 , 2\n"
		self.code = self.code + "	.eabi_attribute 30 , 6\n"
		self.code = self.code + "	.eabi_attribute 18 , 4\n \n"
		
		self.code = self.code + "	.text\n"
		self.code = self.code + "	.global main\n"
		self.code = self.code + "	.type main , % function\n\n"
		self.code = self.code + "main :\n"



		#Doit commencer par programme, c-a-d funct-list ou insttruct-list
		# Pas encore au point donc commence par COND
		

		self.instruct_list()

		self.code = self.code + "\n"
		self.code = self.code + ".end\n"
		
		
		print "liste des tokens fin:"
		for tok in self.tokenList:
			print tok
		print "fin generation du code"
		
		
		return self.code	
	
	def funct_list(self):
		# TO DO
		print "funct-list"
	
	def instruct_list(self):
		# TO DO
		# Doit verifier quel type d instruct
		
		if self.tokenList[0].name =="COND":
			self.tokenList = self.tokenList[1:]
			self.cond()
		elif self.tokenList[0].name =="ASSIGN":
			self.assign()
		elif self.tokenList[0].name =="RETURN":
			self.retur()
		else:
			raise "bug instruct-list"
			
	def assign(self):
		# TO DO
		print "assignation"
		
		
	def retur(self):
		# TO DO
		print "return"
		
		
		
	def cond(self):
		cmpt = 0
		while self.tokenList[0].name =="open-cond" or self.tokenList[0].name =="add-cond":
			self.code = self.code + "	CMP "
			
			self.tokenList = self.tokenList[1:]
			self.exp_cond()
			
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
			
			
			

		
		
	def exp_cond(self):
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
