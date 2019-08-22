# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

def estBissextile(annee):
	try: #teste si annee est bien un entier en essayant de le convertir
		annee=int(annee)
	except:
		print("vous n'avez pas entré un entier")
	if annee%4!=0:
		return False
	elif annee%100==0:
		if annee%400:
			return True
		else:
			return False
	else:
		return True
		
inputs_estBissextile=[Args(2000),Args(2019),Args(2020),Args(2100)]
		
exo_estBissextile = ExerciseFunction(
    estBissextile,
    inputs_estBissextile,
    layout='pprint',
    layout_args=(60, 25, 25),
)