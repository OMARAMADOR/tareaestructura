#Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que
#la serie termina al leer un 0.
def ejercicio10ei (self):
        print("\n")
        contador = 0
        suma = 0
        num = int(input("Ingrese un número: "))
        while num > 1:
            num = int(input('Ingrese un número entero (0 para terminar): '))
            suma += num
            contador += 1
            if contador == 0:
                print('No ingreso ningun número: ')
            else:
                promedio = suma / contador
        print('El promedio de los {} numeros es igual a {}.'.format(contador, promedio))