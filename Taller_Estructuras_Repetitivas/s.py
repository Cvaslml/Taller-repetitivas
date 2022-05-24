""""Determinar si un numero entero positivo es primo o no"""


print("----------------------------------")
print("--------Numero primo o no---------")
print("----------------------------------")

#Input
n = int(input("Ingrese un numero: "))

#Processing
x = 1
c = 0
while ( x <= n):
    if n % x == 0:
        c = c + 1
    x = x + 1 
if c == 2:
    msj = "El numero " + str(n) + " es primo"
else:
    msj = "El numero " + str(n) + " no es primo"

#Output
print(msj)