#!/usr/bin/python3
#coding: utf-8
# Différentes classes pour mieux comprendre comment fonctionnent les itérateurs

# METHODE 1 : On créé une classe héritant de string et contenant un itérateur différent
class RevStr(str):
    def __iter__(self):
        """Cette méthode renvoie un itérateur parcourant la chaîne
        dans le sens inverse de celui de 'str'"""
        return ItRevStr(self) # On renvoie l'itérateur créé pour l'occasion
# Définition de l'itérateur
class ItRevStr:
    def __init__(self, chaine_a_parcourir):
        """On se positionne à la fin de la chaîne"""
        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)
    def __next__(self):
        if self.position == 0: # Fin du parcours
            raise StopIteration
        self.position -= 1 # On décrémente la position
        return self.chaine_a_parcourir[self.position]


# METHODE 2 : On créé directement un itérateur et on passe notre string en argument au moment de l'instanciation
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self # Iter se renvoit lui même

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# METHODE 3 : Test avec héritage et changement de __init__ __iter__ et __next__ dans le même objet
class ReverseString(str):
    def __init__(self, data):
        str.__init__(self)
        self.index = len(data)

    def __iter__(self):
        return self # Iter se renvoit lui même

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self[self.index]

# METHODE 4 : Test avec générateur 
def ReverseSpell(chaine):
    index = len(chaine)
    while index!=0:
        index -= 1
        yield chaine[index]


########## TEST ##########
if __name__ == "__main__":
    chaine = "Spam"

    print("Test méthode 1 :")
    ma_chaine = RevStr(chaine) # Création d'une chaîne inverse héritée d'une chaîne standard dont la méthode __iter__ a été modifiée 
    for lettre in ma_chaine: # Le mot-clé fort utilise la méthode __iter__ modifiée qui parcours les lettres à l'envers
        print(lettre)
    print("\n")
    for lettre in ma_chaine.upper(): # En utilisant une des méthodes de str, on renvoie une str par une RevStr. Il faut boucler sur RevStr(ma_chaine.upper())
        print(lettre)

    print("\nTest méthode 2 :")
    ma_chaine = ReverseIterator(chaine) # On créé un itérateur à partir de la chaîne
    for lettre in ma_chaine:
        print(lettre)
    # IMPOSSIBLE D'UTILISER LES METHODES DE str ICI. L'objet ReverseIterator contient un attribut data de type chaîne mais n'est pas une chaîne lui-même
    print("\n")
    for lettre in ReverseIterator(chaine.upper()): # On transforme notre str avant de faire appel à l'itérateur (même problème que pour la METHODE 1)
        print(lettre)

    print("\nTest méthode 3 :")
    ma_chaine = ReverseString(chaine) 
    for lettre in ma_chaine: # ça fonctionne
        print(lettre)
    print("\n")
    for lettre in ma_chaine.upper(): # Même problème que la méthode 1. Il faut boucler sur ReverseString(ma_chaine.upper())
        print(lettre)

    print("\nTest méthode 4 :")
    for lettre in ReverseSpell(chaine): 
        print(lettre)