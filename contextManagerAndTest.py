#!/usr/bin/python3
#coding: utf-8

# Test des fonctions de random et exemple de contexte manager avec le mot with
# Liste des différentes assertions : 
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/2235416-creez-des-tests-unitaires-avec-unittest
# Depuis la console et en se plaçant dans un package contenant des tests, "python3.4 -m unittest" permet de tous les lancer d'un coup
# Toute la sous-arborescence commençant par test sera également fouillée
import random
import unittest

import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        self.liste = list(range(10))

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste)
        self.assertIn(elt, self.liste)

    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)))

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)

        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)

if __name__ == "__main__":
    print("Tests :")
    unittest.main()