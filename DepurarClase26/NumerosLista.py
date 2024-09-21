def sumar_lista(numeros):

    suma = 0

    for i in range(len(numeros) + 1):

        suma += numeros[i]

    return suma



lista_numeros = [1, 2, 3, 4, 5]

print("La suma es:", sumar_lista(lista_numeros))