numeros = [5, 3, 8, 3, 5, 1, 8, 7]

numeros_sin_duplicados = []

for numero in numeros:
    if numero not in numeros_sin_duplicados:
        numeros_sin_duplicados.append(numero)
print("Arreglo sin duplicados:", numeros_sin_duplicados)