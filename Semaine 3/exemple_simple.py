from sly import Lexer
from sly.lex import LexError
import operator

class SimpleLexer(Lexer):
    # token types :
    tokens = {IDENT, OP2, ENTIER, COMMENTS}
    # token specifications :
    
    _operator_2    = '/s([-+*/]|add|sub|mul|div|ADD|SUB|MUL|DIV)'
    _entier_base_16 = '0[xX][^_][0-9A-Fa-f_]*[^_]'
    _entier_base_10 = '[1-9][^_][0-9_]*[^_]'
    _entier_base_8  = '0[oO][^_][0-7_]*[^_]'
    ENTIER = rf'{_entier_base_8}|{_entier_base_10}|{_entier_base_16}'
    OP2 = rf'{_operator_2}'
    
    IDENT =  '[A-Za-z][A-Za-z0-9]*'
    _COMMENT1 = '#[\w\s]*[\n]$'
    _COMMENT2 = '\{[\w\s\n]*\}'
    _COMMENT3 = '<!-[\w\s\n]*->'
    COMMENTS = rf'{_COMMENT1}|{_COMMENT2}|{_COMMENT3}'

    def ENTIER(self,t):
        if(t.value[1]=="x" or t.value[1]=="X"): 
            t.value = int(t.value,16)
        elif(t.value[1]=="o" or t.value[1]=="O"): 
            t.value = int(t.value,8)
        else:
             t.value = int(t.value,10)
        return t
    """
    def OP2(self,t):
        if('add' == t.value or '+' == t.value):
            return operator.add == t.value
        if('sub' == t.value or '-' == t.value):
            return operator.sub == t.value
        if('mul' == t.value or '*' == t.value):
            return operator.mul == t.value
        if('div' == t.value or '/' == t.value):
            return operator.floordiv == t.value
    """

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
 
    #ignore_spaces = r'[ \t]+'
    
if __name__ == '__main__':
    
    analyseur = SimpleLexer()
    #source = 'alpha+321*x5'
    #print('entrez un texte à analyser');
    #source = input()
    #tokenIterator = analyseur.tokenize(source)
    
    print('Les textes à analyser:')
    source = open('entree.txt','r')
    try :
        tokenIterator = analyseur.tokenize(source.read())
        for tok in tokenIterator :
            print(f'token -> type: {tok.type}, valeur: {tok.value} ({type(tok.value)}), ligne : {tok.lineno}')
    except LexError as erreur :
        print("Erreur à l'anayse lexicale ", erreur)
