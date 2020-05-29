#!/usr/bin/python3
#coding: utf-8

# Voir https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/233857-manipulez-les-expressions-regulieres
import re

chaine = "Ceciiii est une chaîne de caractère. \n\
Elle est plutôt longue mais c''est nécessaire pour caractériser les expressions régulières...\n\
Pas de chichi ! Au travail !"

print(chaine)
re.search

if __name__=="__main__":
    print("Tests :")

    print("\nChaîne utilisée :")
    print(chaine)

    print("\nRecherche d'un r suivi de 1 ou plusieurs a optionnels puis un c, un e, un v ou une majuscule ou un nombre entre 2 et 6:")
    print(re.search("ra*[cevA-Z2-6]",chaine))

    print("\nRecherche de 3 à 7 i à la suite :")
    print(re.search("i{3,7}",chaine))

    print("\nRecherche du groupe ""chi"" de 0 à 6 fois (Pas de):")
    print(re.search("(Pas de )(chi){,6}",chaine))

    print("\nRecherche du groupe ""chi"" 0 ou 1 fois après le mot (Pas de) :")
    print(re.search("(Pas de )(chi)?",chaine))

    print("\nRecherche du groupe ""chi"" au moins 1 fois :")
    print(re.search("(chi)+",chaine))