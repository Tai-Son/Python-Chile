# Practica de funciones
#! /usr/bin/python
# -*- coding: iso-8859-15



def f(x):
    y = 2 * x ** 2 + 1
    return y
# Programa que usa la funcion f

n = int(input("Ingrese número: "))

for i in range(n):
    y = f(i)
    print (i,y)
