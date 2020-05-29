#!/usr/bin/python3
# coding: utf-8

# Comprendre les fonctions

"""Module multipli contenant la fonction table"""

def table(nb = 7, max = 10):
	"""Fonction affichant la table de multiplication
	 par nb de 1 * nb jusqu'à max * nb"""
	for i in range(1,max+1):
		print(nb," x ",i," = ",nb*i)
		
if __name__ == "__main__":
	table(8,5)
