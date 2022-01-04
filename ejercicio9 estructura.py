#Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir.
def ejercicio9ei (self):
        print("\n")
        print("Desea mostrar las fichas deL domino? ")
        desea = input("Seleccione S (Si) o N (No): ")
        if desea == "S":
            for i in range(1, 7):
                for j in range(i, 7):
                    print("{}:{}".format(i, j))
        else:
            print("No se moestrará las fichas del domino")