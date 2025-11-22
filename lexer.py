import ply.lex as lex

reserved = {
    'inteiro': 'INTEIRO',
    'char': 'CHAR',
    'se': 'SE',
    'senao': 'SENAO',
    'enquanto': 'ENQUANTO',
}

tokens = [
    'ID', 'NUM', 'STRING',
    'MAIS', 'MENOS', 'VEZES', 'DIV',
    'IGUAL', 'DIF', 'MENOR', 'MAIOR', 'LE', 'GE',
    'ATRIB', 'PONTO_VIRG', 'LPAREN', 'RPAREN',
] + list(reserved.values())

t_MAIS       = r'\+'
t_MENOS      = r'-'
t_VEZES      = r'\*'
t_DIV        = r'/'
t_IGUAL      = r'=='
t_DIF        = r'!='
t_MENOR      = r'<'
t_MAIOR      = r'>'
t_LE         = r'<='
t_GE         = r'>='
t_ATRIB      = r'='
t_PONTO_VIRG = r';'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'

t_ignore = ' \t'

def t_COMMENT(t):
    r'/\*([^*]|\*+[^*/])*\*+/'
    pass

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^\\"]|\\n|\\t)*"'
    t.value = t.value[1:-1].replace('\\n', '\n').replace('\\t', '\t')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Erro léxico na linha {t.lineno}: caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()