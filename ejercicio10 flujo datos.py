#En un almacén se hace un 20% de descuento a los clientes cuya compra supere
#los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
#pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
#necesario.
def run():
    monto = int(input("Ingrese el monto a cancelar para verificar si obtiene el descuento: "))
    if monto > 1000:
        descuento1 = monto * 0.20
        valorapagar = monto - descuento1
        print ("El monto a cancelar es: ", valorapagar)
        print("Nota: incluido descuento de 20%")
    else:
        print("El monto a cancelar es:", monto)
        print("Nota: El monto a cancelar no incluye descuento")

if __name__ == "__main__":
    run()