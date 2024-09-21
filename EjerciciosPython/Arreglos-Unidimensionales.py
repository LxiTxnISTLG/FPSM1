N = 3

Temp = [0] * N  
suma = 0.0
media = 0.0
C = 0

for i in range(N):
    Temp[i] = float(input(f"Ingrese la temperatura {i + 1}: "))
    suma += Temp[i]


media = suma / N

for i in range(N):
    if Temp[i] >= media:
        C += 1
        print(f"Temperatura mayor o igual a la media: {Temp[i]}")

print(f"La media es: {media}")
print(f"Total de temperaturas mayores o iguales a la media: {C}")