# Write code below 💖

pH = int(input("Enter a pH value (0-14): "))

pHBasic = [8, 9, 10, 11, 12, 13, 14]
pHAcidic = [0, 1, 2, 3, 4, 5, 6]
pHNeutral = 7

if pH in pHBasic:
    print("The pH is basic")
elif pH in pHAcidic:
    print("The pH is acidic")
elif pH == pHNeutral:
    print("The pH is neutral")
else:
    print("Invalid pH value")