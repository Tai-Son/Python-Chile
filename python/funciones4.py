# Practica de funciones
#! /usr/bin/python
# -*- coding: iso-8859-15

def primo(a):
    c = 0
    for i in range(1, a+1):
        if a%i == 0:
            c = c + 1
    if c > 2:
        return False
    else:
        return True
#Programa que lista los numeros primos en el rango

a = int(input("Desde: "))
b = int(input("Hasta: "))
for a in range(a, b+1):
    if primo(a):
        print("Numero primo: ", a)

