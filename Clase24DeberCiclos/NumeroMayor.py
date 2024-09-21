
numeros = [4, 7, 2, 9, 1]

i = 0
menor = numeros[0]

while i < len(numeros):
    if numeros[i] < menor:
        menor = numeros[i]
    i += 1

print("El número menor es:", menor)