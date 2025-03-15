import ply.lex as lex
import re

tokens = (
    'COMMENT',
    'SELECT',
    'VAR',
    'WHERE',
    'CE',
    'CD',
    'POINT',
    'ID',
    'TYPE',
    'LIMIT',
    'WORD'
)

t_VAR = r'\?[a-zA-Z]+'
t_CE = r'\{'
t_CD = r'\}'
t_POINT = r'\.'
t_TYPE = r'[a-zA-Z]+:[a-zA-Z]+'
t_ID = r'("[^.]+)'
t_WORD = r'[a-zA-Z]+'

def t_SELECT(t):
    r'select'
    return t

def t_LIMIT(t):
    r'LIMIT.*'
    t.value = re.match(r'LIMIT\s(\d+)', t.value).group(1).strip()
    return t

def t_WHERE(t):
    r'where'
    return t

def t_COMMENT(t):
    r'\#.*'
    t.value = re.match(r'#(.*)', t.value).group(1).strip()
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = '''
# DBPedia: obras de Chuck Berry

    select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
'''

lexer.input(data)
while True:
    tok = lexer.token()

    if not tok:
        break

    print(tok)