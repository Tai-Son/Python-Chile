#Simular el lanzamiento de un dado y determine la cantidad de lanzamientos hasta que salga el numero 5.
#! /usr/bin/python
# -*- coding: iso-8859-15


from random import *
n = int(input("Ingrese la cantidad de intentos: "))
x = 0
while True:
    x = randint(1,6)
    print x
    i =x+1
    if x == 5:
        break
print "El Lanzamiento en el que salio 5 fue,", i

    