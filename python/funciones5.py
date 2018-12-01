# Escribir una funcion recursiva para contar en cuantos intentos se puede adivinar un numero de un dado 
#Practica de funciones
#! /usr/bin/python
# -*- coding: iso-8859-15

from random import *

x = int(input("Adivina el numero: "))
n = randint(1, 6)

print "Numero aleatorio: ", n

def adivina(intento):
    if x != n:
        print ( "Fallaste, intenta de nuevo",n)
        intento = intento + 1
    else:
        print("Acertasate", intento)

for i in range(1):
    if x != n:
        print "Fallaste, intenta de nuevo "
    else:
        print "Acertasate"

