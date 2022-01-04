#Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es
#capicúa.
#Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás
def run():
    num = int(input('Ingresa el valor de un número: '))
    if num > 9999 and num <= 99999:
        mil = num // 10000
        unidades = num % 10
        if mil == unidades:
            print("Es número capicúa")
        else:
            print("No es un número capicúa")
    else:
        print("No es un número con cinco dígitos")

if __name__ == "__main__":
    run()