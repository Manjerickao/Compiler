class Environment:
    def __init__(self):
        self.vars = {}

    def declare(self, name):
        self.vars[name] = 0

    def set(self, name, value):
        if name not in self.vars:
            raise RuntimeError(f"Variável '{name}' não declarada")
        self.vars[name] = value

    def get(self, name):
        if name not in self.vars:
            raise RuntimeError(f"Variável '{name}' não declarada")
        return self.vars[name]

def eval_expr(expr, env):
    if isinstance(expr, int):
        return expr

    elif isinstance(expr, str):
        # Se for uma variável declarada, pega o valor
        if expr in env.vars:
            return env.get(expr)
        else:
            # Trata como string literal
            return str(expr)

    elif isinstance(expr, tuple):
        op, left, right = expr
        left = eval_expr(left, env)
        right = eval_expr(right, env)

        # Tratamento seguro para strings e inteiros
        if op == '+':
            if isinstance(left, int) and isinstance(right, int):
                return left + right
            elif isinstance(left, str) and isinstance(right, str):
                return left + right
            else:
                raise RuntimeError(f"Erro: não é possível somar {type(left).__name__} com {type(right).__name__}")

        if isinstance(left, str) or isinstance(right, str):
            raise RuntimeError(f"Erro: operação '{op}' inválida com string.")

        if op == '-': return left - right
        if op == '*': return left * right
        if op == '/': return left // right
        if op == '==': return int(left == right)
        if op == '!=': return int(left != right)
        if op == '<': return int(left < right)
        if op == '>': return int(left > right)
        if op == '<=': return int(left <= right)
        if op == '>=': return int(left >= right)


def exec_stmt(stmt, env):
    if stmt[0] == 'assign':
        _, var, expr = stmt
        val = eval_expr(expr, env)
        env.set(var, val)
    elif stmt[0] == 'if':
        _, cond, then_branch, else_branch = stmt
        if eval_expr(cond, env):
            exec_stmt(then_branch, env)
        elif else_branch:
            exec_stmt(else_branch, env)
    elif stmt[0] == 'while':
        _, cond, body = stmt
        while eval_expr(cond, env):
            exec_stmt(body, env)

def exec_block(stmts, env):
    for stmt in stmts:
        exec_stmt(stmt, env)