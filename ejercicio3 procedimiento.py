#Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la
#suma de los lados del polígono).
def ejercicio3ayf (self):
        print("\n")
        print("¿De que tipo de pentagono quiere calcular el perímetro?")
        penta = int(input("Regular o irregular? /n Nota: Regular es 1 e Irregular es 0: "))
        if penta == 1:
            lado = int(input("Ingrese el valor de los lados del pentágono: "))
            perimetro = lado * 5
            print(str(lado) + "+" + str(lado) + "+" + str(lado) + "+" + str(lado) + "+" + str(lado) + " es igual a:", perimetro)
        else:
            lado1 = int(input("Ingrese el valor del primer lado del pentágono: "))
            lado2 = int(input("Ingrese el valor del segundo lado del pentágono: "))
            lado3 = int(input("Ingrese el valor del tercer lado del pentágono: "))
            lado4 = int(input("Ingrese el valor del cuarto lado del pentágono: "))
            lado5 = int(input("Ingrese el valor del quinto lado del pentágono: "))
            perimetro = lado1 + lado2 + lado3 + lado4 + lado5
            print("El perímetro del pentágono es", perimetro)