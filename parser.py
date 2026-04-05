import ply.yacc as yacc

from lexer import tokens
from lang_ast import *

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
    '''statement : print_statement'''
    p[0] = p[1]

def p_print_statement(p):
    '''print_statement : PRINT expression'''
    p[0] = PrintStatement(p[2])

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
               | NUMBER'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = ConstantExpression(p[1])

def p_error(p):
    print("ошибка на", p)

def build_parser():
    return yacc.yacc()