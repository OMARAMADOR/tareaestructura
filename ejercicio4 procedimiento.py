#En una empresa pagan según las horas trabajadas y una tarifa fija por hora. Si la
#cantidad de horas trabajadas en una semana es mayor a 40, la tarifa se
#incrementa en un 35% para las horas extras. Escribe una acción principal que
#solicite la identificación de 5 empleados, el monto cancelado por hora, y la
#cantidad de horas trabajadas por cada uno, llame a acciones/funciones que
#calculen el salario semanal por horas trabajadas (<=40) y los ingresos por
#concepto de horas extras, y finalmente informe los resultados en la acción
#principal.
def ejercicio4ayf (self):
        print("\n")
        empleados = int(input("¿Cuántos empleados se identificaran? "))
        for i in range(empleados):
            print("\n")
            name = input("Identifiquese con sus nombres y apellidos: ")
            pagohora = int(input("Ingrese el valor cancelado por hora: "))
            horastrabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
            extrahoras = int(input("Ingrese la cantidad de horas extras trabajadas: "))
            if horastrabajadas > 40:
                tarifaextra = pagohora * (35 / 100)
                valorextra = extrahoras * tarifaextra
                print("La cantidad ganada por las horas extras es", valorextra)
                salariosemanal = pagohora * (horastrabajadas - extrahoras)
                print("El salario semanal es de", salariosemanal)
                valorfinal = salariosemanal + valorextra
                print("El valor final a cancelar por horas extras de", name ,"es de", valorfinal)
            else:
                salariosemanal = pagohora * (horastrabajadas - extrahoras)
                print("El salario semanal y final de" , name, "es de", salariosemanal)