#!/usr/bin/python3
#coding: utf-8

# Intercepter les signaux de l'OS et s'en servir
import sys
import signal

def closeProgram(signal, frame):
    print("\nEXIT ! (on est passé par une fonction personnalisée)")
    sys.exit(0)

if __name__ == "__main__":
    print("Tests :")

    signal.signal(signal.SIGINT,closeProgram)
    print("Le programme va boucler... Arrêter le avec CTRL+C")
    while True: 
        continue