palabra = input("Introduzca una palabra")

invertida = palabra [::-1]
separada = [letra for letra in invertida]

print(f"Palabra invertida:     {invertida}")
print(f"Letras separadas:      {separada} ")

pegada="" 

for letra in separada:
    pegada+=letra 


print(pegada)