def main():
    numeros = [-5,500,21,4,19,25,18]
    orden = numeros.sort()
    menor = numeros[0]
    mayor = numeros[len(numeros)-1]
    cont = 0
    for i in numeros:
        cont +=i
    promedio = cont/len(numeros)
    print(f'El promedio del arreglo es: {promedio}')
    if menor == mayor:
        print(f'El arreglo no tiene valores diferentes, por lo tanto, no hay mayores o menores')
    else:
        print(f'El menor es: {menor}\nEl mayor es: {mayor} ')
    
main()
