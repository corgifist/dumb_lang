import environment as env

class ConstantExpression:
    def __init__(self, const):
        self.const = const

    def eval(self):
        return self.const
    
    def __str__(self):
        return str(self.const)
    
class BinaryExpression:
    def __init__(self, expr1, expr2, op):
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op

    def eval(self):
        if self.op == '+':
            return self.expr1.eval() + self.expr2.eval()
        if self.op == '-':
            return self.expr1.eval() - self.expr2.eval()
        if self.op == '*':
            return self.expr1.eval() * self.expr2.eval()
        if self.op == '/':
            return self.expr1.eval() / self.expr2.eval()
        
    def __repr__(self):
        return str(self.expr1) + f' {self.op} ' + str(self.expr2)
    
class UnaryExpression:
    def __init__(self, expr, op):
        self.expr = expr
        self.op = op

    def eval(self):
        if self.op == '-':
            return -self.expr.eval()
        if self.op == '+':
            return +self.expr.eval()
        
    def __repr__(self):
        return f'{self.op}{str(self.expr)}'
    
class VariableExpression:
    def __init__(self, var):
        self.var = var

    def eval(self):
        return env.vars[self.var]
    
    def __repr__(self):
        return str(self.var)