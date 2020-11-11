def main():
    final = 1600;
    cont = 2
    aux= 0
    suma = 0
    print(cont)
    while(cont<final):
        if aux %2 == 0:
            cont +=3
        if aux %2 != 0:
            cont +=2
        print(cont)
        suma += cont
        aux +=1
    print(f'La suma de la seria es: {suma}')
main()