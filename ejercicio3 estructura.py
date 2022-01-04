#Dado un número N determinar si es un número primo.
#Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo. 
def run():
    num = int(input("Ingresa un número: "))
    x = 1
    cont = 0
    while x <= num:
        if num % x == 0:
            cont = cont +1
        x = x + 1
    if cont == 2:
        print ("Es un número primo")
    else:
        print ("No es un número primo")
if __name__ == "__main__":
    run()