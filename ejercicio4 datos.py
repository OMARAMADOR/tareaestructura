#Dados tres (3) números, Hacer una aplicación que calcule la resolvente.
from math import sqrt

num1 = int(input("Ingrese el primer número: \n"))
num2 = int(input("Ingrese el segundo número: \n"))
num3 = int(input("Ingrese el tercer número: \n"))
x1 = 0
x2 = 0

if ((num2 ** 2) - 4 * num1 * num3) < 0:
    print("La solución de la ecuación es con números complejos")
else:
    x1 = (-num2 + sqrt(num2 ** 2 - (4 * num1 * num3))) / (2 * num1)
    x2 = (-num2 - sqrt(num2 ** 2 - (4 * num1 * num3))) / (2 * num1)
    print("Las soluciones son:")
    print("El valor de x1 es:",x1)
    print("El valor de x2 es:",x2)
