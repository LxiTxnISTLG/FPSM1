
palabras = ["manzana", "banana", "cereza", "manzana", "durazno", "banana", "kiwi"]

palabras_sin_duplicados = []

for palabra in palabras:
    
    if palabra not in palabras_sin_duplicados:
        palabras_sin_duplicados.append(palabra)

print("Arreglo sin duplicados:", palabras_sin_duplicados)