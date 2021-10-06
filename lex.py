# ------------------------------------------------------------
# calclex.py
#
# tokenizer para um avaliador de expressão simples para
# números e +, -, *, /
# --------------- ---------------------------------------------

import ply.lex as lex

# Lista de nomes de tokens. Isso é sempre necessário
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'TEXT', #  regras para identificadores
    'EQUALS', # regras para atribuição e final de linha (;)
    'SEMICOLON' # regras para atribuição e final de linha (;)
)

# Regras de expressão regular para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_TEXT = r'\w+' # regras para identificadores
t_EQUALS = r'=' # regras para atribuição e final de linha (;)
t_SEMICOLON = r';' # regras para atribuição e final de linha (;)


# Uma regra de expressão regular com algum código de ação


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Uma string contendo caracteres ignorados (espaços e tabulações)
t_ignore = ' \t'

# Regra de tratamento de erro


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construa o lexer
lexer = lex.lex()

