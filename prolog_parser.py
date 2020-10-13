import ply.yacc as yacc
from prolog_lex import tokens


def p_program(p):
    '''program : expression
               | expression program'''
    p[0] = 'program (' + p[1] + ')'
    if len(p) == 3:
        p[0] += ' (' + p[2] + ')'


def p_expression(p):
    '''expression : head DOT
                  | head DECLARE body DOT'''
    p[0] = 'expression (' + p[1] + ') '
    if len(p) == 5:
        p[0] += 'DECLARE (' + p[3] + ') '
    p[0] += 'DOT'


def p_head_atom(p):
    'head : atom'
    p[0] = p[1]


def p_id(p):
    'id : ID'
    p[0] = 'ID ' + p[1]


def p_atom_id(p):
    'atom : id'
    p[0] = 'atom (' + p[1] + ')'


def p_atom_seqatoms(p):
    'atom : id seqatoms'
    p[0] = 'atom (' + p[1] + ') ' + p[2]


def p_seqatoms_id(p):
    'seqatoms : id'
    p[0] = '(atom (' + p[1] + '))'


def p_seqatoms(p):
    'seqatoms : id seqatoms'
    p[0] = '(atom (' + p[1] + ') ' + p[2] + ')'


def p_seqatoms_br(p):
    'seqatoms : LBR seqatoms RBR'
    p[0] = p[2]


def p_seqatoms_br_seqatoms(p):
    'seqatoms : LBR seqatoms RBR seqatoms'
    p[0] = p[2] + ' ' + p[4]



def p_body(p):
    'body : dij'
    p[0] = p[1]


def p_dij(p):
    '''dij : conj
            | conj SEMICOLON dij'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = 'DISJUNCTION (' + p[1] + ') (' + p[3] + ')'


def p_conj(p):
    '''conj : term
            | term COMMA conj'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = 'CONJUNCTION (' + p[1] + ') (' + p[3] + ')'


def p_term(p):
    '''term : atom
            | LBR body RBR'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_error(p):
    raise RuntimeError


def parse(s):
    parser = yacc.yacc()
    return parser.parse(s)
