def invertir_cadena(cadena):
    invertida = ""
    for i in range(len(cadena) - 1, -1, -1):  
        invertida += cadena[i]
    return invertida

cadena = "Python"
print("Cadena invertida:", invertir_cadena(cadena))
