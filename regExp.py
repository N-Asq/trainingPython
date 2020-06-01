#!/usr/bin/python3
#coding: utf-8

# Voir https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/233857-manipulez-les-expressions-regulieres
import re

chaine = "ceciiii est une chaîne de caractère. \n\
Elle est plutôt longue mais ceci est nécessaire pour caractériser les expressions régulières...\n\
Pas de chichi ! Au travail !"

print(chaine)
re.search

if __name__=="__main__":
    print("Tests :")

    print("\nChaîne utilisée :")
    print(chaine)

    print("\nRecherche d'un r suivi de 1 ou plusieurs a optionnels puis un c, un e, un v ou une majuscule ou un nombre entre 2 et 6 :")
    print(re.search("ra*[cevA-Z2-6]",chaine))

    print("\nRecherche d'au moins 5 i à la suite précédé d'un c et suivi d'un espace :")
    print(re.search("ci{5,} ",chaine))

    print("\nRecherche de 1 à 3 i à la suite précédé d'un c et suivi d'un espace :")
    print(re.search("ci{1,3} ",chaine))

    print("\nRecherche du groupe (ceci) en début de chaine :")
    print(re.search("^ceci",chaine))

    print("\nRecherche du groupe (chi) de 0 à 6 fois précédé de (Pas de) et suivi de ( !) :")
    print(re.search("(Pas de )(chi){,6}",chaine))

    print("\nRecherche du groupe (chi) 0 ou 1 fois précédé de (Pas de) et suivi de ( !) :")
    print(re.search("(Pas de )(chi)? !",chaine))

    print("\nRecherche du groupe (chi) au moins 1 fois :")
    print(re.search("(chi)+",chaine))

    regExp = r"^((0|(\+[1-9]{1,3}))[0-9]([ .-]?[0-9]{2}){4})$"
    compRegExp = re.compile(regExp) # Compilation pour gagner en rapidité lors des opérations
    telNum = ""
    while compRegExp.search(telNum) is None: # Version non compilée : while re.search(regExp,telNum) is None: 
        telNum = input("\nVeuillez taper un numéro de téléphone ayant un format valide : ")

    # On enlève les séparateurs
    telNum = re.sub(r"[ .-]+",r"",telNum)
    # On met entre paranthèses l'éventuel +xxx
    telNum = re.sub(r"(?P<pays>\+[1-9]{1,3})(?P<digits>[0-9]{9})",r"(\g<pays>) 0\g<digits>",telNum)
    print("Le numéro [{numero}] est valide !".format(numero = telNum))