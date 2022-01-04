#Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
#resultado su equivalente en segundos.
def run():
    horas = int(input("Ingrese las horas:"))
    minutos = int(input("Ingrese los minutos:"))
    s1 = horas * 3600
    s2 = minutos * 60
    segundos = s1 + s2
    print("En total hay", segundos, "segundos")

if __name__ == "__main__":
    run()