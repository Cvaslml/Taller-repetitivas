"""Calcular el factorial de n"""

from random import randint


print("-----------------------------------------------------------")
print("----Cantidad de veces que sale 3 al lanzar dado n veces----")
print("-----------------------------------------------------------")

#Input
n = int(input("Ingrese el valor de lanzamientos del dado: "))

#Processing
n = 1
while (n <= 10):
    numero = randint(1,6)
    n = n + 1

#Output 
print(str(numero))