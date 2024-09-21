def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

lista_numeros = [1, -2, 3, 0, 5, -4, 6]
print("Números pares:", filtrar_pares(lista_numeros))