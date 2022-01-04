#Dado un número entero N que representa una contraseña y asumiendo que una
#contraseña debe tener al menos 10 dígitos para ser segura, determine si la
#contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
#nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
#mostrar un mensaje de éxito al usuario, por salida estándar.
def ejercicio5ei (self):
        print("\n")
        contraseña = int(input("Ingresar una contraseña de 10 digitos:"))
        m = 0
        while contraseña > 0:
            contraseña //= 10
            m = m + 1
        if m == 10:
            print("la contraseña es correcta")
        else:
            print("La contraseña es incorrecta")
