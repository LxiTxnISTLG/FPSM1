def calcular_promedio(numeros):
    if len(numeros) == 0:
        return "La lista está vacía"
    
    suma = 0
    for numero in numeros:
        suma += numero

    promedio = suma / len(numeros)
    return promedio

lista_numeros = [10, 20, 30, 40, 50]
print("El promedio es:", calcular_promedio(lista_numeros))

lista_vacia = []
print("El promedio es:", calcular_promedio(lista_vacia))