def factorial(n):

    resultado = 1

    for i in range(1, n + 1):

        resultado *= i

    return resultado



numero = 5

print("Factorial de", numero, "es:", factorial(numero))