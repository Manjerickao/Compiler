import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'IGUAL', 'DIF'),
    ('left', 'MENOR', 'LE', 'MAIOR', 'GE'),
    ('left', 'MAIS', 'MENOS'),
    ('left', 'VEZES', 'DIV'),
)

def p_program(p):
    'program : decls stmts'
    p[0] = ('program', p[1], p[2])

def p_decls(p):
    '''decls : decl decls
             | empty'''
    p[0] = [p[1]] + p[2] if len(p) == 3 else []

def p_decl(p):
    '''decl : INTEIRO ID PONTO_VIRG
            | CHAR ID PONTO_VIRG'''
    p[0] = ('decl', p[1], p[2])

def p_stmts(p):
    '''stmts : stmt stmts
             | empty'''
    p[0] = [p[1]] + p[2] if len(p) == 3 else []

def p_stmt(p):
    '''stmt : ID ATRIB expr PONTO_VIRG
            | SE LPAREN expr RPAREN stmt
            | SE LPAREN expr RPAREN stmt SENAO stmt
            | ENQUANTO LPAREN expr RPAREN stmt'''
    if p[1] == 'se':
        if len(p) == 6:
            p[0] = ('if', p[3], p[5], None)
        else:
            p[0] = ('if', p[3], p[5], p[7])
    elif p[1] == 'enquanto':
        p[0] = ('while', p[3], p[5])
    else:
        p[0] = ('assign', p[1], p[3])

def p_expr_binop(p):
    '''expr : expr MAIS expr
            | expr MENOS expr
            | expr VEZES expr
            | expr DIV expr
            | expr IGUAL expr
            | expr DIF expr
            | expr MENOR expr
            | expr MAIOR expr
            | expr LE expr
            | expr GE expr'''
    p[0] = (p[2], p[1], p[3])

def p_expr_num(p):
    'expr : NUM'
    p[0] = p[1]

def p_expr_string(p):
    'expr : STRING'
    p[0] = p[1]

def p_expr_id(p):
    'expr : ID'
    p[0] = p[1]

def p_expr_paren(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_empty(p):
    'empty :'
    p[0] = []

def p_error(p):
    if p:
        print(f"Erro sintático na linha {p.lineno}: token inesperado '{p.value}'")
    else:
        print("Erro sintático: fim inesperado do arquivo")

parser = yacc.yacc()