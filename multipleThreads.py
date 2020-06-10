#!/usr/bin/python3
#coding: utf-8
import random
import sys
from threading import Thread
import time

import random
import sys
from threading import Thread, RLock
import time

verrou = RLock() # Le lock sert à obliger un thread à attendre avant d'utiliser une ressource utilisée par un autre thread

class Afficheur(Thread):

    """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 5:
            with verrou: # On appelle le lock comme ça. Tout ce qui est à l'intérieur ne peut être exécuté que si le lock est disponible (aucun thread ne l'utilise)
                for lettre in self.mot:
                    sys.stdout.write(lettre) #On écrit une lettre du mot
                    sys.stdout.flush() # Obligatoire pour que le print se fasse tout de suite et pas en bloc à la fin du programme
                    attente = random.randint(0, 21) / 100 # Attente
                    time.sleep(attente) # On atten avant d'afficher chaque lettre, mais aucun thread ne peut utiliser cette boucle tant que le with n'est pas fini
            i += 1


if __name__ == "__main__":
    print("Tests :")
    # Création des threads
    thread_1 = Afficheur("canard")
    thread_2 = Afficheur("TORTUE")

    # Lancement des threads
    thread_1.start()
    thread_2.start()

    # Attend que les threads se terminent
    thread_1.join()
    thread_2.join()

    print("\n")