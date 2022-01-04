#Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
#decenas, centenas y unidades de mil.
#Entrada:
#1234
#Salida:
#Unidades: 4
#Decenas: 3
#Centenas: 2
#Unidades de mil: 1
def run():
    num = int(input("Ingrese un número: \n"))
    n = str(num)
    print("Entrada:\n", num)
    print("Salida:")
    print("Unidades {}".format(n[3]))
    print("Decenas {}".format(n[2]))
    print("Centenas {}".format(n[1]))
    print("Unidades de mil {}".format(n[0]))

if __name__ == "__main__":
    run()