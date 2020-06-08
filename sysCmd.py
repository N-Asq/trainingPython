#!/usr/bin/python3
#coding: utf-8
# Envoyez des cmd system
import os
if __name__ == "__main__":
    print("Tests :")
    filedir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(filedir)
    os.system("ls -lah")
#La fonction system exécute un environnement particulier rien que pour votre commande. 
#Cela veut dire, entre autres, que system retournera tout de suite même si la commande tourne toujours.
#En gros, si vous faites os.system("sleep 5"), le programme ne s'arrêtera pas pendant cinq secondes.