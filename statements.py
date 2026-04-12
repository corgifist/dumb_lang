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