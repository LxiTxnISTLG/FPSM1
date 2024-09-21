# Escribe un programa que solicite al usuario ingresar un número 
# con decimales y almacenalo en una variable.
# A continuación, el programa debe solicitar al usuario que ingrese
# un número entero y guardarlo en otra variable 
# En una tercera variable se deberpa guaradar el resultado de la suma
# de los dos múmeros ingresados por el usuario
# Por último, se debe mostrar en pantalla el texto 
# Por último, se debe mostrar en panatalla el texto 
# "El resultado de la suma es [suma]", donde "[suma]"
# se reemplazara por el resultado de la operación 

valorDecimal = float (input("ingrese un decimal: "))

valorEntero= int (input("Ingrese un entero: "))

suma = valorDecimal + valorEntero
print ("El resultado de la suma es  " + str (+suma))
# print ("El resultado de la suma es" + str(suma))
