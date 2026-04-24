import lexer, parser

if __name__ == '__main__':
    print('you ran the wrong file bro')
    exit(1)

def run(code):
    p = parser.build_parser()
    statements = p.parse(code)
    if statements is None:
        return
    print("абстрактное синтаксическое дерево:")
    for statement in statements:
        print(statement)
    for statement in statements:
        statement.execute()