#Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
#peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
#base en dicha secuencia se desea realizar un estudio a fin de conocer:
# Edad promedio de todas las personas en la muestra.
# Peso promedio de todas las personas en la muestra.
# Estatura promedio de todas las personas en la muestra.
# Cuántas personas hay con edad entre los 18 y 25 años.
# Cuántas personas son mayores a 36 años.
# Cuál es el promedio de peso de las personas con edades entre 18 y 35
#años.
def ejercicio7ei(self):
        print("\n")
        edad=[23,38,42,56,67,72]
        peso=[40,50,60,70,80,90]
        estatura=[1.45,1.56,1.65,1.74,1.86,1.97]
        prom_edad=(sum(edad))/len(edad)
        prom_peso=(sum(peso))/len(peso)
        prom_estatura=(sum(estatura))/len(estatura)
        c=0
        x=0
        while c < 8:
            x+=(edad.count(20+c))
            c+=1  
        c=1
        cal=0  
        while c<150:
            cal+=(edad.count(40+c))
            c+=1
        c=0
        contPos=0
        while c<36:
            contPos=[i for i,x in enumerate(edad) if x>=18 and x<=35]
            c+=1
        suma=0
        c=0
        while c<len(contPos):
            suma+=peso[contPos[0+c]]
            c+=1
        print(contPos)
        print(f"El promedio de edades de todas las personas es de: {prom_edad:.2f}")
        print(f"El promedio de peso de todas las personas es de: {prom_peso:.2f}")
        print(f"El promedio de estatura de todas las personas es de: {prom_estatura:.2f}")
        print(f"Hay {x}, persona(s) con edad de entre [18-25] ")
        print(f"Hay {cal}, personas mayor(es) a 36 años")
        print(f"El promedio de peso entre las personas de 18 a 35 años es: {suma/len(contPos):.2f}")