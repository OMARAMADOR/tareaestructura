#Construya un programa que dado un valor entero N, haga el cálculo de la función
#factorial utilizando estructuras iterativas.
def run():
    num = int(input('Ingresa un número: '))
    factorial = 1
    if num!=0:
        for i in range(1, num + 1):
            factorial = factorial*i
    print("Factorial:", factorial)
if __name__ == "__main__":
    run()