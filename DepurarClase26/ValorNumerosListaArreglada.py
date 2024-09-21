def encontrar_maximo(numeros):
    if len(numeros) == 0:
        return "La lista está vacía"
    
    maximo = numeros[0]  
    
    for numero in numeros:
        if numero > maximo:
            maximo = numero
            
    return maximo

lista_numeros = [-10, -20, -30, -5, -15]
print("El valor máximo es:", encontrar_maximo(lista_numeros))

lista_vacia = []
print("El valor máximo es:", encontrar_maximo(lista_vacia))