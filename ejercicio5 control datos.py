#Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
#mayor? y ¿cuál es el segundo mayor?
def run():
    print("Ingrese tres números enteros positivos")
    A = int(input("A: "))
    B = int(input("B: "))
    C = int(input("C: "))

    if A > B and A > C:
        print(A, "es el número mayor")
        if B > C:
            print (B, "es el segundo número mayor")
        else:
            print(C, "es el segundo número mayor")
    elif B > A and B > C:
        print(B, "es el número mayor")
        if A > C:
            print (A,"es el segundo número mayor")
        else:
            print(C,"es el segundo número mayor")
    elif C > A and C > B:
        print(C, "es el número mayor")
        if A > B:
            print (A, "es el segundo número mayor")
        else:
            print (B, "es el segundo número mayor")
    else:
        print ("No se puede determinar")

if __name__ == "__main__":
    run()
