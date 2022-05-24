"""Calcular el factorial de n"""

print("-------------------------------------")
print("--------Calcular n factorial---------")
print("-------------------------------------")

#Input
n = int(input("Ingrese un numero para hallar su factorial: "))

#Processing
if n >= 0:
    i = 1
    f = 1
    while (i <= n):
        f = f * i
        i = i + 1
        

#Output
print("El factorial de " + str(n) + " es: " + str(f))