#Dado un número, determine si es capicúa.
#Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.
def ejercicio2ei (self):
        print("\n")
        num = int(input('Ingresa el valor de un número: '))
        if str(num) == str(num)[::-1]:
            print("Si es capicúa")
        else:
            print("No es capicúa")