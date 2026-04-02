import ply.lex as lex

keywords = [

]

tokens = (
    'WORD',
    'NUMBER'
)

t_WORD = r'\w+'

def t_NUMBER(t):
    r'[+-]?(\d+\.)?\d+'
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f'ошибка лексера на символе {t.value[0]}')
    t.lexer.skip(1)

t_ignore = ' \t'

def build_lexer():
    return lex.lex()