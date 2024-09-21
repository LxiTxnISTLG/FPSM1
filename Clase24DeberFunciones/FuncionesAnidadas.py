def funcionexterior():
    def funcioninterior(valor):
        print(f"Esta es la función interior y el valor recibido es: {valor}")
    
    funcioninterior(42)
    print("Esta es la función exterior")

funcionexterior()