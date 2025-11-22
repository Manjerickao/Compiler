from parser import parser
from interpreter import Environment, exec_block

with open("exemplo5.ft","r", encoding="utf-8") as f:
    data = f.read()

result = parser.parse(data)

if result:
    _, decls, stmts = result
    env = Environment()
    for decl in decls:
        _, tipo, nome = decl
        env.declare(nome)

    print("\nDeclarações:")
    print([d[2] for d in decls])

    print("\nExecutando código:")
    try:
        exec_block(stmts, env)
    except RuntimeError as e:
        print("Erro de execução:", e)