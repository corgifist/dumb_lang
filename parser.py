import ply.yacc as yacc

from lexer import tokens
from statements import *
from expressions import *

start = 'program'

def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : print_statement
                 | var_assign_statement
                 | expr_statement'''
    p[0] = p[1]

def p_var_assign_statement(p):
    '''var_assign_statement : WORD EQUALS expression'''
    p[0] = VariableAssignmentStatement(p[1], p[3])

def p_print_statement(p):
    '''print_statement : PRINT expression'''
    p[0] = PrintStatement(p[2])

def p_expr_statement(p):
    '''expr_statement : expression'''
    p[0] = ExpressionStatement(p[1])

def p_expression(p):
    '''expression : additive'''
    p[0] = p[1]

def p_additive(p):
    '''additive : additive PLUS additive
                | additive MINUS additive
                | multiplicative'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryExpression(p[1], p[3], p[2])

def p_multiplicative(p):
    '''multiplicative : multiplicative STAR multiplicative
                      | multiplicative SLASH multiplicative
                      | unary'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinaryExpression(p[1], p[3], p[2])

def p_unary(p):
    '''unary : PLUS unary
             | MINUS unary
             | primary'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = UnaryExpression(p[2], p[1])

def p_primary(p):
    '''primary : LPAREN expression RPAREN
               | WORD
               | NUMBER'''
    if len(p) == 4:
        p[0] = p[2]
    elif type(p[1]) is str:
        p[0] = VariableExpression(p[1])
    else:
        p[0] = ConstantExpression(p[1])

def p_error(p):
    print("ошибка на", p)

def build_parser():
    return yacc.yacc()