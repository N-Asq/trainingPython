#!/usr/bin/python3
# coding: utf-8

# Comprendre les exceptions

# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

try:
	annee = int(input("Saisissez une année supérieure à 0: "))
	assert annee>0
except ValueError:
	print("Ce n\'est pas un nombre. Bien tenté, bouffon.")
except AssertionError:
	print("On a dit supérieure à 0, c'est quoi ton problème ?")	
else:
	if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    		print("L'année saisie est bissextile.")
	else:
    		print("L'année saisie n'est pas bissextile.")
finally:
	print("Content du résultat ?")
