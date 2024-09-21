hora_24 = input("Ingresa la hora en formato de 24 horas (HH:MM): ")

horas, minutos = map(int, hora_24.split(':'))

if horas == 0:
    periodo = "AM"
    horas_12 = 12
elif horas < 12:
    periodo = "AM"
    horas_12 = horas
elif horas == 12:
    periodo = "PM"
    horas_12 = 12
else:
    periodo = "PM"
    horas_12 = horas - 12

hora_12 = f"{horas_12}:{minutos:02d} {periodo}"

print("La hora en formato de 12 horas es:", hora_12)