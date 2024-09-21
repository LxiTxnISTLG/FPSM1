numeros = [4, 7, 2, 9, 1]
i = 0
mayor = numeros[0]
while i < len(numeros):
 if numeros[i] > mayor:
   mayor = numeros[i]
 i += 1
print("El número mayor es:", mayor)