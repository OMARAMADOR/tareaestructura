#Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla
#del 1 hasta la del 10.
def run():
    num = int(input("Introduzca el número de la tabla que desee: "))
    for i in range(0,11):
        resul = i * num
        print(num, "x", i, "=", resul)
if __name__ == "__main__":
    run()