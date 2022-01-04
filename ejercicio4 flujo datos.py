#Para un valor entero positivo que representa una cantidad en segundos, indicar
#su equivalente en minutos, horas y días.
def run():
    segundos = int(input("Ingrese los segundos:"))
    dia = segundos // 86400
    resto1 = segundos % 86400
    horas = resto1 // 3600
    resto2 = resto1 % 3600
    minutos = resto2 // 60
    resto3 = resto2 % 60
    print("Son", dia, "dia(s),", horas, "horas,",minutos, "minutos",resto3, "segundos en total")

if __name__ == "__main__":
    run()