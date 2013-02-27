import token
import re



	
	

def scanner(pathFile):
	Perlfile = open(pathFile,"r")
	tokenList = list()
	
	try:

		for line in Perlfile :
			while line != "" :
				
					# Ca fait des plombes que je cherche a modifier line en la passant par reference, mais ca marche pas, donc je la return, voir avec thomas s il y a
					# un moyen plus propre

				token, line = getNextToken(line)
			
				if token.name != "" :
					tokenList.append(token)
				
		for tok in tokenList :
			print tok.name + "  " + tok.value
	except :
		print("Le fichier ne respecte pas la syntaxe PERL")
	
	
	
		
	Perlfile.close()



def getNextToken(line):
	
	# On retire le caractere de fin de ligne :
	line = line.replace("\n","")
	# On retire les commentaires de la lignes :
	line = line.split("#")[0]
	# On retire les caractere vide au debut de la ligne :
	line = line.lstrip()
	# On ne considere pas les lignes vides :
	if line == "" :
		return token.token("", ""), line
		
	else :
		# On cherche d'abord les operateurs "non string"
		if line[0] == "-" :
			line = line[1:]
			return token.token("MINUS", ""), line
		elif line[0] == "+" :
			line = line[1:]
			return token.token("ADD", ""), line
		elif line[0] == ">" :
			if len(line)> 1 and line[1] == " " :
				line = line[1:]
				return token.token("GT", ""), line
			elif len(line)> 2 and line[1] == "=" :
				line = line[2:]
				return token.token("GE", ""), line
		elif line[0] == "<" :
			if len(line)> 1 and line[1] == " " :
				line = line[1:]
				return token.token("LT", ""), line
			elif len(line)> 2 and line[1] == "=" :
				line = line[2:]
				return token.token("LE", ""), line
		elif line[0] == "/" :
			line = line[1:]
			return token.token("DIV", ""), line
		elif line[0] == "*" :
			line = line[1:]
			return token.token("MULTI", ""), line
		elif line[0] == "}" :
			line = line[1:]
			return token.token("CLOSE-BRAC", ""), line
		elif line[0] == "{" :
			line = line[1:]
			return token.token("OPEN-BRAC", ""), line
		elif line[0] == ")" :
			line = line[1:]
			return token.token("CLOSE-PAR", ""), line
		elif line[0] == "(" :
			line = line[1:]
			return token.token("OPEN-PAR", ""), line
		elif line[0] == "," :
			line = line[1:]
			return token.token("COMA", ""), line
		elif line[0] == ";" :
			line = line[1:]
			return token.token("SEMICOLON", ""), line
		elif line[0] == "." :
			line = line[1:]
			return token.token("DOT", ""), line
		elif line[0] == "=" :
			if len(line)> 1 and line[1] == " " :
				line = line[1:]
				return token.token("EQUAL", ""), line
			elif len(line)> 2 and line[1] == "=" :
				line = line[2:]
				return token.token("EQUIV", ""), line
		elif line[0] == "!" :
			if len(line)> 1 and line[1] == " " :
				line = line[1:]
				return token.token("FAC", ""), line
			elif len(line)> 2 and line[1] == "=" :
				line = line[2:]
				return token.token("DIF", ""), line
		elif len(line)> 2 and line[0:2] == "||" :
			line = line[2:]
			return token.token("OR", ""), line
		elif len(line)> 2 and line[0:2] == "&&" :
			line = line[2:]
			return token.token("AND", ""), line
		elif len(line)> 2 and line[0:2] == "''" : # Dans l'enonce on peut definir un false avec un string vide !!!!!!!!!!!!!!!!!!!!!!!!!
			line = line[2:]
			return token.token("BOOL", "false"), line
			
		# On cherche ensuite les operateurs "strings"
		elif line[0] == "n" :
			if len(line)> 3 and line[1:4] == "ot " :
				line = line[3:]
				return token.token("NOT", ""), line
			elif len(line)> 2 and line[1] == "e" and line[2]==" ":
				line = line[2:]
				return token.token("NE-S", ""), line
		elif len(line)> 4 and line[0:5] == "true ":
			line = line[4:]
			return token.token("BOOL", "true"), line
		elif len(line)> 5 and line[0:6] == "false " :
			line = line[5:]
			return token.token("BOOL", "false"), line
		elif line[0] == "l" :
			if len(line)> 2 and line[1] == "t" and line[2]==" ":
				line = line[2:]
				return token.token("LT-S", ""), line
			elif len(line)> 2 and line[1] == "e" and line[2]==" ":
				line = line[2:]
				return token.token("LE-S", ""), line
			elif len(line)> 6 and line[1:7] == "ength " :
				line = line[6:]
				return token.token("PERL-LENG", ""), line
		elif line[0] == "g" :
			if len(line)> 2 and line[1] == "t" and line[2]==" ":
				line = line[2:]
				return token.token("GT-S", ""), line
			elif len(line)> 2 and line[1] == "e" and line[2]==" ":
				line = line[2:]
				return token.token("GE-S", ""), line
		elif line[0] == "i" :
			if len(line)> 2 and line[1] == "f" and line[2]==" ":
				line = line[2:]
				return token.token("OPEN-COND", ""), line
			elif len(line)> 3 and line[1:4] == "nt " :
				line = line[3:]
				return token.token("PERL-INT", ""), line
		elif line[0] == "e" :
			if len(line)> 2 and line[1] == "q" and line[2]==" ":
				line = line[2:]
				return token.token("EQ-S", ""), line
			elif len(line)> 4 and line[1:5] == "lse " :
				line = line[4:]
				return token.token("CLOSE-COND", ""), line
			elif len(line)> 7 and line[1:8] == "lse if " :
				line = line[7:]
				return token.token("ADD-COND", ""), line
		elif len(line)> 7 and line[0:8] == "defined " :
			line = line[7:]
			return token.token("PERL-DEF", ""), line
		elif len(line)> 6 and line[0:7] == "unless " :
			line = line[6:]
			return token.token("NEG-COND", ""), line
		elif len(line)> 5 and line[0:6] == "print " :
			line = line[5:]
			return token.token("PERL-PRINT", ""), line
		elif len(line)> 6 and line[0:7] == "return " :
			line = line[6:]
			return token.token("RET", ""), line
		elif line[0] == "s" :
			if len(line)> 3 and line[1:4] == "ub ":
				line = line[3:]
				return token.token("FUNCT-DEF", ""), line
			elif len(line)> 6 and line[1:7] == "ubstr " :
				line = line[6:]
				return token.token("PERL-SUBS", ""), line
			elif len(line)> 6 and line[1:7] == "calar " :
				line = line[6:]
				return token.token("PERL-SCAL", ""), line
				
		# On cherche ensuite les nombres (float et int)		
		elif re.match("[0-9]", line) :
			if re.match("([0-9])+\.([0-9])+ ", line) :
				# On a un float
				nmbr = line.split(' ')
				line = line[len(nmbr[0]):]
				return token.token("FLOAT", nmbr[0]), line
			elif re.match("([0-9])+ ", line) :
				# on a un entier
				nmbr = line.split(' ')
				line = line[len(nmbr[0]):]
				return token.token("INT", nmbr[0]), line
		
		# On cherche ensuite les variables, fonctions et strings (tout ce qui necessite une boucle)
		elif line[0] == "&" :
			if re.match("&([A-Za-z])+([A-Za-z0-9_-])* ", line) :
				# On a un appel de fonction (& suivi d'un string)
				nmbr = line.split(' ')
				line = line[len(nmbr[0]):]
				return token.token("FUNCT-CALL", nmbr[0][1:]), line
				
		elif line[0] == "'" :
			if re.match("'(.)*'", line) :
				# On a un string (' suivi d'un string et termine par un autre ')
				nmbr = line.split("'")
				line = line[len(nmbr[1])+2:]
				return token.token("STRING", nmbr[1]), line
				
		elif line[0] == "$" :
			if re.match("[$]([A-Za-z])+([A-Za-z0-9_-])* ", line) :
				# On a une variable ($ suivi d'un string)
				nmbr = line.split(' ')
				line = line[len(nmbr[0]):]
				return token.token("VARIABLE", nmbr[0][1:]), line
		
		
		
		# tout ce qui reste est alors une variable
		elif re.match("([A-Za-z])+([A-Za-z0-9_-])* ", line) :
			# On a un ID (un string)
			nmbr = line.split(' ')
			line = line[len(nmbr[0]):]
			return token.token("ID", nmbr[0]), line
	
		# Si on arrive ici c est qu il y a un probleme avec la syntaxe du fichier
		else :
			print "pas bien"
			return NULL
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	



scanner("test.perl")
