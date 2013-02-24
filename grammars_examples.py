EPSILON = 'EPSILON'
import cfgrammar

# --------------------------
# G1 from slide 115 of the syllabus

rules = [
	['S', 'program', '$'],
	['program', 'begin', 'st-list', 'end'],
	['st-list', 'st', 'st-tail'],
	['st-tail', 'st', 'st-tail'],
	['st-tail', EPSILON],
	['st', 'Id', ':=', 'expression', ';'],
	['st', 'read', '(', 'id-list', ')', ';'],
	['st', 'write', '(', 'expr-list', ')', ';'],
	['id-list', 'Id', 'id-tail'],
	['id-tail', ',', 'Id', 'id-tail'],
	['id-tail', EPSILON],
	['expr-list', 'expression', 'expr-tail'],
	['expr-tail', ',', 'expression', 'expr-tail'],
	['expr-tail', EPSILON],
	['expression', 'prim', 'prim-tail'],
	['prim-tail', 'add-op', 'prim', 'prim-tail'],
	['prim-tail', EPSILON],
	['prim', '(', 'expression', ')'],
	['prim', 'Id'],
	['prim', 'Nb'],
	['add-op', '+'],
	['add-op', '-']
]

terminals = set(['$', 'begin', 'end', 'Id', ':=', 'read', 'write', '(', ')', ',', 'Nb', '+', '-', ';', EPSILON])
g1 = cfgrammar.CFGrammar(terminals, rules)

#-----------------------------------------------------------------------------------
# G2 : from TP6

rules = [
	['S', 'expr', '$'],
	['expr', '-', 'expr'],
	['expr', '(', 'expr', ')'],
	['expr', 'var', 'expr-tail'],
	['expr-tail', '-', 'expr'],
	['expr-tail', EPSILON],
	['var', 'ID', 'var-tail'],
	['var-tail', '(', 'expr', ')'],
	['var-tail', EPSILON]
]
terminals = set(['$', '-', 'ID', '(', ')', EPSILON])

g2 = cfgrammar.CFGrammar(terminals, rules)

# ------------------------------------------------------------------------
# G3 : from slide 130
rules = [
	['S', 'E', '$'],
	['E', 'T', 'E2'],
	['E2', '+', 'T', 'E2'],
	['E2', EPSILON],
	['T', 'F', 'T2'],
	['T2', '*', 'F', 'T2'],
	['T2', EPSILON],
	['F', '(', 'E', ')'],
	['F', 'id'],
]
terminals = set(['$', '+', '*', 'id', '(', ')', EPSILON])

g3 = cfgrammar.CFGrammar(terminals, rules)

# ---------------------------------------------------------------------------
# G4 : grammaire du projet
rules = [
	['EXPRESSION', 'VARIABLE'],
	['EXPRESSION', 'EXPRESSION', 'OPERATOR', 'EXPRESSION'],
	['EXPRESSION', 'EXPRESSION-COMP'],
	['EXPRESSION-COMP', 'EXPRESSION', 'OPERATOR-COMP', 'EXPRESSION'],
	['ASSIGNATION', 'VARIABLE', 'EQUAL', 'VALUE'],
	['ASSIGNATION', 'VARIABLE', 'EQUAL', 'EXPRESSION'],			
	['CONDITION', 'OPEN-COND', 'EXPRESSION-COND', 'OPEN-BRAC', 'INSTRUCTIONS', 'CLOSE-BRAC', 'CONDITION-END'],
	['CONDITION', 'NEG-COND', 'EXPRESSION-COND', 'OPEN-BRAC', 'INSTRUCTIONS', 'CLOSE-BRAC', 'CONDITION-END'],
	['CONDITION', 'EXPRESSION', 'OPEN-COND', 'EXPRESSION-COND'],
	['CONDITION', 'EXPRESSION', 'NEG-COND', 'EXPRESSION-COND'],
	['CONDITION-END', 'ADD-COND', 'EXPRESSION-COND', 'OPEN-BRAC', 'INSTRUCTIONS', 'CLOSE-BRAC'],
	['CONDITION-END', 'ADD-COND', 'EXPRESSION-COND', 'OPEN-BRAC', 'INSTRUCTIONS', 'CLOSE-BRAC', 'CONDITION-END'],
	['CONDITION-END', 'CLOSE-COND', 'EXPRESSION-COND', 'OPEN-BRAC', 'INSTRUCTIONS', 'CLOSE-BRAC'],
	['CONDITION-END', EPSILON],										
	['INSTRUCTIONS', 'CONDITION', 'SEMICOLON', 'INSTRUCTIONS'],
	['INSTRUCTIONS', 'EXPRESSION', 'SEMICOLON', 'INSTRUCTIONS'],
	['INSTRUCTIONS', 'FUNCT-CALL', 'SEMICOLON', 'INSTRUCTIONS'],
	['INSTRUCTIONS', 'ASSIGNATION', 'SEMICOLON', 'INSTRUCTIONS'],
	['INSTRUCTIONS', 'CONDITION', 'SEMICOLON'],
	['INSTRUCTIONS', 'EXPRESSION', 'SEMICOLON'],
	['INSTRUCTIONS', 'FUNCT-CALL', 'SEMICOLON'],
	['INSTRUCTIONS', 'ASSIGNATION', 'SEMICOLON'],
	['INSTRUCTIONS', EPSILON],					
	['PARAM', 'DOLLAR', 'VARIABLE'],
	['PARAM', 'DOLLAR', 'VARIABLE', 'PARAM-END'],
	['PARAM', EPSILON],
	['PARAM-END', 'COMA', 'DOLLAR', 'VARIABLE'],
	['PARAM-END', 'COMA', 'DOLLAR', 'VARIABLE', 'PARAM-END'],
	['PARAM-END', EPSILON],
	['USER-FUNCT-CALL', 'AND', 'FUNCT-NAME', 'OPEN-PAR', 'CLOSE-PAR', 'SEMICOLON'],
	['USER-FUNCT-CALL', 'AND', 'FUNCT-NAME', 'OPEN-PAR', 'PARAM', 'CLOSE-PAR', 'SEMICOLON'],
	['USER-FUNCT-CALL', 'AND', 'FUNCT-NAME', 'PARAM', 'SEMICOLON'],
	['USER-FUNCT-CALL', 'AND', 'FUNCT-NAME', 'SEMICOLON'],					
	['PERL-FUNCT-CALL', 'defined', 'EXPRESSION'],
	['PERL-FUNCT-CALL', 'int', 'EXPRESSION'],
	['PERL-FUNCT-CALL', 'length', 'EXPRESSION'],
	['PERL-FUNCT-CALL', 'scalar', 'EXPRESSION'],
	['PERL-FUNCT-CALL', 'substr', 'EXPRESSION', 'COMA', 'INT', 'COMA', 'INT'],
	['PERL-FUNCT-CALL', 'scalar', 'EXPRESSION'],
	['PERL-FUNCT-CALL', 'substr', 'EXPRESSION', 'COMA', 'INT'],
	['PERL-FUNCT-CALL', 'print'],					
	['FUNCTION-CALL', 'USER-FUNCT-CALL'],
	['FUNCTION-CALL', 'PERL-FUNCT-CALL'],
	['FUNCTION', 'FUNCT-ID', 'FUNCT-NAME', 'OPEN-BRAC', 'INSTRUCTIONS', 'RETURN', 'SEMICOLON', 'CLOSE-BRAC'],
	['FUNCTION', 'FUNCT-ID', 'FUNCT-NAME', 'OPEN-PAR', 'CLOSE-PAR', 'OPEN-BRAC', 'INSTRUCTIONS', 'RETURN', 'SEMICOLON', 'CLOSE-BRAC'],
	['FUNCTION', 'FUNCT-ID', 'FUNCT-NAME','OPEN-PAR', 'PARAM', 'CLOSE-PAR', 'OPEN-BRAC', 'INSTRUCTIONS', 'RETURN', 'SEMICOLON', 'CLOSE-BRAC'],
	['RETURN', 'RET', 'EXPRESSION'],
	['RETURN', 'RET', 'EXPRESSION-COND'],
	['RETURN', 'RET', 'VARIABLE'],
	['RETURN', EPSILON],					
	['FUNCTION-LIST', 'FUNCTION'],
	['FUNCTION-LIST', 'FUNCTION', 'FUNCTION-LIST'],
	['FUNCTION-LIST', EPSILON],
	['PROGRAM', 'PROGRAM', 'FUNCTION-LIST'],
	['PROGRAM', 'PROGRAM', 'INSTRUCTIONS'],
	['PROGRAM', 'FUNCTION-LIST'],
	['PROGRAM', 'INSTRUCTIONS'],
	['PROGRAM', EPSILON],
	['S','PROGRAM'],
]
terminals = set(['VALUE','VARIABLE','OPERATOR','OPERATOR-COMP','EQUAL','SEMICOLON','COMA','AND','OPEN-PAR','CLOSE-PAR','OPEN-BRAC','CLOSE-BRAC','DOLLAR','OPEN-COND','CLOSE-COND','ADD-COND','NEG-COND','RET','FUNCT-ID','FUNCT-NAME','FUNCT-CALL'])
g4 = cfgrammar.CFGrammar(terminals, rules)
