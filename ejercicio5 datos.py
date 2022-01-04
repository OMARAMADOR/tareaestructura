#Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.
dato1 = int(input("Ingrese dato del cateto a:  "))
dato2 = int(input("Ingrese dato del cateto b:  "))
#calculo
import math
valorraiz = (dato1 * 2) + (dato2* 2)
hipotenusa = math.sqrt(valorraiz)
print("El resultado de la hipotenusa es: "+str(hipotenusa))