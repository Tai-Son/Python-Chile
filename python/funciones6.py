# Escribir una funcion recursiva para contar en cuantos intentos
#Practica de funciones
#! /usr/bin/python
# -*- coding: iso-8859-15

from random import *

def adivina(n):
    n = randint(1,6)
    return n

a = int(input("Adivina el numero: "))

for i in range(a):
    print adivina(1)
    if a== adivina(i):
        print("Acerto ", a, i )
    else:
        print ("Fallo", a, i)
