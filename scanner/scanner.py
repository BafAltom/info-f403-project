# coding: utf-8
# Iportation du fichier pour faire plus joli, on hardcode en attendant
#import os

#nomFichier = raw_input("Quel fichier voulez-vous utiliser ? ")
#while not os.path.exists(nomFichier) :
#    print("Ce fichier n'existe pas !")
#    nomFichier = raw_input("Quel fichier voulez-vous utiliser ? ")

# Ouvrir le fichier :
#fichier = open(nomFichier,"r")

def scanner():
	fichier = open("test.perl","r")
	output = list()
	symbolTable = list()

	for ligne in fichier :
		# On retire le caractere de fin de ligne :
		ligne = ligne.replace("\n","")
		# On retire les commentaires de la lignes :
		ligne = ligne.split("#")[0]
		# On ne considere pas les lignes vides :
		if ligne != "" :
			#print ligne 
			operations = ligne.split(' ')
			#print operations 
			# Suppose que tout est separe par des espaces vides dans un premier temps
			#for operation in operations :
			print "ligne : ",ligne
			if operations[0] == "sub":
				output.append("FUNCT-CREATION")
				output.append("FUNCTION-NAME")
				symbolTable.append(operations[1])
				
				if operations[2] == "{":
					output.append("OPEN-BRAC")
				else :
					output.append("OPEN-PAR")
					if operations[3]==")":
						output.append("CLOSE-PAR")
					else :
						value = operations[3].split('$')
						output.append("VARIABLE")
						symbolTable.append(value[1])
						assert(operations[4]==")")
						output.append("CLOSE-PAR")
						assert(operations[5]=="{")
						output.append("OPEN-BRAC")
			elif operations[0] == "}" :
				output.append("CLOSE-BRAC")
			elif operations[0] == "print" :
				output.append("PERL-FUNCT-NAME")
				symbolTable.append(operations[0])
				value = operations[1].split('$')
				output.append("VARIABLE")
				symbolTable.append(value[1])
				assert(operations[2]==";")
				output.append("SEMICOLON")
			elif operations[0][0] == "$" :
				value = operations[0].split('$')
				output.append("VARIABLE")
				symbolTable.append(value[1])
				assert(operations[1]=="=")
				output.append("EQUAL")
				value = operations[2].split("’")
				value2 = operations[3].split("’")
				output.append("STRING")
				symbolTable.append(""+value[1]+" "+value2[0])
				assert(operations[4]==";")
				output.append("SEMICOLON")
			elif operations[0][0] == "&" :
				value = operations[0].split('&')
				output.append("FUNCT-NAME")
				symbolTable.append(value[1])
				assert(operations[1]=="(")
				if operations[1] == "(":
					output.append("OPEN-PAR")
					if operations[2]==")":
						output.append("CLOSE-PAR")
					else :
						value = operations[2].split('$')
						output.append("VARIABLE")
						symbolTable.append(value[1])
						assert(operations[3]==")")
						output.append("CLOSE-PAR")
				output.append("SEMICOLON")
			print "output : ",output
			print "table des symboles : ",symbolTable
			print ""
		
	fichier.close()

if __name__ == '__main__':
	scanner()
