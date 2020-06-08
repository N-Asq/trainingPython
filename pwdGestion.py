#!/usr/bin/python3
#coding: utf-8

# Non-affichage des mdp à l'écran et hashing

from getpass import getpass
import hashlib

print("Algorithmes garantis par Python : {}".format(hashlib.algorithms_guaranteed))
print("Algorithmes disponibles sur l'OS : {}".format(hashlib.algorithms_available))

mdp = getpass("Tapez un mot de passe : ")
hashedMdp = hashlib.sha1(str.encode(mdp))
print("Mot de passe chiffré en héxadécimal : {}".format(hashedMdp.hexdigest()))
print("Veuillez maintenant retapez votre mot de passe pour vous authentifier :")

locked = True
while locked:
    mot = getpass("Mot de passe : ")
    hashedMot = hashlib.sha1(str.encode(mot))
    if hashedMot.hexdigest() == hashedMdp.hexdigest():
        locked = False
    else:
        print("Mot de passe incorrect. Veuillez réessayer.")
print("Accès dévérouillé. Fermeture du programme.")