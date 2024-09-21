def invertir_cadena(cadena):

    invertida = ""

    for i in range(len(cadena)):

        invertida += cadena[i-1]

    return invertida



cadena = "Python"

print("Cadena invertida:", invertir_cadena(cadena))