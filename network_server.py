#!/usr/bin/python3
#coding: utf-8
# Un peu de réseau...
# Executer ce script depuis la commande pour mettre un serveur en attente d'une connexion
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(("",12800)) # Serveur prêt à écouter sur le port 12800
mySocket.listen(5) # 5 Machines max
tcpConnexion, infos = mySocket.accept() # Attente d'une connexion

print("Connexion réussie : {}".format(infos))
tcpConnexion.send(b"Coucou ! Je viens d'accepter la connexion.")
tcpConnexion.close()
