umbral = 5.0

def pedir_notas():
    notas = []
    while True:
        nota = input("Ingresa una nota (o escribe 'fin' para terminar): ")
        if nota.lower() == 'fin':
            break
        try:
            nota = float(nota)
            notas.append(nota)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return notas

def filtrar_notas(notas):
    notas_filtradas = []
    for nota in notas:
        if nota >= umbral:  
            notas_filtradas.append(nota)
    return notas_filtradas

def calcular_promedio(notas):
    if len(notas) == 0:  
        return 0
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)
    return promedio

def main():
    notas = pedir_notas()
    notas_filtradas = filtrar_notas(notas)
    notas_excluidas = len(notas) - len(notas_filtradas) 
    promedio = calcular_promedio(notas_filtradas)
    print(f"El promedio de las notas que están por encima del umbral ({umbral}) es: {promedio}")
    print(f"Número de notas excluidas por estar por debajo del umbral: {notas_excluidas}")  

main()
