#!/usr/bin/python3
#coding: utf-8
# Un peu de réseau...
# Executer ce script après avoir executé la partie serveur depuis une autre console
import socket

tcpConnexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpConnexion.connect(("",12800)) # Connexion via le port 12800 du serveur
msg = tcpConnexion.recv(1024) # On lit le message envoyé par le serveur
print("Message du serveur : {}".format(msg))
tcpConnexion.close()
