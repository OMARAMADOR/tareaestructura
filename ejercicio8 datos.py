#Dado un (1) número binario de cuatro (4) dígitos imprimir su valor
def run():
    nbin = input('Ingrese el número binario a convertir:')
    valor = int(nbin, 2)
    print('La conversión de binario a decimal es:', valor)

if __name__ == "__main__":
    run()