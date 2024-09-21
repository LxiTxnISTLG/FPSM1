numeros = [4, 2, 7, 4, 8, 4, 1, 4]

valor_a_contar = 4
contador = 0

for numero in numeros:
    if numero == valor_a_contar:
        contador += 1
print(f"El numero (valor_a_contar) aparece (contador) veces en el arreglo.")