#Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho
#número.
def run():
    número = int(input("Ingrese un número entre el 1 y el 12: "))
    if número == 1:
        print("Enero")
    elif número == 2:
        print("Febrero")
    elif número == 3:
        print("Marzo")
    elif número == 4:
        print("Abril")
    elif número == 5:
        print("Mayo")
    elif número == 6:
        print("Junio")
    elif número == 7:
        print("Julio")
    elif número == 8:
        print("Agosto")
    elif número == 9:
        print("Septiembre")
    elif número == 10:
        print("Octubre")
    elif número == 11:
        print("Noviembre")
    elif número == 12:
        print("Diciembre")
    else:
        print("No existe mes con ese número")

if __name__ == "__main__":
    run()