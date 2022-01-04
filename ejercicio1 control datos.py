#Todos los años que se dividen exactamente entre 400, o que son divisibles
#exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
#Usando estas premisas crea un algoritmo que lea una fecha como un número
#entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
#el mismo es un año bisiesto o no.
def run():
    fecha = int(input("Fecha en formato DDMMAAAA:"))
    año = fecha % 10000
    dia = fecha // 1000000
    mes = (fecha // 10000) % 100

    if año % 4 != 0:
        print("El año",año,"no es bisiesto")
    elif año % 4 == 0 and año % 100 != 0:
        print("El año",año, "es bisiesto")

if __name__ == "__main__":
    run()