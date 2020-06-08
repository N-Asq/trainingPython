#!/usr/bin/python3
#coding: utf-8
# Module Fraction
from fractions import Fraction
unDemi = Fraction(1,2)
unTiers = Fraction("1/3")
unSixieme = Fraction(unTiers,2)
unHuitieme = Fraction.from_float(0.125)
unHuitieme_float = float(unHuitieme)

print("Sans Fraction : 1/2 + 1/3 + 1/6 = {}".format(1/2+1/3+1/6))
print("Avec Fraction : 1/2 + 1/3 + 1/6 = {}".format(unDemi+unTiers+unSixieme))