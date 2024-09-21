# Write code below 💖

COP = float(input("Enter the amount in COP: "))
PEN = float(input("Enter the amount in PEN: "))
BRL = float(input("Enter the amount in BRL: "))

COP_TO_USD = 4065.50
PEN_TO_USD = 3.74
BRL_TO_USD = 5.63

USD_FROM_COP = COP / COP_TO_USD
USD_FROM_PEN = PEN / PEN_TO_USD
USD_FROM_BRL = BRL / BRL_TO_USD

leftover = USD_FROM_COP + USD_FROM_PEN + USD_FROM_BRL

print("The leftover is: ", (leftover))
