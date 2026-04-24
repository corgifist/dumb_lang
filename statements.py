import environment as env

class PrintStatement:
    def __init__(self, expr):
        self.expr = expr

    def execute(self):
        print(str(self.expr.eval()))

    def __repr__(self):
        return f"напечатать {str(self.expr)}"
    
class VariableAssignmentStatement:
    def __init__(self, var, value):
        self.var = var
        self.value = value
    
    def execute(self):
        env.vars[self.var] = self.value.eval()

    def __repr__(self):
        return f"{self.var} = {self.value}"
    
class ExpressionStatement:
    def __init__(self, expr):
        self.expr = expr

    def execute(self):
        self.expr.eval()

    def __repr__(self):
        return str(self.expr)
    
class BlockStatement:
    def __init__(self, statements):
        self.statements = statements

    def execute(self):
        for stmt in self.statements:
            stmt.execute()

    def __repr__(self):
        return f"то {' '.join(map(lambda x: x.__repr__(), self.statements))} конец"
    
class IfStatement:
    def __init__(self, expr, if_body, else_body):
        self.expr = expr
        self.if_body = if_body
        self.else_body = else_body

    def execute(self):
        a = self.expr.eval()
        if a:
            self.if_body.execute()
        elif self.else_body is not None:
            self.else_body.execute()

    def __repr__(self):
        return f'если {self.expr} то {self.if_body} ' + 'конец' if self.else_body is None else f'если {self.expr} то {self.if_body} иначе {self.else_body} конец'
    
class WhileStatement:
    def __init__(self, expr, statement):
        self.expr = expr
        self.statement = statement

    def execute(self):
        while self.expr.eval():
            self.statement.execute()

    def __repr__(self):
        return f'пока {self.expr} {self.statement}'