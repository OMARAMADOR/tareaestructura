#En un estacionamiento el monto a pagar se calcula multiplicando el número de
#horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se
#incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
#Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada
#y la hora de salida de un vehículo (las mismas corresponden a un mismo día)
#calcule el monto a pagar por el dueño del vehículo.
#La entrada vendrá dada por dos enteros positivos el primero representa las horas
#y el segundo los minutos, además por último se debe leer un carácter (A o P) que
#indica si la hora es AM o PM.

def ejercicio6fd (self):
        print("\n")
        tiempo = [0, 0, "", 0, 0, ""]
        tiempos = [0]*2
        horas = ["Su hora de ingreso al estacionamiento es: ", "Los minutos excedentes de entrada", 2, "Hora de partida del estacionamiento", "Los minutos excedentes de salida", 5]
        ct = 0

        for i in horas:
            if (ct != 2 or ct != 5):
                if (i != 2 and i != 5):
                    tiempo[ct] = int(input("Ingrese {}: ".format(i)))
                ct += 1
            if ct == 2 or ct == 5:
                horario = input("La hora que ingresada, ¿Es A.M o P.M? ")
                tiempo[(horas[ct])] = horario

        tiempos[0] = (tiempo[0] * 3600) + (tiempo[1] * 60)
        tiempos[1] = (tiempo[3] * 3600) + (tiempo[4] * 60)

        if tiempo[2] == tiempo[5]:
            nhp = tiempos[1] - tiempos[0]
        else:
            nhp = (43200 - tiempos[0]) + tiempos[1]

        tiempos[0] = (nhp-(nhp % 3600)) / 3600
        tiempos[1] = (nhp%3600)/60
        print(tiempos)
        pagar = tiempos[0] * 4

        if tiempos[1] >= 30:
            pagar = pagar + 2.50
        print("El dueño del vehículo deberá cancelar",pagar, "dolares")