
n = int(input("Introduce el número de términos de la serie de Fibonacci que deseas ver: "))

a, b = 0, 1

contador = 0

while contador < n:
    print(a)         
    a, b = b, a + b  
    contador += 1    