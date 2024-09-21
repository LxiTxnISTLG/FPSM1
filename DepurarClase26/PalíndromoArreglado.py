def es_palindromo(palabra):
    palabra_invertida = ""
    for i in range(len(palabra) - 1, -1, -1):  
        palabra_invertida += palabra[i]
    return palabra == palabra_invertida

palabra = "radar"
print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")
