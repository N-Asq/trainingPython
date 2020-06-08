#!/usr/bin/python3
#coding: utf-8
# Script à éxécuter en ligne de commande pour voir l'effet de l'interprétation des options
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("x", type = float, help="Le nombre sur lequel effectuer l'opération.")
parser.add_argument("op", type = str, help="L'opération à effectuer. Pour le moment sqrt ou square.")
parser.add_argument("-v", "--verbose", action="store_true",help="Pour que le programme soit bavard.") 
# Avec "store_true", on précise que l'argument est un booléen qui vaut True si il est précisé

args = parser.parse_args()

if len(sys.argv) < 3:
    print("Précisez un nombre, puis une opération en paramètre.")
    sys.exit(1)

operation = sys.argv[2]

if args.verbose:
    print("Le nombre spécifié est {}".format(args.x))
    print("L'opération à effectuer est {}".format(args.op))
    print("Les arguments passés à cette fonction sont : ",sys.argv)

if operation == "sqrt":
    print("On renvoie la racine du nombre : {}".format(math.sqrt(args.x)))
elif operation == "square":
    print("On met le nombre au carré : {}".format(pow(args.x,2)))
else:
    print("Je ne connais pas cette operation.")