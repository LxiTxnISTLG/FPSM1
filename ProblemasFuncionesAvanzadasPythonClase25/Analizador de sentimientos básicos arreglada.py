palabras_positivas = {
    "bien": 1,
    "genial": 2,
    "fantástico": 3,
    "excelente": 3,
    "feliz": 2
}

palabras_negativas = {
    "mal": 1,
    "terrible": 3,
    "horrible": 3,
    "malo": 2,
    "triste": 2
}

def analizar_sentimiento(texto):
    texto = texto.lower()  

    
    puntaje_positivo = sum(palabras_positivas.get(palabra, 0) for palabra in texto.split())
    puntaje_negativo = sum(palabras_negativas.get(palabra, 0) for palabra in texto.split())

    
    if puntaje_positivo > puntaje_negativo:
        return "Sentimiento positivo"
    elif puntaje_negativo > puntaje_positivo:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

texto = input("Escribe una oración para analizar: ")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")
