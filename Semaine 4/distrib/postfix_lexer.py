"""
Benedictus Kent Rachmat
Groupe 6B
"""

from sly import Lexer
from sly.lex import LexError
import operator

class PostfixLexer(Lexer):
    # token types :
    tokens = {IDENT,OP1, OP2, ENTIER, POP,SET}
    
    # token specifications :
    SET             = '->[A-Za-z](_?[A-Za-z0-9])*'
    POP             = 'pop|POP'
    
    OP2             = '[-+*/]|add|sub|mul|div|ADD|SUB|MUL|DIV'
    OP1             = 'opp|OPP'
    
    _entier_base_16 = '0[xX][0-9A-Fa-f_](_?[0-9A-Fa-f_])*'
    _entier_base_10 = '[0-9](_?[0-9_])*'
    _entier_base_8  = '0[oO][0-7](_?[0-7])*'
    ENTIER = rf'{_entier_base_8}|{_entier_base_10}|{_entier_base_16}'
    IDENT =  '[A-Za-z][A-Za-z0-9]*'

    def ENTIER(self,t) :
        if (len(t.value) == 1):
            t.value = int(t.value,10)
            return t
        if(t.value[1] == "x" or t.value[1] == "X"): 
            t.value = int(t.value,16)
        elif(t.value[1] == "o" or t.value[1] == "O"): 
            t.value = int(t.value,8)
        else:
             t.value = int(t.value,10)
        return t

    def OP1(self,t):
        t.value = (lambda x : -x)
        return t

    def OP2(self,t):
        if(t.value in {'add','ADD','+'}):
            t.value = operator.add
        if(t.value in {'sub','SUB','-'}):
            t.value = operator.sub
        if(t.value in {'mul','MUL','*'}):
            t.value = operator.mul
        if(t.value in {'div','DIV','/'}):
            t.value = operator.floordiv
        return t
    
    def POP(self,t):
        #t.pop()
        return t
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    @_(r'#.*')
    def ignore_hastag(self, t):
        self.lineno += len(t.value)
        
    @_(r'<!-[\w\s\n]*->')
    def ignore_fleche(self, t):
        self.lineno += len(t.value)
        
    @_(r'{[^}]*}')
    def ignore_accolade(self, t):
        self.lineno += len(t.value)
 
    @_(r'\s+')
    def ignore_espace(self, t):
        self.lineno += len(t.value)
        
if __name__ == '__main__':
    import sys
    analyseur = PostfixLexer()
    #source = 'alpha+321*x5'
    print('entrez un texte a analyser :')
    source = sys.stdin.read()
    tokenIterator = analyseur.tokenize(source)
    try:
        for tok in tokenIterator :
            print(f'token -> type: {tok.type}, valeur: {tok.value} ({type(tok.value)}), ligne : {tok.lineno}')
    except LexError as erreur :
        print("Erreur à l'anayse lexicale ", erreur)