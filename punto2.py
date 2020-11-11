def mayor_cero(numeros):
    mayor = []
    cont = 0
    for i in numeros:
        if i > 0:
            mayor.append(i)
            cont += 1
    print(f'El total de numeros mayores a cero es: {cont}\n{mayor}')

def prom_positivos(numeros):
    positivos = 0
    cont = 0
    for i in numeros:
        if i > 0:
            positivos += i
            cont += 1
    promedio = positivos/cont
    print(f'El promedio de los positivos es: {promedio}')

def prom_todos(numeros):
    positivos = 0
    cont = 0
    for i in numeros:
        positivos += i
        cont += 1
    promedio = positivos/cont
    print(f'El promedio de todos los numeros es: {promedio}')

def main():
    numeros = [10,54,-2,30,10,-5,-15,11,50,-30]
    mayor_cero(numeros)
    prom_positivos(numeros)
    prom_todos(numeros)


main()