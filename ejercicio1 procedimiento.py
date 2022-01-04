#Construya una función que solicite edades al usuario y determine el promedio de
#las edades mayores a 18 años. El usuario indicará cuando desea dejar de
#suministrar datos de entrada. En la Acción Principal se informará el promedio
#calculado.

print("\n")
print("\tProcedimientos (Acciones y Funciones)")
print("\n")
acumulador = 0
nedad = int(input("Ingrese cuantas edades se ingresará: "))
for i in range(nedad):
    edad = int(input("Ingrese la edad, nota: las edades deben ser mayores a 18: "))
    if edad >= 18:
        acumulador = acumulador + edad
        promedio = acumulador / nedad
    print("El promedio de las edades es de", promedio)