frase = "Hola, ¿cómo estás?"
vocales = "aeiouAEIOU"
contador_vocales = 0
for letra in frase:
 if letra in vocales:
    contador_vocales += 1
print("El número de vocales es:", contador_vocales)