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

def p_block(p):
    '''block : THEN statements END'''
    p[0] = BlockStatement(p[2])

def p_statement(p):
    '''statement : print_statement
                 | var_assign_statement
                 | expr_statement
                 | block_statement'''
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

def p_block_statement(p):
    '''block_statement : block'''
    p[0] = p[1]

def p_expression(p):
    '''expression : logical_or'''
    p[0] = p[1]

def p_logical_or(p):
    '''logical_or : logical_or OR logical_or
                  | logical_and'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = LogicalExpression(p[1], p[3], 'или')

def p_logical_and(p):
    '''logical_and : logical_and AND logical_and
                   | logical_compare'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = LogicalExpression(p[1], p[3], 'и')

def p_logical_compare(p):
    '''logical_compare : logical_compare LESS logical_compare
                       | logical_compare GREATER logical_compare
                       | logical_compare LESS_EQUAL logical_compare
                       | logical_compare GREATER_EQUAL logical_compare
                       | logical_compare EQUAL_EQUAL logical_compare
                       | logical_compare NOT_EQUAL logical_compare
                       | additive'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = LogicalExpression(p[1], p[3], p[2])

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
