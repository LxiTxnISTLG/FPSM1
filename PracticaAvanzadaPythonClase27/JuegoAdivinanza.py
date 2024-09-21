from collections import Counter

def pedir_numeros():
    numeros = []
    while True:
        entrada = input("Ingresa un número (o escribe 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return numeros

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    else:
        mediana = numeros_ordenados[n//2]
    return mediana

def calcular_moda(numeros):
    frecuencia = Counter(numeros)
    moda = frecuencia.most_common(1)[0][0]
    return moda

def calcular_rango(numeros):
    return max(numeros) - min(numeros)

def main():
    numeros = pedir_numeros()
    if len(numeros) == 0:
        print("No se ingresaron números.")
        return
    
    promedio = calcular_promedio(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    rango = calcular_rango(numeros)
    
    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Rango: {rango}")
    
main()
