from postfixees import evaluate
from postfixees import PostfixException

try :
    ## interactif :
    #expression=input('expression ?')
    ## variable :
    #expression = '16 ->x 8 * 1 +  x *'
    # fichier :
    filename = 'exp.txt'
    with open(filename) as f :
        expression = f.read()
        
    calc = evaluate(expression, verbose = True)
    print(f"Le résultat est {calc}")

except PostfixException  as e :
    print(f"/!\  {e}");


    
    
