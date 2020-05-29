#!/usr/bin/python3
#coding: utf-8

# Comprendre le fonctionnement et les compréhensions des listes et dictionnaires

# Utiliser attrgetter pour trier des objets

liste = [("pommes", 22),("melons", 4),("poires", 18),("fraises", 76),("prunes", 51)]
dico = {"pommes":22,"melons":4,"poires":18,"fraises":76,"prunes":51}

liste_inverse = [(quantity,fruit) for (fruit,quantity) in liste]
liste = [(fruit,quantity) for (quantity,fruit) in sorted(liste_inverse,reverse = True)]

dico = {fruit: quantity for (fruit,quantity) in sorted(dico.items(),key = lambda item: item[1],reverse = True)}

for a in dico:
    print(a)
print(liste)
print(dico)

