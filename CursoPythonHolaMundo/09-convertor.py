temperatura = float(input("Ingrese temperatura:"))
escala = input ("Es farenheit(F) o es Celsius(C)?:").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
    