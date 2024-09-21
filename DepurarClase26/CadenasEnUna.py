def combinar_cadenas(lista):

    cadena = ""

    for palabra in lista:

        cadena += palabra + " "

    return cadena



lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]

print("Cadena combinada:", combinar_cadenas(lista_cadenas))