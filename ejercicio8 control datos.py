#Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año
#2014 e imprima por pantalla el número de días que han pasado desde el 1 de
#Enero de 2014 hasta la fecha dada.
año = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))
from datetime import date 
fechainicial = date(2014,1,1) 
fechafinal= date(año,mes,dia) 
#calculo
dias = fechafinal - fechainicial
print (dias)

