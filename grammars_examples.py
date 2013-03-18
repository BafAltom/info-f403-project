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

