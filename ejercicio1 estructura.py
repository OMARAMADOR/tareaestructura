#Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene
#dicho número.
num = int(input("Ingrese un número: "))
contador = len(str(num))
print("El numero ingresado tiene %s digitos" % (contador))
