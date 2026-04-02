import lexer

if __name__ == '__main__':
    print('you ran the wrong file bro')
    exit(1)

def run(code):
    lex = lexer.build_lexer()
    lex.input(code)
    while True:
        tok = lex.token()
        if not tok:
            break
        print(tok)