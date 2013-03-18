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
g1 = cfgrammar.CFGrammar(rules, terminals)

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

g2 = cfgrammar.CFGrammar(rules, terminals)

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

g3 = cfgrammar.CFGrammar(rules, terminals)


# ---------------------------------------------------------------------------
# G5 : grammaire du projet : Grammaire complete
rules = [
	['S', 'PROGRAM'],
	['PROGRAM', 'PROG', 'PROG-TAIL'],
	['PROG', 'FUNCT-LIST'],
	['PROG', 'INSTRUCT'],
	['PROG', 'EPSILON'],
	['PROG-TAIL', 'PROG-END', 'PROG-TAIL'],
	['PROG-TAIL', 'EPSILON'],
	['PROG-END', 'FUNCT-LIST'],
	['PROG-END', 'INSTRUCT'],
	['FUNCT-LIST', 'FUNCT', 'FUNCT-LIST-END'],
	['FUNCT-LIST-END', 'FUNCT-LIST'],
	['FUNCT-LIST-END', 'EPSILON'],
	['FUNCT', 'FUNCT-DEF', 'ID', 'FUNCT-END'],
	['FUNCT-END', 'OPEN-BRAC', 'INSTRUCT', 'RETURN', 'CLOSE-BRAC'],
	['FUNCT-END', 'OPEN-PAR', 'FUNCT-END2'],
	['FUNCT-END2', 'CLOSE-PAR', 'OPEN-BRAC', 'INSTRUCT', 'RETURN', 'CLOSE-BRAC'],
	['FUNCT-END2', 'PARAM', 'CLOSE-PAR', 'OPEN-BRAC', 'INSTRUCT', 'RETURN', 'CLOSE-BRAC'],
	['FUNCT-CALL', 'USER-FUNCT-CALL'],
	['FUNCT-CALL', 'PERL-FUNCT-CALL'],
	['USER-FUNCT-CALL', 'ID', 'USER-FUNCT-CALL-END'],
	['USER-FUNCT-CALL-END', 'OPEN-PAR', 'USER-FUNCT-CALL-END2'],
	['USER-FUNCT-CALL-END', 'PARAM'],
	['USER-FUNCT-CALL-END', 'EPSILON'],
	['USER-FUNCT-CALL-END2', 'CLOSE-PAR'],
	['USER-FUNCT-CALL-END2', 'PARAM CLOSE-PAR'],
	['PERL-FUNCT-CALL', 'PERL-DEF', 'EXP'],
	['PERL-FUNCT-CALL', 'PERL-INT', 'EXP'],
	['PERL-FUNCT-CALL', 'PERL-LENG', 'EXP'],
	['PERL-FUNCT-CALL', 'PERL-SCAL', 'EXP'],
	['PERL-FUNCT-CALL', 'PERL-SUBS', 'PERL-SUBS-END'],
	['PERL-FUNCT-CALL', 'PERL-PRIN', 'LIST'],
	['PERL-SUBS-END', 'EXP', 'COMA', 'INT', 'COMA', 'INT'],
	['PERL-SUBS-END', 'EXP', 'COMA', 'INT'],
	['LIST', 'STRING LIST-END'],
	['LIST-END', 'LIST'],
	['LIST-END', 'EPSILON'],
	['PARAM', 'PARAM2'],
	['PARAM', 'EPSILON'],
	['PARAM2', 'PARAM-END'],
	['PARAM2', 'EPSILON'],
	['PARAM-END', 'COMA', 'VAR', 'PARAM-END2'],
	['PARAM-END', 'EPSILON'],
	['PARAM-END2', 'PARAM-END'],
	['PARAM-END2', 'EPSILON'],
	['RETURN', 'RET', 'RETURN-END'],
	['RETURN', 'EPSILON'],
	['RETURN-END', 'EXP', 'SEMICOLON'],
	['RETURN-END', 'EXP-COND', 'SEMICOLON'],
	['RETURN-END', 'VAR', 'SEMICOLON'],
	['INSTRUCT', 'COND', 'INSTRUCT-END'],
	['INSTRUCT', 'EXP', 'INSTRUCT-END'],
	['INSTRUCT', 'FUNCT-CALL', 'INSTRUCT-END'],
	['INSTRUCT', 'ASSIGNATION', 'INSTRUCT-END'],
	['INSTRUCT-END', 'SEMICOLON', 'INSTRUCT-END2'],
	['INSTRUCT-END2', 'INSTRUCT'],
	['INSTRUCT-END2', 'EPSILON'],
	['ASSIGNATION', 'VAR', 'EQUAL', 'ASSIGNATION-END'],
	['ASSIGNATION-END', 'VALUE'],
	['ASSIGNATION-END', 'EXP'],
	['COND', 'OPEN-COND', 'EXP-COND', 'OPEN-BRAC', 'INSTRUCT', 'CLOSE-BRAC', 'COND-END'],
	['COND', 'NEG-COND', 'EXP-COND', 'OPEN-BRAC', 'INSTRUCT', 'CLOSE-BRAC', 'COND-END'],
	['COND', 'EXP', 'COND-END2'],
	['COND-END2', 'OPEN-COND', 'EXP-COND'],
	['COND-END2', 'NEG-COND', 'EXP-COND'],
	['COND-END', 'ADD-COND', 'EXP-COND', 'OPEN-BRAC', 'INSTRUCT', 'CLOSE-BRAC', 'COND-END3'],
	['COND-END', 'CLOSE-COND', 'OPEN-BRAC', 'INSTRUCT', 'CLOSE-BRAC'],
	['COND-END', 'EPSILON'],
	['COND-END3', 'COND-END'],
	['COND-END3', 'EPSILON'],
	['EXP', 'E', 'EXP-TAIL'],
	['E', 'EXP2', 'EQUAL', 'EXP'],
	['E', 'NOT', 'EXP'],
	['E', 'FAC', 'EXP'],
	['E', 'EXP2'],
	['EXP-TAIL', 'EXP-END', 'EXP-TAIL'],
	['EXP-TAIL', 'EPSILON'],
	['EXP-END', 'LT', 'EXP2'],
	['EXP-END', 'LT-S', 'EXP2'],
	['EXP-END', 'GT', 'EXP2'],
	['EXP-END', 'GT-S', 'EXP2'],
	['EXP-END', 'LE', 'EXP2'],
	['EXP-END', 'LE-S', 'EXP2'],
	['EXP-END', 'GE', 'EXP2'],
	['EXP-END', 'GE-S', 'EXP2'],
	['EXP-END', 'EQUIV', 'EXP2'],
	['EXP-END', 'EQ-S', 'EXP2'],
	['EXP-END', 'NE-S', 'EXP2'],
	['EXP-END', 'DIF', 'EXP2'],
	['EXP-END', 'DOT', 'EXP2'],
	['EXP-END', 'COMA', 'EXP2'],
	['EXP2', 'EXP', 'EXP2-END'],
	['EXP2', 'EXP3'],
	['EXP2-END', 'ADD', 'EXP3'],
	['EXP2-END',  'MINUS', 'EXP3'],
	['EXP2-END',  'OR', 'EXP3'],
	['EXP3', 'EXP', 'EXP3-END'],
	['EXP3', 'VAR'],
	['EXP3-END', 'MUL', 'VAR'],
	['EXP3-END', 'DIV', 'VAR'],
	['EXP3-END', 'AND', 'VAR'],
	['VALUE', 'INT'],
	['VALUE', 'FLOAT'],
	['VALUE', 'BOOL'],
	['VALUE', 'STRING'],
	['VAR', 'VALUE'],
	['VAR', 'VARIABLE'],
	['VAR', 'MINUS', 'VAR'],
	['VAR', 'ADD', 'VAR'],
	['VAR', 'OPEN-PAR', 'EXP', 'CLOSE-PAR'],
]
terminals = set(['INT', 'FLOAT', 'BOOL', 'STRING', 'FAC', 'MUL', 'DIV', 'MINUS', 'ADD', 'LT', 'GT', 'LE', 'GE', 'EQUIV', 'DIF', 'AND', 'OR', 'NOT', 'LT-S', 'GT-S', 'LE-S', 'GE-S', 'EQ-S', 'NE-S', 'EQUAL', 'DOT', 'SEMICOLON', 'COMA', 'OPEN-PAR', 'CLOSE-PAR', 'OPEN-BRAC', 'CLOSE-BRAC', 'OPEN-COND', 'CLOSE-COND', 'ADD-COND', 'NEG-COND', 'RET', 'FUNCT-DEF', 'ID', 'FUNCT-CALL', 'PERL-DEF', 'PERL-INT', 'PERL-LENG', 'PERL-SCAL', 'PERL-SUBS', 'PERL-PRIN', 'VARIABLE', EPSILON])
g5 = cfgrammar.CFGrammar(rules, terminals)





# ---------------------------------------------------------------------------
# G6 : grammaire du projet : Grammaire simplifiee

rules = [
	['S', 'PROGRAM', 'END-SYMBOL'],
	['PROGRAM', 'FUNCT-LIST', 'PROG-TAIL'],
	['PROGRAM', 'INSTRUCT-LIST'],
	['PROG-TAIL', 'INSTRUCT-LIST'],
	['FUNCT-LIST', 'FUNCT-LIST-BEG', 'FUNCT-LIST-END'],
	['FUNCT-LIST-BEG', 'FUNCT'],
	['FUNCT-LIST-END', 'FUNCT', 'FUNCT-LIST-END'],
	['FUNCT-LIST-END', EPSILON],
	['FUNCT', 'FUNCT-DEF', 'ID', 'ARG-LIST', 'OPEN-BRAC', 'INSTRUCT-LIST', 'CLOSE-BRAC'],
	['ARG-LIST', 'OPEN-PAR', 'ARG-LIST-BEG', 'ARG-LIST-END', 'CLOSE-PAR'],
	['ARG-LIST-BEG', 'VARIABLE'],
	['ARG-LIST-BEG', EPSILON],
	['ARG-LIST-END', 'COMA', 'VARIABLE', 'ARG-LIST-END'],
	['ARG-LIST-END', EPSILON],
	['INSTRUCT-LIST', 'INSTRUCT', 'SEMICOLON', 'INSTRUCT-LIST'],
	['INSTRUCT-LIST', EPSILON],
	['FUNCT-CALL', 'FUNCT-NAME', 'OPEN-PAR', 'FUNCT-CALL-ARG', 'CLOSE-PAR'],
	['FUNCT-CALL', 'PERL-PRIN', 'OPEN-PAR', 'FUNCT-CALL-ARG', 'CLOSE-PAR'],
	['FUNCT-CALL-ARG', 'FUNCT-CALL-ARG-BEG', 'FUNCT-CALL-ARG-END'],
	['FUNCT-CALL-ARG-BEG', 'EXP'],
	['FUNCT-CALL-ARG-BEG', EPSILON],
	['FUNCT-CALL-ARG-END', 'COMA', 'EXP', 'FUNCT-CALL-ARG-END'],
	['FUNCT-CALL-ARG-END', EPSILON],
	['INSTRUCT', 'FUNCT-CALL'],
	['INSTRUCT', 'VARIABLE', 'EQUAL', 'EXP'],
	['INSTRUCT', 'RET', 'EXP'],
	['INSTRUCT', 'COND'],
	['COND', 'OPEN-COND', 'EXP', 'OPEN-BRAC', 'INSTRUCT-LIST', 'CLOSE-BRAC', 'COND-END'],
	['COND-END', 'CLOSE-COND', 'OPEN-BRAC', 'INSTRUCT-LIST', 'CLOSE-BRAC'],
	['COND-END', 'ADD-COND', 'EXP', 'OPEN-BRAC', 'INSTRUCT-LIST', 'CLOSE-BRAC', 'COND-END'],
	['COND-END', EPSILON],
	['SIMPLE-EXP', 'FUNCT-CALL'],
	['SIMPLE-EXP', 'VARIABLE'],
	['SIMPLE-EXP', 'INT'],
	['SIMPLE-EXP', 'STRING'],
	['SIMPLE-EXP', 'OPEN-PAR', 'EXP', 'CLOSE-PAR'],
	['EXP', 'EXP-2', 'EXP-TAIL'],
	['EXP-TAIL', 'EQUIV', 'EXP-2'],
	['EXP-TAIL', 'GT', 'EXP-2'],
	['EXP-TAIL', EPSILON],
	['EXP-2', 'EXP-3', 'EXP-2-TAIL'],
	['EXP-2-TAIL', 'ADD', 'EXP-3'],
	['EXP-2-TAIL', 'MINUS', 'EXP-3'],
	['EXP-2-TAIL', EPSILON],
	['EXP-3', 'SIMPLE-EXP', 'EXP-3-TAIL'],
	['EXP-3-TAIL', 'MUL', 'SIMPLE-EXP'],
	['EXP-3-TAIL', 'DIV', 'SIMPLE-EXP'],
	['EXP-3-TAIL', EPSILON],
]
terminals = set(['END-SYMBOL', 'INT', 'STRING', 'MUL', 'DIV', 'MINUS', 'ADD', 'GT', 'EQUIV', 'EQUAL', 'SEMICOLON', 'COMA', 'OPEN-PAR', 'CLOSE-PAR', 'OPEN-BRAC', 'CLOSE-BRAC', 'OPEN-COND', 'CLOSE-COND', 'ADD-COND', 'RET', 'FUNCT-DEF', 'ID', 'FUNCT-NAME', 'VARIABLE', 'PERL-PRIN', EPSILON])
g6 = cfgrammar.CFGrammar(rules, terminals)

