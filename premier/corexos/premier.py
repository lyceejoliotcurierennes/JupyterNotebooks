# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

from math import sqrt

def estPremier(n):
    try: #teste si nombre est bien un entier en essayant de le convertir
        n=int(n)
    except:
        print("vous n'avez pas entré un entier")
    if n<0:
        n=-n
    if n==2 or n==3:
        return True
    if n%2==0 or n<=1:
        return False
    d=3
    while n%d!=0 and d <= sqrt(n):
        d+=2
    return n%d!=0

inputs_estPremier = [
    Args(1), Args(2), Args(3), Args(5), Args(17), Args(1001)  
]

exo_estPremier = ExerciseFunction(
    estPremier,
    inputs_estPremier,
    layout='pprint',
    layout_args=(60, 25, 25),
)