import token
import re

class PerlScanner:
	def __init__(self, verbose=False):
		self.verbose = verbose

	def scans(self, pathFile):
		try:
			Perlfile = open(pathFile, "r")
			tokenList = list()
			line = ""
			for line2 in Perlfile:
				line = line + line2

			while line != "":
				tok, line = self.getNextToken(line)
				if tok.name != "":
					tokenList.append(tok)
					if (self.verbose):
						print tok
			tokenList.append(token.token('END-SYMBOL'))
		except Exception as e:
			raise Exception("Le fichier ne respecte pas la syntaxe PERL", e)
			tokenList = list()
		Perlfile.close()
		return tokenList

	def getNextToken(slef, line):
		line = line.lstrip()

		while re.match("\n", line):
			line = line[2:]
			print "ligne vide"

		if line == "":
			return token.token("", ""), line
		else:
			# On cherche d'abord les operateurs "non string"
			if line[0] == "-":
				line = line[1:]
				return token.token("MINUS", ""), line
			if line[0] == "+":
				line = line[1:]
				return token.token("ADD", ""), line
			if line[0] == ">":
				if len(line) > 2 and line[1] == "=":
					line = line[2:]
					return token.token("GE", ""), line
				else:
					line = line[1:]
					return token.token("GT", ""), line
			if line[0] == "<":
				if len(line) > 2 and line[1] == "=":
					line = line[2:]
					return token.token("LE", ""), line
				else:
					line = line[1:]
					return token.token("LT", ""), line
			if line[0] == "/":
				line = line[1:]
				return token.token("DIV", ""), line
			if line[0] == "*":
				line = line[1:]
				return token.token("MUL", ""), line
			if line[0] == "}":
				line = line[1:]
				return token.token("CLOSE-BRAC", ""), line
			if line[0] == "{":
				line = line[1:]
				return token.token("OPEN-BRAC", ""), line
			if line[0] == ")":
				line = line[1:]
				return token.token("CLOSE-PAR", ""), line
			if line[0] == "(":
				line = line[1:]
				return token.token("OPEN-PAR", ""), line
			if line[0] == ",":
				line = line[1:]
				return token.token("COMA", ""), line
			if line[0] == ";":
				line = line[1:]
				return token.token("SEMICOLON", ""), line
			if line[0] == ".":
				line = line[1:]
				return token.token("DOT", ""), line
			if line[0] == "=":
				if len(line) > 2 and line[1] == "=":
					line = line[2:]
					return token.token("EQUIV", ""), line
				else:
					line = line[1:]
					return token.token("EQUAL", ""), line
			if line[0] == "!":
				if len(line) > 2 and line[1] == "=":
					line = line[2:]
					return token.token("DIF", ""), line
				else:
					line = line[1:]
					return token.token("FAC", ""), line
			if re.match("\|\|", line):
				line = line[2:]
				return token.token("OR", ""), line
			if re.match("\&\&", line):
				line = line[2:]
				return token.token("AND", ""), line
			if re.match("''", line):
				line = line[2:]
				return token.token("BOOL", "false"), line

			# On cherche ensuite les operateurs "strings"
			if line[0] == "n":
				if re.match("not[^a-zA-Z0-9_-]", line):
					line = line[3:]
					return token.token("NOT", ""), line
				elif re.match("ne[^a-zA-Z0-9__-]", line):
					line = line[2:]
					return token.token("NE-S", ""), line
			if re.match("true[^a-zA-Z0-9_-]", line):
				line = line[4:]
				return token.token("BOOL", "true"), line
			if re.match("false[^a-zA-Z0-9_-]", line):
				line = line[5:]
				return token.token("BOOL", "false"), line
			if line[0] == "l":
				if re.match("lt[^a-zA-Z0-9__-]", line):
					line = line[2:]
					return token.token("LT-S", ""), line
				if re.match("le[^a-zA-Z0-9__-]", line):
					line = line[2:]
					return token.token("LE-S", ""), line
				if re.match("length[^a-zA-Z0-9_-]", line):
					line = line[6:]
					return token.token("PERL-LENG", ""), line
			if line[0] == "g":
				if re.match("gt[^a-zA-Z0-9__-]", line):
					line = line[2:]
					return token.token("GT-S", ""), line
				if re.match("ge[^a-zA-Z0-9__-]", line):
					line = line[2:]
					return token.token("GE-S", ""), line
			if line[0] == "i":
				if re.match("if[^a-zA-Z0-9_-]", line):
					line = line[2:]
					return token.token("OPEN-COND", ""), line
				if re.match("int[^a-zA-Z0-9_-]", line):
					line = line[3:]
					return token.token("PERL-INT", ""), line
			if line[0] == "e":
				if re.match("eq[^a-zA-Z0-9__-]", line):
					line = line[2:]
					return token.token("EQ-S", ""), line
				if re.match("elsif[^a-zA-Z0-9_-]", line):
					line = line[5:]
					return token.token("ADD-COND", ""), line
				if re.match("else[^a-zA-Z0-9_-]", line):
					line = line[4:]
					return token.token("CLOSE-COND", ""), line
			if re.match("defined[^a-zA-Z0-9_-]", line):
				line = line[7:]
				return token.token("PERL-DEF", ""), line
			if re.match("unless[^a-zA-Z0-9_-]", line):
				line = line[6:]
				return token.token("NEG-COND", ""), line
			if re.match("print[^a-zA-Z0-9_-]", line):
				line = line[5:]
				return token.token("PERL-PRIN", ""), line
			if re.match("return[^a-zA-Z0-9_-]", line):
				line = line[6:]
				return token.token("RET", ""), line
			if line[0] == "s":
				if re.match("sub[^a-zA-Z0-9_-]", line):
					line = line[3:]
					return token.token("FUNCT-DEF", ""), line
				if re.match("substr[^a-zA-Z0-9_-]", line):
					line = line[6:]
					return token.token("PERL-SUBS", ""), line
				if re.match("scalar[^a-zA-Z0-9_-]", line):
					line = line[6:]
					return token.token("PERL-SCAL", ""), line

			# On cherche ensuite les nombres (float et int)
			if re.match("[0-9]", line):
				floatNumber = re.match("([0-9])+\.([0-9])+", line)
				intNumber = re.match("([0-9])+", line)  # On sait deja qu il n y a pas de point apres puisqu on teste les float d abord
				if floatNumber:
					# On a un float
					line = line[len(floatNumber.group()):]
					return token.token("FLOAT", floatNumber.group()), line
				if intNumber:
					# on a un entier
					line = line[len(intNumber.group()):]
					return token.token("INT", intNumber.group()), line

			# On cherche ensuite les variables, fonctions et strings (tout ce qui necessite une boucle)
			if line[0] == "&":
				func = re.match("&([A-Za-z])+([A-Za-z0-9_-])*", line)
				if func:
					# On a un appel de fonction (& suivi d'un string)
					line = line[len(func.group()):]
					return token.token("FUNCT-NAME", func.group()[1:]), line

			if line[0] == "'":
				string = re.match("'([^'])*'", line)
				if string:
					# On a un string (' suivi d'un string et termine par un autre ')
					line = line[len(string.group()):]
					return token.token("STRING", string.group()[1:-1]), line

			if line[0] == "#":
				com = re.match("#(.)*\n", line)
				if com:
					# On a un commentaire (# suivi d'un string et termine par un autre \n)
					line = line[len(com.group()):]
					return token.token("", ""), line

			if line[0] == "$":
				var = re.match("[$]([A-Za-z])+([A-Za-z0-9_-])*", line)
				if var:
					# On a une variable ($ suivi d'un string)
					line = line[len(var.group()):]
					return token.token("VARIABLE", var.group()[1:]), line
			# tout ce qui reste est alors une variable
			if re.match("([A-Za-z])", line):
				var = re.match("([A-Za-z])+([A-Za-z0-9_-])*", line)
				if var:
					# On a un ID (un string)
					line = line[len(var.group()):]
					return token.token("ID", var.group()), line
			# Si on arrive ici c est qu il y a un probleme avec la syntaxe du fichier
			return None



if __name__ == '__main__':
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

	perl_scanner = PerlScanner()
	inputTokens = perl_scanner.scans(perlFile)
	for token in inputTokens:
		print token

