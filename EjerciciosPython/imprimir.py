palabra = input("Introduzca una palabra")

# palabra_reverse =reversed(palabra)
# palabra_reverse.reverse


palabra_reverse = palabra[::-1]
print(palabra_reverse)
for letra in palabra_reverse:
    print(letra)
