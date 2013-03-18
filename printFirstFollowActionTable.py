from grammars_examples import g6

print "first"
firstString = ""
first = g6.first_1()
for a, b in first.items():
	if a not in g6.terminals:
		firstString += str(a) + " , "
		for termin in b:
			firstString += str(termin) + ", "
		firstString += "\n"
print firstString

print "follow"
followString = ""
follow = g6.follow_1()
for a, b in follow.items():
	if a not in g6.terminals:
		followString += str(a) + " : "
		for termin in b:
			followString += str(termin) + ", "
		followString += "\n"
print followString

print "actionTable"
aT = g6.actionTable()
symbols = g6.symbols
terminals = g6.terminals
aTString = " , "
for t in terminals:
	aTString += str(t) + ",	"
aTString += "\n"
for a in symbols:
	if a not in g6.terminals:
		aTString += str(a) + ": "
		for b in terminals:
			if b in aT[a]:
				aTString += str(aT[a][b])
			aTString += ", "
		aTString += " \n"
print aTString
