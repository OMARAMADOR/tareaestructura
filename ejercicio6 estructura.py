#Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que
#informe al usuario qué valor tiene el número mayor y qué valor tiene el número
#menor, sin contar el cero (0).
def ejercicio6ei(self):
        print("\n")
        may = 0
        men = 0
        i = 1
        ntotal = int (input("Ingrese la cantidad de números: "))
        while i <= ntotal:
            ntemp = int (input("Ingrese el número, nota: ingresa cero para terminar: "))
            if i == 1:
                may = ntemp
                men = ntemp
            else:
                if ntemp > may:
                    may = ntemp
                if ntemp < men and ntemp != 0:
                    men = ntemp
            i = i + 1
        print("El número mayor es", may)
        print("El número menor es", men)