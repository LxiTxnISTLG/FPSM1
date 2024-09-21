def modificar_cadena(cadena, letra_a_reemplazar, nueva_letra):
    
    cadena_minusculas = cadena.lower()

   
    cadena_reemplazada = cadena_minusculas.replace(letra_a_reemplazar, nueva_letra)

    
    lista_palabras = cadena_reemplazada.split()

    
    print("Cadena modificada:", cadena_reemplazada)
    print("Lista de palabras:", lista_palabras)

cadena = "Python Es Genial"
letra_a_reemplazar = 'e'
nueva_letra = 'x'
modificar_cadena(cadena, letra_a_reemplazar, nueva_letra)
