import ply.lex as lex

keywords = {
    'напечатать': 'PRINT',
    'или': 'OR',
    'и': 'AND'
}

tokens = (
    'WORD',
    'NUMBER',
    'EQUALS',
    'PLUS',
    'MINUS',
    'STAR',
    'SLASH',
    'LPAREN',
    'RPAREN',
    'LESS',
    'GREATER',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'EQUAL_EQUAL',
    'NOT_EQUAL',
    *keywords.values()
)


t_EQUALS = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_STAR = r'\*'
t_SLASH = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LESS = r'\<'
t_GREATER = r'\>'
t_LESS_EQUAL = r'\<\='
t_GREATER_EQUAL = r'\>\='
t_EQUAL_EQUAL = r'\=\='
t_NOT_EQUAL = r'\!\='

def t_WORD(t):
    r'[a-zA-Zа-яА-Я_][a-zA-Zа-яА-Я_0-9]*'
    if t.value in keywords:
        t.type = keywords[t.value]
    return t

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

lexer = lex.lex()