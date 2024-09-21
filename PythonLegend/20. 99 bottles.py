# Write code below 💖

start = 99

for bottles in range(start, 0, -1):
    print(f"{bottles} bottles of beer on the wall")
    print(f"{bottles} bottles of beer")
    print("Take one down, pass it around")
   
    next_bottles = bottles - 1
    if next_bottles > 0:
        print(f"{next_bottles} bottles of beer on the wall")
    else:
        print("No more bottles of beer on the wall")
    print()  
