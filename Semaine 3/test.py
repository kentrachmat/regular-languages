from sly import Lexer
from sly.lex import LexError
#import operator

class SimpleLexer(Lexer):
    # token types :
    tokens = {IDENT, OP2, ENTIER}
    # token specifications :
    
    OP2 =    '[-+*/]'
    ENTIER = '[0-9]+'
    IDENT =  '[A-Za-z][A-Za-z0-9]*'


    def ENTIER(self,t) :
        t.value = int(t.value)
        return t
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
 

if __name__ == '__main__':
    
    analyseur = SimpleLexer()
    source = 'alpha + 321*x5'
    print('entrez un texte à analyser');
    #source = input()
    tokenIterator = analyseur.tokenize(source)
    try :
        for tok in tokenIterator :
            print(f'token -> type: {tok.type}, valeur: {tok.value} ({type(tok.value)}), ligne : {tok.lineno}')
    except LexError as erreur :
        print("Erreur à l'anayse lexicale ", erreur)