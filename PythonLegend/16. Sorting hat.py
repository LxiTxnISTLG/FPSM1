# Write code below 💖

gryffindor_points = 0
ravenclaw_points = 0
hufflepuff_points = 0
slytherin_points = 0

answer1 = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
if answer1 == 1:
    gryffindor_points += 1
    ravenclaw_points += 1
elif answer1 == 2:
    hufflepuff_points += 1
    slytherin_points += 1
else:
    print("Wrong input.")

answer2 = int(input("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
if answer2 == 1:
    hufflepuff_points += 2
elif answer2 == 2:
    slytherin_points += 2
elif answer2 == 3:
    ravenclaw_points += 2
elif answer2 == 4:
    gryffindor_points += 2
else:
    print("Wrong input.")

answer3 = int(input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
if answer3 == 1:
    slytherin_points += 4
elif answer3 == 2:
    hufflepuff_points += 4
elif answer3 == 3:
    ravenclaw_points += 4
elif answer3 == 4:
    gryffindor_points += 4
else:
    print("Wrong input.")

points = {
    "Gryffindor": gryffindor_points,
    "Ravenclaw": ravenclaw_points,
    "Hufflepuff": hufflepuff_points,
    "Slytherin": slytherin_points
}

max_points = max(points.values())
sorted_houses = [house for house, score in points.items() if score == max_points]

if len(sorted_houses) == 1:
    print(f"You belong to {sorted_houses[0]}!")
else:
    print(f"Multiple houses have the highest score: {', '.join(sorted_houses)}")