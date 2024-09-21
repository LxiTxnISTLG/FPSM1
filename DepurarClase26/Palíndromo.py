def es_palindromo(palabra):

    palabra_invertida = ""

    for i in range(len(palabra)):

        palabra_invertida += palabra[i-1]

    return palabra == palabra_invertida



palabra = "radar"

print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")