p = input("escriba una palabra: ").lower()

## solucion1
# p_reversa = ""
# for letra in p:
#     p_reversa = letra + p_reversa

# if p == p_reversa:
#    print("es un palindromo")
# else:
#    print("no es un palindromo")

## solucion2
if str(p) == str(p)[::-1]:
   print("es un palindromo")
else:
   print("no es un palindromo")
    
## solucion3

# p1 = list(p)
# p2 = list(p1)
# p2.reverse()
# if p1 == p2:
#     print("Es un palindromo")
# else:
#     print("No es un palindromo")
